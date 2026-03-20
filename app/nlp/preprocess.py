import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


#from app.nlp.preprocess import clean_text
#print(clean_text("Internet is SLOW!!"))