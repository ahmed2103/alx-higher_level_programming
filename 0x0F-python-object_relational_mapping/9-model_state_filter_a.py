#!/usr/bin/python3

"""
script that lists all State objects that contain the letter `a`
 from the database `hbtn_0e_6_usa`
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1],argv[2],argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session(engine)
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id.asc()).all()
    for state in states:
        print(state.id, state.name, sep=": ")
    session.close()