from decimal import Decimal
from django.conf import settings
from food.models import Food

class Cart(object):
	def __init__(self, request):
		"""
		Initialize the cart.
		"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# save an empty cart in the session
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def __len__(self):
		"""
		Count all items in the cart.
		"""
		return sum(item['quantity'] for item in self.cart.values())

	def __iter__(self):
		"""
		Iterate over the items in the cart and get the books from the database.
		"""
		food_ids = self.cart.keys()
		# get the book objects and add them to the cart
		foods = Food.objects.filter(id__in = food_ids)
		for food in foods:
			self.cart[str(book.id)]['book'] = book
			for item in self.cart.values():
				item['price'] = Decimal(item['price'])
				item['total_price'] = item['price'] * item['quantity']
				yield item

	def add(self, book, quantity=1, update_quantity=False):
		"""
		Add a book to the cart or update its quantity.
		"""
		food_id = str(book.id)
		if food_id not in self.cart:
			self.cart[food_id] = {'quantity': 0,'price': str(food.price)}
			if update_quantity:
				self.cart[food_id]['quantity'] = quantity
			else:
				self.cart[food_id]['quantity'] += quantity
		self.save()

	def remove(self, book):
		"""
		Remove a book from the cart.
		"""
		food_id = str(food.id)
		if food_id in self.cart:
			del self.cart[food_id]
			self.save()

	def save(self):
		# update the session cart
		self.session[settings.CART_SESSION_ID] = self.cart
		# mark the session as "modified" to make sure it is saved
		self.session.modified = True

	def clear(self):
		# empty cart
		self.session[settings.CART_SESSION_ID] = {}
		self.session.modified = True

	def add_from_recipe(self):
		return 5

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
