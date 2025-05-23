# Morphological_Analysis

This project involves training models using two Jupyter notebooks to generate `.pth` files, which are then used by a Python script (`main.py`) to perform downstream tasks such as lemmatization, tagging, or prediction.

---

## How to Run This Project

### Step 1: Train Models

Run the following two notebooks in order to generate the required `.pth` model files:

- `Working_POS.ipynb`
- `bi_lstm_attention_training_code.ipynb`

After successful execution, `.pth` files (PyTorch model checkpoints) will be saved automatically in the current directory.

---

###  Step 2: Run the Main Script

Note: The script uses a predefined variable called "inp" to store the input sentence for processing. You can modify the inp variable inside main.py to use any custom input

Once the `.pth` files(best_lemmatizer_model_2.pth, old_best_pos_tagger_model) are generated, you can run the main pipeline:

```bash
python3 main.py


