class Area:
    def __init__(self, name):
        self.name = name

class Square(Area):
    def __init__(self, name, side_a):
        super().__init__(name)
        self.side_a = side_a
        
    def area(self):
        print(f"Area of {self.name} is {self.side_a**2}")

class Rectangle(Square):
    def __init__(self, name, side_a, side_b):
        super().__init__(name, side_a)
        self.side_b = side_b

    def area(self):
        print(f"Area of {self.name} is {self.side_a*self.side_b}")

class Circle(Area):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        print(f"Area of {self.name} is {3.14*self.radius**2}")


    
square = Square("squere",3)
square.area()
rectangle = Rectangle("rectangle",3, 4)
rectangle.area()
circle = Circle("circle",10)
circle.area()
