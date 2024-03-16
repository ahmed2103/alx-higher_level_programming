#!/usr/bin/python3

"""
script that adds the State object “Louisiana” to the database `hbtn_0e_6_usa`
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    new_state = session.query(State).filter_by(name="Louisiana").first()
    print(new_state.id)
    session.commit()
    session.close()
