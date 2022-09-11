#!/usr/bin/python3
"""
script that lists all State objects from the database
"""
import sys
from sqlalchemy import MetaData, create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        if state.id == 2:
            state.name = 'New Mexico'
    session.commit()
