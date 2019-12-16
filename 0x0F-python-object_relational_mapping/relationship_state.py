#!/usr/bin/python3
"""New class for SQLAlquemy to link to a table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ New class for linking to a table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(City, backref="state", cascade="all, delete-orphan")
