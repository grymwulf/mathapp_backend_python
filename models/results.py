from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer,
        primary_key=True,
        nullable=False)

    answers = Column(JSON, 
        nullable=False)
    
    test_id = Column(Integer,
        ForeignKey('test.id'))

    teacher_id = Column(Integer, 
        ForeignKey('teacher.id'))

    student_id = Column(Integer,
        ForeignKey('student.id'))

    num_correct = Column(Integer,
        nullable=False)

    num_questions = Column(Integer,
        nullable=False)

    

