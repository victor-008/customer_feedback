from app.services.feedback_service import process_feedback


text = "The Airtel internet is so bad, I would dispose it"
text = "The network router at main office is not working, restore power supply"
text = "jamani tufanye jambo tuomoke tutoke block"
text = "Internet is slow, you should upgrade bandwidth"

result = process_feedback(text)

print(result)