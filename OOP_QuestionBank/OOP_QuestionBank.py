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
    def __init__(rectangle, width=0.0, length=0.0):
        rectangle.width = width
        rectangle.length = length
    def area(rectangle):
        return rectangle.width * rectangle.length