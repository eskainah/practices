"""
Create a base class Shape with a method calculate_area().
Create a subclass Rectangle that inherits from Shape and 
overrides calculate_area() to calculate the area of a rectangle.
"""

class shape:
    def calculate_area(self):
        pass
    
class Rectangle(shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.length  * self.width
    
    def __repr__(self):
        return f"Rectangle(width={self.width}, length={self.length}, area={self.calculate_area()})"
    
figure1 = Rectangle(4, 8)

print(figure1)