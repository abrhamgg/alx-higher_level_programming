#!/usr/bin/python3
"""
script that deletes all State objects which includes 'a' from the database
"""
import sys
from sqlalchemy import MetaData, create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).filter(State.name.like("%a%")).all()
    for d in data:
        session.delete(d)
        session.commit()
    '''
    for state in session.query(State):
        if 'a' in state.name:
            print(state)
            session.delete(state)
            session.commit()
'''
