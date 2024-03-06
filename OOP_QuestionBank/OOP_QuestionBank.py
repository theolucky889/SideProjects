"""

1. Use the inheritance method to calculate the surface area and volume of the cuboid.
- First construct the rectangle (Rectangle) category, which contains member variables 
  double width, double length, rectangle constructors Rectangle( ), Rectangle(double, double) 
  and member function Area(double, double).
  
- Construct the class RectangleVolume (cuboid) class by inheriting the 
  rectangle (Rectangle) class, which contains the member variable double height and the 
  constructor RectangleVolume( ), RectangleVolume(double, double, double), 
  member function surface area Surface(double, double, double) and 
  volume Volume(double, double, double).
  
- In the main program main(), declare the variable RectangleVolume A, and after reading in the 
  height, width, and length respectively, calculate the surface area and volume of the cuboid.

2. Use operator overload (overload) method to execute vectors +, -, * and /, 
which are defined as follows:
For example:
A = [a1, a2], B = [b1, b2]
A + B = [a1 + b1, a2 + b2]
A - B = [a1 - b1, a2 - b2]
A * B = [a1 * b1, a2 * b2]
A / B = [a1 / b1, a2 / b2]

    """
    # Part 1
class Rectangle:
    def __init__(self, width=0.0, length=0.0):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
    
class RectangleVolume(Rectangle):
    def __init__(self, width=0.0, length=0.0, height=0.0):
        Rectangle.__init__(self, width, length)
        
        self.height = height
        
    def surface(self):
        return 2 * (self.width * self.length + self.height * self.length + self.height * self.width)     # A=2(wl+hl+hw)
        
    def volume(self):
        return self.width * self.height * self.length     # V=whl
        
def main():
    width = float(input("Input the width of the rectanglular prism: "))
    length = float(input("Input the length of the rectanglular prism: "))
    height = float(input("Input the height of the rectanglular prism: "))
    
    A = RectangleVolume(width, length, height)

    surface_area = A.surface()
    cube_volume = A.volume()

    print("Surface area of the Rectangular Prism is: ", surface_area)
    print("Volume of the Rectangular Prism is: ", cube_volume)
    
if __name__ == "__main__":
    main()
    
    
# Part 2

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mult__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __div__(self, other):
        return Vector(self.x / other.x, self.y / other.y)
    
    def __userinput__():
        x = input("Input coordinates for x: ")
        y = input("Input coordinates for y: ")
        return Vector(x, y)
    
    def __repr__(self):
        return f"[{self.x}, {self.y}]"