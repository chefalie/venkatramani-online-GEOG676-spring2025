#creating classes for each shape 
class Shape:()
def __init__(self):
    pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def calculateArea(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def calculateArea(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def calculateArea(self):
        return 0.5 * self.base * self.height

#Input file
shape_file = open("C:\\Mac\\Home\\Documents\\GEOG676\\repo\\venkatramani-online-GEOG676-spring2025\\Lab_3\\shape.txt", "r")
lines = shape_file.readlines()
shape_file.close()

for line in lines:
    parameters = line.split(',')
    Shape = parameters[0]
    if Shape == 'Rectangle':
        rect = Rectangle(int(parameters[1]), int(parameters[2]))
        print("Area of Rectangle is:", rect.calculateArea())
    elif Shape == 'Circle':
        circ = Circle(int(parameters[1]))
        print("Area of Circle is:", circ.calculateArea())
    elif Shape == 'Triangle':
        tri = Triangle(int(parameters[1]), int(parameters[2]))
        print("Area of Triangle is", tri.calculateArea())
    else:
        pass
