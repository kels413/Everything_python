from sqlalchemy import create_engine, text
engine = create_engine('mysql://root:31006569@localhost/hbtn_0e_0_usa?charset=utf8mb4', echo=True)
connection = engine.connect()

create_table_query = """
CREATE TABLE IF NOT EXISTS example_table (
    id INT PRIMARY KEY,
    name VARCHAR(255)
)
"""
insert_value = """
    INSERT INTO TABLE IF EXISTS example_table (id,name)VALUES(1, 1),
                                                (2,'stitch'),
                                                (3, 'kee kay), 
                                                (4, 'pas onye ego);
"""


# delete_table = """DROP TABLE example_table
# """
show_states = """
SELECT * FROM states
"""
create_table_sql = text(create_table_query)
insert = text(insert_value)
show_state = text(show_states)

# Execute the SQL command to create the table
connection.execute(create_table_sql)
connection.execute(insert)
result = connection.execute(show_state)


for i in result:
    print(i)

connection.close()

