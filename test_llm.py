from app.nlp.pipeline import process_feedback

text = "Internet is slow, you should upgrade bandwidth"

result = process_feedback(text)

print(result)