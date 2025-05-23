import torch
import nltk
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence
import numpy as np
from sklearn.model_selection import train_test_split
from lemmatiser import Lemmatizer

# Device configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



# Step 1: Load and preprocess the dataset
class LemmatizerDataset(Dataset):
    def __init__(self, data_file):
        self.data = []
        with open(data_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Split line and validate format
                parts = line.strip().split('-')
                if len(parts) == 2:  # Ensure there are exactly two parts
                    self.data.append(parts)
                else:
                    continue
                    #print(f"Skipping invalid line: {line.strip()}")

        self.char_to_idx, self.idx_to_char = self.build_vocab()

    def build_vocab(self):
        chars = set("".join(word for pair in self.data for word in pair))  # Collect unique characters
        char_to_idx = {char: idx + 1 for idx, char in enumerate(sorted(chars))}  # Start from index 1
        char_to_idx['<pad>'] = 0  # Padding token at index 0
        char_to_idx['<sos>'] = len(char_to_idx)  # Sequentially assign <sos>
        char_to_idx['<eos>'] = len(char_to_idx)  # Sequentially assign <eos>
        
        idx_to_char = {idx: char for char, idx in char_to_idx.items()}


        # Adjust the assertion
        assert max(char_to_idx.values()) == len(char_to_idx) - 1, "Vocabulary size mismatch"
        import json
        # Save character mappings
        with open("char_to_idx.json", "w") as f:
            json.dump(char_to_idx, f)

        with open("idx_to_char.json", "w") as f:
            json.dump(idx_to_char, f)
        return char_to_idx, idx_to_char

    def encode(self, word):
        return [self.char_to_idx['<sos>']] + [self.char_to_idx[char] for char in word] + [self.char_to_idx['<eos>']]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        input_word, target_word = self.data[idx]
        input_encoded = self.encode(input_word)
        target_encoded = self.encode(target_word)
        # Debug print to validate encoding
        # print(f"Input Word: {input_word}, Encoded: {input_encoded}")
        return torch.tensor(input_encoded, dtype=torch.long), torch.tensor(target_encoded, dtype=torch.long)


# Collate function to pad sequences in the batch
def collate_fn(batch):
    inputs, targets = zip(*batch)
    inputs = pad_sequence(inputs, batch_first=True, padding_value=0)
    targets = pad_sequence(targets, batch_first=True, padding_value=0)
    return inputs, targets


# Load dataset
data_file = "Huge_Augmented_Dataset.txt"
dataset = LemmatizerDataset(data_file)
# Splitting the dataset into training and validation sets
train_data, val_data = train_test_split(list(range(len(dataset))), test_size=0.1, random_state=42)
train_dataset = torch.utils.data.Subset(dataset, train_data)
val_dataset = torch.utils.data.Subset(dataset, val_data)

# DataLoaders with collate_fn
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True, collate_fn=collate_fn)
val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False, collate_fn=collate_fn)



class Encoder(nn.Module):
    def __init__(self, input_dim, embed_dim, hidden_dim, n_layers, dropout=0.2):
        super().__init__()
        self.embedding = nn.Embedding(input_dim, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, n_layers, batch_first=True, bidirectional=True)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, src_lengths):
        embedded = self.dropout(self.embedding(x))  # Shape: (batch_size, seq_len, embed_dim)
        packed = nn.utils.rnn.pack_padded_sequence(embedded, src_lengths.cpu(), batch_first=True, enforce_sorted=False)
        packed_outputs, (hidden, cell) = self.lstm(packed)
        outputs, _ = nn.utils.rnn.pad_packed_sequence(packed_outputs, batch_first=True)

        # Combine forward and backward states for hidden and cell
        hidden = self._combine_directions(hidden)
        cell = self._combine_directions(cell)
        return outputs, hidden, cell

    def _combine_directions(self, states):
        # Combine forward and backward states
        num_layers = states.size(0) // 2
        batch_size = states.size(1)
        hidden_dim = states.size(2)
        combined = states.view(num_layers, 2, batch_size, hidden_dim).mean(dim=1)
        return combined  # Shape: (num_layers, batch_size, hidden_dim)

class Attention(nn.Module):
    def __init__(self, enc_hidden_dim, dec_hidden_dim):
        super().__init__()
        self.attn = nn.Linear((enc_hidden_dim * 2) + dec_hidden_dim, dec_hidden_dim)
        self.v = nn.Parameter(torch.rand(dec_hidden_dim))

    def forward(self, hidden, encoder_outputs):
        src_len = encoder_outputs.shape[1]
        hidden = hidden.unsqueeze(1).repeat(1, src_len, 1)
        energy = torch.tanh(self.attn(torch.cat((hidden, encoder_outputs), dim=2)))
        attention = torch.sum(self.v * energy, dim=2)
        return torch.softmax(attention, dim=1)

