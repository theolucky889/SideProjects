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
    
    def __repr__(self):
        return f"[{self.x}, {self.y}]"

def get_user_vector():
    x = input("Input x-coordinate: ")
    y = input("Input y-coordinate: ")
    return Vector(x, y)
    
def main():
    print("Enter coordinates for vector A: ")
    A = get_user_vector()
    
    print("Enter coordinates for vector B: ")
    B = get_user_vector()
    
    print("A + B = ", A + B) 
    print("A - B = ", A - B)
    print("A * B = ", A * B)
    print("A / B = ", A / B)
    
if __name__ == "__main__":
    main()