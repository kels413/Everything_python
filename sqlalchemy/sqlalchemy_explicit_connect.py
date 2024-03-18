from sqlalchemy import create_engine,text

# create a connection.
engine = create_engine("sqlite:///sample.db")


# explicit connect
connection = engine.connect()

# execute querry.
test_data = connection.execute(text('SELECT "HELLO" ')).all()

# test output
print(test_data)
