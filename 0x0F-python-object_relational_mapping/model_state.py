#!/usr/bin/python3
""" Write a python file that contains the class definition
of a State and an instance Base = declarative_base() """

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class State"""
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128))
