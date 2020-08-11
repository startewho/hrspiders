from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime

Base = declarative_base()

class Area(Base):
    __tablename__ = 'area'

    id = Column(Integer, primary_key=True)
    area_code = Column(String)
    area_simple= Column(String)
    phone_code= Column(String)
    name= Column(String)
    pid= Column(Integer)