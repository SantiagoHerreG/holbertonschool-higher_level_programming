#!/usr/bin/python3
"""Creates the State California with the City San
Francisco from the database hbtn_0e_100_usa
"""
import sys
from relationship_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State

if __name__ == "__main__":
    """Creates a State and a City
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    id_obj = session.query(State).filter(State.id == '1')\
        .order_by(State.id.desc()).first()

    if id_obj.id is None:
        cal = State(name="California", id='1')
    else:
        new_id = id_obj.id + 1
        new_id = str(new_id)
        cal = State(name="California", id=new_id)
    session.add(cal)
    San_f = City(name="San Francisco", state_id=cal.id)
    session.add(San_f)

    session.commit()
    session.close()
