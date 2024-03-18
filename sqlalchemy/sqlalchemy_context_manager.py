from sqlalchemy import create_engine, text

# database+driver://username:password@host:port/db
engine = create_engine("sqlite:///sample_db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('SELECT "HELLO world"'))
    print(result.all())

