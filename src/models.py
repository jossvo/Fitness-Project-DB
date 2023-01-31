import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
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
    location = Column(String(250), nullable=False)
    share_location = Column(Boolean(), nullable=False)
    weight = Column(String(250), nullable=False)
    share_weight = Column(Boolean(), nullable=False)
    height = Column(String(250), nullable=False)
    share_height = Column(Boolean(), nullable=False)
    bio = Column(String(250))
    # workouts - done by table Workout_User
    # reviews:
    #   -wk reviews
    #   coach reviews
    # wk progress - in progress

class Coach(Base):
    __tablename__ = 'coach'
    id = Column(Integer(), primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    bio = Column(String(250))
    socials = Column(String(250), nullable=False)
    # custom exercise videos library
    # custom exercises library
    # wks library
    # general reviews
    # no. wks bought
    # no. custom plans bought
    # general rating

class Workout(Base):
    __tablename__ = "workout"
    id = Column(Integer(),primary_key=True)
    coach_id = Column(Integer(),ForeignKey("coach.id"))
    coach = relationship(Coach)
    name = Column(String(250), nullable=False)
    weeks = Column(Integer())
    days_per_week = Column(Integer())
    difficulty = Column(String(30), nullable=False)
    description = Column(String(250), nullable=False) #summary
    isfree = Column(Boolean(), nullable=False)
    exercise_count = Column(Integer())
    # image
    # classifications
    # reviews

class Exercise_Video(Base):
    __tablename__ = "exercise_video"
    id = Column(Integer(),primary_key=True)
    coach_id = Column(Integer(),ForeignKey("workout.id",ondelete="cascade"))
    coach = relationship(Coach)

class Exercise(Base):
    __tablename__ = "exercise"
    id = Column(Integer(),primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    video_id = Column(Integer(),ForeignKey("exercise_video.id"))
    video = relationship(Exercise_Video)
    # wk program OTM
    
class Category(Base):
    __tablename__ = "category"
    id = Column(Integer(),primary_key=True)
    name = Column(String(250), nullable=False)
    icon = Column(String(250), nullable=False)

class Exercise_Assign(Base):
    __tablename__ = "exercise_assign"
    id = Column(Integer(),primary_key=True)
    workout_id = Column(Integer(),ForeignKey("workout.id",ondelete="cascade"))
    workout = relationship(Workout)
    week = Column(Integer())
    day = Column(Integer())
    order = Column(Integer())
    # tener la información
    # exercise_id = Column(Integer(),ForeignKey("exercise.id",ondelete="cascade"))
    # exercise = relationship(Exercise)
    sets = Column(Integer())
    reps = Column(Integer())
    rest_between_sets = Column(Float())
    video_id = Column(Integer(),ForeignKey("exercise_video.id",ondelete="cascade"))
    video = relationship(Exercise_Video)
    description = Column(String(250))
    

class Workout_User(Base):
    __tablename__ = "workout_user"
    id = Column(Integer(),primary_key=True)
    workout_id = Column(Integer(),ForeignKey("workout.id",ondelete="cascade"))
    workout = relationship(Workout)
    user_id = Column(Integer(),ForeignKey("user.id",ondelete="cascade"))
    user = relationship(User)
    exercise_assign_id = Column(Integer(),ForeignKey("exercise_assign.id",ondelete="cascade"))
    exercise = relationship(Exercise_Assign)
    # progress = should we add a table?

class Workout_Review(Base):
    __tablename__ = "workout_review"
    id = Column(Integer(),primary_key=True)
    workout_id = Column(Integer(),ForeignKey("workout.id",ondelete="cascade"))
    workout = relationship(Workout)
    user_id = Column(Integer(),ForeignKey("user.id",ondelete="cascade"))
    user = relationship(User)
    rating = Column(Integer())

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

