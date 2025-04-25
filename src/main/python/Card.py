class Card:
        def __init__(self, color: str, value: str):
                self.color = color
                self.value  = value

        def equal_colors(self, other):
                return (self.color == other.color or self.color == "wild" or other.color == "wild")
       
        def equal_values(self, other):
                return (self.value == other.value)

        def __str__(self):
                return f"{self.color} - {self.value}"