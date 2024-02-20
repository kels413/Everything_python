"""
steps:
    1: import sqlalchemy
    2. import columns, strings, intergers, primary key, create_engine
    3. import declartive base
    4. create a connection
    5. create a class and inherit from the declarative class
    6. call the declarative class (Base) and create all Table.
"""

import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# create connection
#'mysql+mysqlconnector://username:password@host:port/database'
engine = create_engine('mysql+mysqlconnector://root:31006569@localhost:3306/hbtn_0e_0_usa')
print(engine)


