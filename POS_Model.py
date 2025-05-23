verb_tags = ['V_VM_VF', 'V_VAUX']
naming_word_tags = [
    'N_NN', 'N_NNP', 'N_NST',
    'PR_PRP', 'PR_PRF', 'PR_PRL', 'PR_PRC', 'PR_PRQ',
    'DM_DMD', 'DM_DMR', 'DM_DMQ',
    'JJ', 'RB', 'PSP',
    'CC_CCD', 'CC_CCS', 'CC_CCS_UT',
    'RP_RPD', 'RP_CL', 'RP_INJ', 'RP_INTF', 'RP_NEG',
    'QT_QTF', 'QT_QTC', 'QT_QTO',
    'RD_RDF', 'RD_SYM', 'RD_PUNC', 'RD_UNK', 'RD_ECH'
]
verbal_tags = ['V_VM_VNF', 'V_VM_VINF', 'V_VM_VNG', 'N_NNV']

import pandas as pd
import torch
import pickle
import numpy as np
from transformers import BertTokenizer, BertForTokenClassification, AdamW
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
import logging

logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

# Initialize tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

# Define paths
file_path = 'output.conllu'  # Update with actual file path
tag_to_id_path = 'old_tag_to_id.pkl'
best_model_save_path = 'old_best_pos_tagger_model.pth'

# Function to read CoNLL-U format file
def read_conllu(file_path):
    sentences, pos_tags = [], []
    with open(file_path, 'r', encoding='utf-8') as file:
        current_sentence, current_tags = [], []
        for line in file:
            if line.startswith('#'):
                continue
            elif line.strip() == "":
                if current_sentence:
                    sentences.append(current_sentence)
                    pos_tags.append(current_tags)
                current_sentence, current_tags = [], []
            else:
                parts = line.split('\t')
                if len(parts) > 3:
                    current_sentence.append(parts[1])  # Word
                    current_tags.append(parts[3])  # POS Tag

    if current_sentence:
        sentences.append(current_sentence)
        pos_tags.append(current_tags)

    return sentences, pos_tags

# Read data
sentences, pos_tags = read_conllu(file_path)

# Create tag-to-ID mapping
unique_tags = set(tag for tags in pos_tags for tag in tags)
tag_to_id = {tag: idx for idx, tag in enumerate(unique_tags)}
tag_to_id['O'] = len(tag_to_id)  # Handling unknown tags

# Save tag_to_id dictionary
with open(tag_to_id_path, 'wb') as f:
    pickle.dump(tag_to_id, f)

# Function to encode sentences and tags
def encode_tags(texts, tags, max_length):
    input_ids, attention_masks, tag_ids = [], [], []

    for i, text in enumerate(texts):
        encoded = tokenizer.encode_plus(text, is_split_into_words=True, max_length=max_length, padding='max_length', truncation=True)
        input_ids.append(encoded['input_ids'])
        attention_masks.append(encoded['attention_mask'])

        encoded_tags = [tag_to_id.get(tag, tag_to_id['O']) for tag in tags[i]]
        encoded_tags += [tag_to_id['O']] * (max_length - len(encoded_tags))  # Padding

        tag_ids.append(encoded_tags)

    return torch.tensor(input_ids), torch.tensor(attention_masks), torch.tensor(tag_ids)

# Encode the dataset
max_length = 128
input_ids, attention_masks, tag_ids = encode_tags(sentences, pos_tags, max_length)

# Split data into train, validation, and test
train_inputs, test_inputs, train_tags, test_tags = train_test_split(input_ids, tag_ids, test_size=0.1, random_state=42)
train_masks, test_masks, _, _ = train_test_split(attention_masks, attention_masks, test_size=0.1, random_state=42)

train_inputs, val_inputs, train_tags, val_tags = train_test_split(train_inputs, train_tags, test_size=0.1, random_state=42)
train_masks, val_masks, _, _ = train_test_split(train_masks, train_masks, test_size=0.1, random_state=42)

# Create Dataset class
class POSDataset(Dataset):
    def __init__(self, input_ids, attention_masks, tags):
        self.input_ids = input_ids
        self.attention_masks = attention_masks
        self.tags = tags

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return {
            'input_ids': self.input_ids[idx],
            'attention_mask': self.attention_masks[idx],
            'labels': self.tags[idx]
        }

# Create DataLoaders
batch_size = 32
train_dataset = POSDataset(train_inputs, train_masks, train_tags)
val_dataset = POSDataset(val_inputs, val_masks, val_tags)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Load BERT model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BertForTokenClassification.from_pretrained('bert-base-multilingual-cased', num_labels=len(tag_to_id))
model.to(device)

optimizer = AdamW(model.parameters(), lr=5e-5)

best_val_loss = float("inf")  # Initialize with a high value



# In[1]:


import torch
import pickle
from transformers import BertTokenizer, BertForTokenClassification

# Define paths
tag_to_id_path = 'old_tag_to_id.pkl'
best_model_save_path = 'old_best_pos_tagger_model.pth'

# Load tag_to_id dictionary
with open(tag_to_id_path, 'rb') as f:
    tag_to_id = pickle.load(f)

# Load tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

# Load best trained model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BertForTokenClassification.from_pretrained('bert-base-multilingual-cased', num_labels=len(tag_to_id))
model.load_state_dict(torch.load(best_model_save_path, map_location=device))
model.to(device)
model.eval()

# Reverse dictionary for ID-to-tag mapping
id_to_tag = {id: tag for tag, id in tag_to_id.items()}

# Function to predict POS tags
def predict_pos_tags(sentence, tokenizer, model, tag_to_id, max_length=128):
    inputs = tokenizer(sentence, is_split_into_words=True, return_tensors="pt", padding='max_length', max_length=max_length, truncation=True)
    input_ids, attention_mask = inputs["input_ids"].to(device), inputs["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
    logits = outputs.logits

    # Extract predictions for non-padding tokens
    active_logits = logits.view(-1, model.num_labels)[attention_mask.view(-1) == 1]
    predicted_ids = torch.argmax(active_logits, axis=1)
    predicted_tags = [id_to_tag[id.item()] for id in predicted_ids]

    return sentence, predicted_tags[:len(sentence)]

def tag_POS(sen):
    sentence_string = sen
    sentence = sentence_string.split()
    tokens, predicted_tags = predict_pos_tags(sentence, tokenizer, model, tag_to_id)
    new_predicted_tags = list()
    for tag in predicted_tags:
        if tag in verb_tags:
            new_predicted_tags.append("VB")
        elif tag in verbal_tags:
            new_predicted_tags.append("VBL")
        else:
            new_predicted_tags.append("NW")
    return new_predicted_tags









