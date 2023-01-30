import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    name = Column(String(250), nullable=False)
    alias = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    share_gender = Column(Boolean(), nullable=False)
    password = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    share_adress = Column(Boolean(), nullable=False)
    weight = Column(String(250), nullable=False)
    bio = Column(String(250))

class Coach(Base):
    __tablename__ = 'coach'
    id = Column(Integer(), primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    bio = Column(String(250))
    socials = Column(String(250), nullable=False)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

