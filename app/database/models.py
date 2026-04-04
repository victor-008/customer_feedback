from sqlalchemy import Column, Integer, String, Text, DateTime, LargeBinary
from datetime import datetime
from app.database.db import Base

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    category = Column(String)
    #complaint / compliment
    problem = Column(String)
    suggestion = Column(Text)
    rule_suggestion = Column(Text)
    llm_analysis = Column(Text)
    final_solution = Column(Text)
    embedding = Column(LargeBinary)

    created_at = Column(
        DateTime, 
        default=datetime.utcnow)