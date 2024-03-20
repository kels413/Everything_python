from model_db import Customers, Orders
from create_db import engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# create session


Session = sessionmaker(bind=engine)
session = Session()


# Insert records into the Customers table
customers_data = [
    Customers(customer_name='John Doe', customer_gender='Male'),
    Customers(customer_name='Jane Smith', customer_gender='Female'),
    Customers(customer_name='Michael Johnson', customer_gender='Male'),
    Customers(customer_name='Emily Davis', customer_gender='Female'),
    Customers(customer_name='Robert Brown', customer_gender='Male')
]
session.add_all(customers_data)
session.commit()

# Insert records into the Orders table
orders_data = [
    Orders(order_name='Laptop', order_time='14:30:00', order_date=datetime.now(), customer_id=1),
    Orders(order_name='Smartphone', order_time='10:45:00', order_date=datetime.now(), customer_id=2),
    Orders(order_name='Headphones', order_time='09:15:00', order_date=datetime.now(), customer_id=3),
    Orders(order_name='Tablet', order_time='12:00:00', order_date=datetime.now(), customer_id=4),
    Orders(order_name='Camera', order_time='16:20:00', order_date=datetime.now(), customer_id=5)
]
session.add_all(orders_data)
session.commit()

# Close the session
session.close()

