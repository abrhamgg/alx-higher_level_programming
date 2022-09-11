#!/usr/bin/python3
"""
script that prints the first State object from
the database
"""
import sys

from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(engine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    if first is None:
        print('Nothing')
    else:
        print('{}: {}'.format(first.id, first.name))
