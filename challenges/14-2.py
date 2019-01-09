class Square:
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append(self.len)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)

SQ1 = Square(29)

print(SQ1)
