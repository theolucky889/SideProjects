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
    
class Rectangle:
    def __init__(self, width=0.0, length=0.0):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
    
class RectangleVolume:
    def __init__(self, width=0.0, length=0.0, height=0.0):
        super().__init__(width, length)
        self.height = height
        
    def surface(self):
        return 2 * (self.width * self.length + self.height * self.length + self.height * self.width)     # A=2(wl+hl+hw)
        
    def volume(self):
        return self.width * self.height * self.length     # V=whl
        
    def main():
        width = float(input("Input the width of the rectanglular prism:　"))
        length = float(input("Input the length of the rectanglular prism:　"))
        height = float(input("Input the height of the rectanglular prism:　"))
    
    