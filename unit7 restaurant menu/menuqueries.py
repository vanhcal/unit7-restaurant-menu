from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker (bind = engine)
session = DBSession()

def create_first_restaurant():
	myFirstRestaurant = Restaurant (name = "Pizza Palace")
	session.add(myFirstRestaurant)
	session.commit()

def get_first_restaurant():
	session.query(Restaurant).all()
	firstResult = session.query(Restaurant).first()
	firstResult.name

def add_item():
	cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
	session.add(cheesepizza)
	session.commit()

def get_all_items():
	items = session.query(MenuItem).all()
	for item in items:
		print item.name

def get_all_veggie_burgers():
	veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
	for veggieBurger in veggieBurgers:
		print veggieBurger.id
		print veggieBurger.price
		print veggieBurger.restaurant.name
		print "/n"

def get_burger_price()
	UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 8).one()
	print UrbanVeggieBurger.price

def change_item_price():
	UrbanVeggieBurger.price = '2.99'
	session.add(UrbanVeggieBurger)
	session.commit()

def change_all_items_price():
	for veggieBurger in veggieBurgers:
		if veggieBurger.price != '$2.99':
			veggieBurger.price = '2.99'
			session.add(veggieBurger)
			session.commit()

def delete_item():
	spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
	session.delete(spinach)
	session.commit()
