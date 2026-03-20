from app.services.feedback_service import process_feedback


text = "The internet is slow, you should restart the router"

result = process_feedback(text)

print(result)