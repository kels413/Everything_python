from model_db import Base
from sqlalchemy import create_engine

db_uri = "mysql+mysqldb://root:31006569@localhost:3306/kelly_test"
engine = create_engine(db_uri, pool_pre_ping=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)





