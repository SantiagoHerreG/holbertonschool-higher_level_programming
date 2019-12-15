#!/usr/bin/python3
"""Link class to table in database
"""
import sys
import re
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

    regex_composite = re.compile(r"^[\w\"\']+[\w ]+[\"\']?")
    state_name = regex_composite.fullmatch(sys.argv[4])

    state_res = session.query(State)\
        .order_by(State.id)\
        .filter(State.name == state_name.group(0))\
        .first()

    if state_res:
        print(state_res.id)
    else:
        print("Not found")
