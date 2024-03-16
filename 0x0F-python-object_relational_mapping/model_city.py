#!/usr/bin/python3

"""
script to create table `city` using SQLAlchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, String, Column)
Base = declarative_base()

class City(Base):
    """class to create city object"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