class Decoder(nn.Module):
    def __init__(self, output_dim, embed_dim, enc_hidden_dim, dec_hidden_dim, n_layers, attention, dropout=0.2):
        super().__init__()
        self.output_dim = output_dim
        self.attention = attention
        self.embedding = nn.Embedding(output_dim, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM((enc_hidden_dim * 2) + embed_dim, dec_hidden_dim, n_layers, batch_first=True)
        self.fc_out = nn.Linear((enc_hidden_dim * 2) + dec_hidden_dim + embed_dim, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, hidden, cell, encoder_outputs):
        x = x.unsqueeze(1)
        embedded = self.dropout(self.embedding(x))
        attention_weights = self.attention(hidden[-1], encoder_outputs)
        attention_weights = attention_weights.unsqueeze(1)
        weighted = torch.bmm(attention_weights, encoder_outputs)
        rnn_input = torch.cat((embedded, weighted), dim=2)
        output, (hidden, cell) = self.lstm(rnn_input, (hidden, cell))
        prediction = self.fc_out(torch.cat((output.squeeze(1), weighted.squeeze(1), embedded.squeeze(1)), dim=1))
        return prediction, hidden, cell, attention_weights

class Seq2Seq(nn.Module):
    def __init__(self, encoder, decoder, device):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.device = device

    def forward(self, src, trg, teacher_forcing_ratio=0.5):
        trg_len = trg.shape[1]
        batch_size = src.shape[0]
        trg_vocab_size = self.decoder.output_dim

        outputs = torch.zeros(batch_size, trg_len, trg_vocab_size).to(self.device)
        src_lengths = (src != 0).sum(dim=1)  # Calculate sequence lengths

        encoder_outputs, hidden, cell = self.encoder(src, src_lengths)

        input = trg[:, 0]
        for t in range(1, trg_len):
            output, hidden, cell, _ = self.decoder(input, hidden, cell, encoder_outputs)
            outputs[:, t, :] = output
            teacher_force = np.random.random() < teacher_forcing_ratio
            input = trg[:, t] if teacher_force else output.argmax(1)
        return outputs




import torch.optim as optim
import matplotlib.pyplot as plt

# Hyperparameters
INPUT_DIM = len(dataset.char_to_idx)
OUTPUT_DIM = len(dataset.char_to_idx)
EMBED_DIM = 64
ENC_HIDDEN_DIM = 128
DEC_HIDDEN_DIM = 128
N_LAYERS = 2
DROPOUT = 0.3
LEARNING_RATE = 0.001
EPOCHS = 3

import json

# Save character mappings
with open("char_to_idx.json", "w", encoding='utf-8') as f:
    json.dump(dataset.char_to_idx, f, ensure_ascii=False, indent=4)

with open("idx_to_char.json", "w", encoding='utf-8') as f:
    json.dump(dataset.idx_to_char, f, ensure_ascii=False, indent=4)

# Save the model architecture configuration
config = {
    "INPUT_DIM": INPUT_DIM,
    "OUTPUT_DIM": OUTPUT_DIM,
    "EMBED_DIM": EMBED_DIM,
    "ENC_HIDDEN_DIM": ENC_HIDDEN_DIM,
    "DEC_HIDDEN_DIM": DEC_HIDDEN_DIM,
    "N_LAYERS": N_LAYERS,
    "DROPOUT": DROPOUT,
}
with open("model_config.json", "w", encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=4)



# Initialize model, optimizer, and loss function
attention = Attention(ENC_HIDDEN_DIM, DEC_HIDDEN_DIM)
encoder = Encoder(INPUT_DIM, EMBED_DIM, ENC_HIDDEN_DIM, N_LAYERS, DROPOUT).to(device)
decoder = Decoder(OUTPUT_DIM, EMBED_DIM, ENC_HIDDEN_DIM, DEC_HIDDEN_DIM, N_LAYERS, attention, DROPOUT).to(device)
model = Seq2Seq(encoder, decoder, device).to(device)

optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
criterion = nn.CrossEntropyLoss(ignore_index=0)



# Load the saved model
MODEL_SAVE_PATH = "best_lemmatizer_model_2.pth"
model.load_state_dict(torch.load(MODEL_SAVE_PATH, map_location=torch.device('cpu')))
model.eval()

def predict_lemmatized_word(model, word, dataset):
    """
    Predict the root form of a given word using the trained model.
    Args:
        model: Trained Seq2Seq model.
        word: Input word as a string.
        dataset: Instance of LemmatizerDataset for encoding and decoding.
    Returns:
        Predicted root word as a string.
    """
    # Encode the input word
    encoded_word = torch.tensor([dataset.encode(word)], dtype=torch.long).to(device)

    # Pass through the encoder
    with torch.no_grad():
        encoder_outputs, hidden, cell = model.encoder(encoded_word, (encoded_word != 0).sum(dim=1))
        input_token = torch.tensor([dataset.char_to_idx["<sos>"]], dtype=torch.long).to(device)

        # Decode the output
        predicted_word = []
        for _ in range(50):  # Max output length
            output, hidden, cell, _ = model.decoder(input_token, hidden, cell, encoder_outputs)
            token_idx = output.argmax(1).item()
            if token_idx == dataset.char_to_idx["<eos>"]:
                break
            predicted_word.append(dataset.idx_to_char[token_idx])
            input_token = torch.tensor([token_idx], dtype=torch.long).to(device)

    return "".join(predicted_word)

def predict_sentece(test_words):
    test_words = test_words.split()
    predicted_list = []
    for surface_form in test_words:
        model_based_root = predict_lemmatized_word(model, surface_form, dataset)
        rule_based_root = Lemmatizer(surface_form)
        final_prediction = ""
        if(rule_based_root==surface_form):
            final_prediction = predict_lemmatized_word(model, surface_form, dataset)
        else:
            if len(rule_based_root)<len(model_based_root):
                final_prediction = rule_based_root
            else:
                final_prediction = model_based_root        
        predicted_list.append(final_prediction)
    return predicted_list





