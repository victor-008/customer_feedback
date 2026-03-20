from app.services.feedback_service import process_feedback


text = "The Airtel internet is so bad, I would dispose it"

result = process_feedback(text)

print(result)