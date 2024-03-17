"""
sqlalchemy a module that helps us map python objects to database.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://{}:{}@{}{}'.format())



Base = declarative_base()


