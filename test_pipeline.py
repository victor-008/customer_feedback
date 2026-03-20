from app.nlp.pipeline import run_pipeline

text = "Internet is slow, you should restart the router"

result = run_pipeline(text)

print(result)