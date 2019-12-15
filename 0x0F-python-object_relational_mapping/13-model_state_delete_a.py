#!/usr/bin/python3
"""Link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Prints a query from a table mapped using SQLAlchemy
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for elem in to_delete:
        session.delete(elem)

    session.commit()
    session.close()
