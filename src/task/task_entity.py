from sqlalchemy import Column, Integer, String, Boolean
from src.db import Base

class Task(Base):
  __tablename__ = 'task'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  status = Column(Boolean)

  def __init__(self, name, status):
    self.name = name
    self.status = status

  def __iter__(self):
    yield 'name', self.name
    yield 'status', self.status
    yield 'id', self.id
