# SOLUTION_WORDS = [
#     "should",
#     "suggest",
#     "recommend",
#     "please",
#     "try",
#     "fix",
#     "install",
#     "replace"
# ]

# def detect_solution(text: str):
#     for w in SOLUTION_WORDS:
#         if w in text:
#             return True
    
#     return False


#using bert
from app.ml.suggestion_predict import has_suggestion

def detect_solution(text):
    if has_suggestion(text):
        return text
    return None