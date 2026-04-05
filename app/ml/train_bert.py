import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments
)
from datasets import Dataset

MODEL_NAME = "bert-base-uncased"
MODEL_DIR = "models/bert_classifier"

df = pd.read_csv("data/feedback_dataset.csv")
labels = {"complaint":0, "compliment":1}
df["label"] = df["label"].map(labels)

train_df, test_df = train_test_split(df, test_size=0.2)
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

def tokenize(example):
    return tokenizer(
        example["text"],
        padding="max_length",
        truncation=True
    )

train_dataset = train_dataset.map(tokenize)
test_dataset = test_dataset.map(tokenize)

train_dataset.set_format(
    type="torch",
    columns=["input_ids", "attention_mask", "label"]
)
test_dataset.set_format(
    type="torch",
    columns=["input_ids", "attention_mask", "label"]
)

model = BertForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2
)

training_args = TrainingArguments(
    output_dir="models/results",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
<<<<<<< HEAD
    #evaluation_strategy="epoch",
)
=======
>>>>>>> 9c77650ec1986b4d289b07b2128ccbab5ca38b38

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

trainer.train()

model.save_pretrained(MODEL_DIR)
tokenizer.save_pretrained(MODEL_DIR)

print("bERT model saved")