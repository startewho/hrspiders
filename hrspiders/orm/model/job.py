from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime

Base = declarative_base()

class Job(Base):
    __tablename__ = 'job'

    url = Column(String, primary_key=True)
    name = Column(String)
    salary= Column(String)
    region= Column(String)
    workplace= Column(String)
    cp_name= Column(String)
    cp_type= Column(String)
    cp_scale= Column(String)
    industry= Column(String)
    exp= Column(String)
    edu= Column(String)
    demand= Column(String)
    pubdate= Column(String)
    skill= Column(String)
    welfare= Column(String)
    detail= Column(String)
    kw= Column(String)
    collect_date= Column(DateTime)