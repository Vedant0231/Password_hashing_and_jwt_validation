from app.database.database import Base
from sqlalchemy import String, Integer, Column


"""model for user signup and login table"""
class Userauth(Base):
    __tablename__ = "userauth"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
