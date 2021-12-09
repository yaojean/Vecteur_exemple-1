from math import sqrt

class vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def norme(self):
		return sqrt(self.x**2 + self.y**2) 


