class Area:
    def __init__(self, name):
        self.name = name

class Square(Area):
    def __init__(self, name, side_a):
        super().__init__(name)
        self.side_a = side_a
        
    def area(self):
        print(f"Area of {self.name} is {self.side_a**2}")
tr = Square("squere",3)
tr.area()