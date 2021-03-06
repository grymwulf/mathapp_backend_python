from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer,
        primary_key=True,
        nullable=False)

    firstName = Column(String,
        nullable=False)

    lastName = Column(String,
        nullable=False)

    teacherId = Column(Integer,
        ForeignKey('teacher.id'))

    teacher = relationship("Teacher",
        back_populates="student")