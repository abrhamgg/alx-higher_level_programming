#!/usr/bin/python3
"""
script that prints all cities from the database
"""
import sys

from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()
    for s, c in data:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
