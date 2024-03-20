from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True, unique=True)
    customer_name = Column(String(30), nullable=False)
    customer_gender = Column(String(30), nullable=False)

    def __str__(self):
        return f"[{self.customer_name}] <{self.customer_gender}>)"


class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True, unique=True)
    order_name = Column(String(30), nullable=False)
    order_time = Column(String(30), nullable=False)
    order_date = Column(DateTime, default=datetime.now())
    customer_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)

    def __str__(self):
        return f"[<{self.order_name}> ({self.order_time} ({self.order_date} ({self.customer_id}))"
