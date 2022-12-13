# class Area:
#     def __init__(self, area):
#         self.area = area

class Square():
    def __init__(self, side_a):
        self.side_a = side_a

    def area(self):
        print(f"Area of square is {self.side_a**2}")
tr = Square(2)
tr.area()