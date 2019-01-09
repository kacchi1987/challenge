class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square:
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

rectangle = Rectangle(10, 20)
print(rectangle.calculate_perimeter())

square = Square(10)
print(square.calculate_perimeter())
