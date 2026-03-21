import torch
from transformers import BertTokenizer, BertForSequenceClassification

MODEL_DIR = "models/bert_classifier"

tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
model = BertForSequenceClassification.from_pretrained(MODEL_DIR)

labels = {
    0: "complaint",
    1: "compliment"
}

def predict_label(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding = True
    )

    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits).item()
    return labels[predicted_class]