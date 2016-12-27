# sys provides different modules and variables that affect runtime
import sys
import os

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# us this to create our foreign key relationships
from sqlalchemy.orm import relationship
# use in configuration code at the end of the file
from sqlalchemy import create_engine
# will let SQL know that our classes are special sqlalchemy classes corresponding to tables in our db
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

# create instance of create_engine and point to the db we will be using
engine = create_engine('sqlite:///restaurantmenu.db')
# goes into sql and creates new tables as data
Base.metadata.create_all(engine)