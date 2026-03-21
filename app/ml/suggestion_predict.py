import torch
from transformers import BertTokenizer, BertForSequenceClassification

MODEL_DIR = "models/suggestion_classifier"

tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
model = BertForSequenceClassification.from_pretrained(MODEL_DIR)

def has_suggestion(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits).item()
    return bool(pred)