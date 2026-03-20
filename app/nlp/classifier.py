#Rule-based
COMPLAINT_WORDS = [
    "slow",
    "bad",
    "problem",
    "not working",
    "error",
    "fail",
    "issue",
    "poor"
]

COMPLIMENT_WORDS = [
    "good",
    "great",
    "excellent",
    "nice",
    "fast",
    "amazing",
    "perfect"
]

def classify(text: str):
    for w in COMPLAINT_WORDS:
        if w in text:
            return "complaint"
        
    for w in COMPLIMENT_WORDS:
        if w in text:
            return "compliment"
    
    return "neutral"
