from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer,
        primary_key=True,
        nullable=False)
    
    graded = Column(Boolean,
        nullable=False)

    baseNumber = Column(Integer,
        nullable=False)

    operator = Column(String,
        nullable=False)

    attemptsAllowed = Column(Integer,
        nullable=False)

    student = relationship("Student",
        back_populates="student")
        
    teacher = relationship("Teacher",
        back_populates="teacher")

    