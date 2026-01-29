from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"  # Название вашей таблицы в БД
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=False, index=False)
    # Добавьте остальные поля из вашей таблицы, например:
    # username = Column(String)
    # email = Column(String)
    # password = Column(String)