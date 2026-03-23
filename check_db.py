from app.database.db import SessionLocal
from app.database.models import Feedback

db = SessionLocal()

rows = db.query(Feedback).all()

for r in rows:
    print(r.id, r.text, r.final_solution)

db.close()