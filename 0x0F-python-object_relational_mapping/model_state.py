#!/usr/bin/python3

"""script to create table `state` using sqlalchemy"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """class to create table `state`"""

    __tablename__ = "state"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
