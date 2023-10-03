class Shape:
    def __init__(self):
        self.area = 0
        self.name = " "

    def show_area(self):
        print("Area of", self.name, "is", self.area, "units")

class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def calc_area(self):
        self.area = 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.name = "Rectangle"
        self.length = length
        self.breadth = breadth

    def calc_area(self):
        self.area = self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.name = "Triangle"
        self.base = base
        self.height = height

    def calc_area(self):
        self.area = (self.base * self.height) / 2

c1 = Circle(5)
c1.calc_area()
c1.show_area()
r1 = Rectangle(5, 4)
r1.calc_area()
r1.show_area()
t1 = Triangle(3, 2)
t1.calc_area()
t1.show_area()
