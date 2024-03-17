from model import States, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from sys import argv


# create engine
engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                     .format(argv[1], argv[2], argv[3]), pool_pre_ping=True, echo=True)


Session = sessionmaker(bind=engine)

session = Session()



all_states = session.query(States).all()

for state in all_states:
    print("{}: {}".format(state.id, state.name))












# Base.metadata.create_all(engine)
#
# Write a script that lists all State objects from the database hbtn_0e_6_usa
#
# Your script should take 3 arguments: mysql username, mysql password and database name
# You must use the module SQLAlchemy
# You must import State and Base from model_state - from model_state import Base, State
# Your script should connect to a MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by states.id
# The results must be displayed as they are in the example below
# Your code should not be executed when imported



