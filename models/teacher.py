from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer,
        primary_key=True,
        nullable=False)

    firstName = Column(String,
        nullable=False)

    lastName = Column(String,
        nullable=False)

    students = relationship("Student", 
        back_populates="students")