from dataclasses import dataclass

@dataclass
class Rectangle:
	lower_x: int
	lower_y: int
	upper_x: int
	upper_y: int
	
	def __hash__(self):
		return hash((self.lower_x, self.lower_y, self.upper_x, self.upper_y))
	
	def __str__(self):
		return "{}, {}, {}, {}".format(self.lower_x, self.lower_y, self.upper_x, self.upper_y)