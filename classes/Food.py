class Food(object):

	
	count = 5000;

	def __init__(self, meal_type, name, amount, calories):
		self.food_id = Food.count;
		self.meal_type = meal_type;
		self.name = name;
		self.amount = amount;
		self.calories = calories;
		Food.count += 1;
	