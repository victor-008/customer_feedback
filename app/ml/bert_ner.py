from transformers import pipeline

ner_pipeline = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

def extract_entities(text: str):
    results = ner_pipeline(text)
    entities = []
    for r in results:
        entities.append(r["word"])
    return entities