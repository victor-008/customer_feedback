from app.services.db_service import save_feedback

data = {
    "text": "Internet is slow",
    "category": "complaint",
    "problem": "slow internet",
    #"customer_solution": None,
    "solution_valid": None,
    "recommended_solution": "check router"
}

save_feedback(data)
print("Saved")