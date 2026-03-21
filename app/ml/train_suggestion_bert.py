import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import(
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments
)

from datasets import Dataset

MODEL_NAME = "bert-base-uncased"
MODEL_DIR = "models/suggestion_classifier"

df = pd.read_csv("data/suggestion_dataset.csv")
train_df, test_df = train_test_split(df,test_size=0.2)
train_dataset = Dataset.from_pandas(train_df)
test_datset = Dataset.from_pandas(test_df)

tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

def tokenize(example):
    return tokenizer(
        example["text"],
        padding="max_length",
        truncation = True
    )

train_dataset = train_dataset.map(tokenize)
test_datset = test_datset.map(tokenize)

train_dataset.set_format(
    type="torch",
    columns=["input_ids", "attention_mask", "label"]
)
test_datset.set_format(
    type="torch",
    columns=["input_ids","attention_mask","label"]
)

model = BertForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2
)

training_args = TrainingArguments(
    output_dir="models/results2",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=3,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_datset,
)

trainer.train()

model.save_pretrained(MODEL_DIR)
tokenizer.save_pretrained(MODEL_DIR)

print("Suggestion model saved")