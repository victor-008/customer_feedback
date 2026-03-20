VALID_SOLUTIONS = [
    "restart",
    "replace",
    "install",
    "upgrade",
    "check",
    "repair"
]


def evaluate_solution(text: str):
    for w in VALID_SOLUTIONS:
        if w in text:
            return "valid"
        
    return "unknown"