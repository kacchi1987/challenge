class Shape:
    def __init__(self, w, h):
        self.width= w
        self.height = h

    def what_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

rectangle = Rectangle(10, 30)
print(rectangle.what_am_i())

square = Square(10, 10)
print(square.what_am_i())
