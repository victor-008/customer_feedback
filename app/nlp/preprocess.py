import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
<<<<<<< HEAD
=======

>>>>>>> 9c77650ec1986b4d289b07b2128ccbab5ca38b38
