from sqlalchemy import create_engine, text
engine = create_engine('mysql://root:31006569@localhost/hbtn_0e_0_usa?charset=utf8mb4', echo=True)
connection = engine.connect()

create_table_query = """
CREATE TABLE IF NOT EXISTS example_table (
    id INT PRIMARY KEY,
    name VARCHAR(255)
)
"""

delete_table = """DROP TABLE example_table
"""
show_states = """
SELECT * FROM states
"""
create_table_sql = text(create_table_query)
del_table = text(delete_table)
show_state = text(show_states)

# Execute the SQL command to create the table
connection.execute(create_table_sql)
connection.execute(del_table)
result = connection.execute(show_state)


for i in result:
    print(i)

connection.close()

