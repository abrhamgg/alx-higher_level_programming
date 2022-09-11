#!/usr/bin/python3
"""
script that creates the State “California”
 with the City “San Francisco” from the database"""
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
    session.add(City(name='San Francisco', state=State(name="California")))
    session.commit()
