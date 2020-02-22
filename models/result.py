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
    
    testId = Column(Integer,
        ForeignKey('test.id'))

    teacherId = Column(Integer, 
        ForeignKey('teacher.id'))

    studentId = Column(Integer,
        ForeignKey('student.id'))

    numCorrect = Column(Integer,
        nullable=False)

    numQuestions = Column(Integer,
        nullable=False)

    

