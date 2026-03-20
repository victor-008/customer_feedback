from app.database.db import engine
from app.database.models import Base

#from app.models.feedback import Feedback     ###adeeeeeeeeeeeeeeeeeeeddd

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()