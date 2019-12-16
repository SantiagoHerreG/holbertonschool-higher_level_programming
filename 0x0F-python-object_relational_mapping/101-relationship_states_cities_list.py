#!/usr/bin/python3
"""Queries a list of States
"""
import sys
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State

if __name__ == "__main__":
    """Lists all State objects
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).all()
    for states in query:
        print("{}: {}".format(states.id, states.name))
        for cit in states.cities:
            print("\t{}: {}".format(cit.id, cit.name))

    session.close()
