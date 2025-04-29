class Card:
	def __init__(self, color: str, value: str):
		self.color = color
		self.value  = value

	def equal_colors(self, other):
		return (self.color == other.color or self.color == "wild" or other.color == "wild")
       
	def equal_values(self, other):
		return (self.value == other.value)

	def is_reverse(self):
		return (self.value == "reverse")

	def is_skip(self):
		return self.value == "skip"
	
	def is_plus_four(self):
		return self.value == "+4"
		
	def is_plus_two(self):
		return self.value == "+2"

	def wild_card(self):
		if self.color != "wild": return False
		print("choose your cards color")
		colors = ["red", "yellow", "green", "blue"]
		for i in range(len(colors)):
			print(i, ":", colors[i])
		self.color=colors[int(input(">> "))]
		return True
	def __str__(self):
		return f"{self.color} - {self.value}"