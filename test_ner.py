from app.nlp.problem_extractor import extract_problem
text = "Internet router at Nairobi office is not working "
print(extract_problem(text))