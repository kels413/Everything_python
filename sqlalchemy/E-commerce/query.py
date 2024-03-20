from model_db import Customers, Orders
from create_db import engine
from sqlalchemy.orm import sessionmaker

# establish session
Session = sessionmaker(bind=engine)

session = Session()

# questions

"""
1. Retrieve the customer_name and order_name of all orders placed by male customers.
"""

male_orders = session.query(Customers, Orders).join(Orders, Customers.customer_id == Orders.customer_id)\
    .filter(Customers.customer_gender == 'Male').all()

print(male_orders)

