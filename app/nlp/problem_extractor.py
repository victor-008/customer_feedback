# PROBLEM_KEYWORDS = [
#     "internet",
#     "power",
#     "network",
#     "water",
#     "server",
#     "router",
#     "system",
#     "connection"
# ]

# def extract_problem(text: str):
#     found = []

#     for p in PROBLEM_KEYWORDS:
#         if p in text:
#             found.append(p)
    
#     if found:
#         return ", ".join(found)
    
#     return None

#problem extractor using NER
from app.ml.bert_ner import extract_entities

def extract_problem(text:str):
    entities = extract_entities(text)
    if not entities:
        return None
    return ", ".join(entities)