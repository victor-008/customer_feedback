SOLUTION_WORDS = [
    "should",
    "suggest",
    "recommend",
    "please",
    "try",
    "fix",
    "install",
    "replace"
]

def detect_solution(text: str):
    for w in SOLUTION_WORDS:
        if w in text:
            return True
    
    return False