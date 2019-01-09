class Square:
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append(self.len)

SQ1 = Square(10)
SQ2 = Square(20)

print(Square.square_list)
