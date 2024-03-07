# Part 2


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(a, b):
        return Vector(a.x + b.x, a.y + b.y)
    
    def __sub__(a, b):
        return Vector(a.x - b.x, a.y - b.y)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y   # dot product
    
    def scalar_mult(self, scalar):
        return Vector(self.x * scalar, self.y * scalar) # scalar
        
    def scalar_div(self, scalar):
        if scalar == 0:
            print("Division by zero")
        else:
            return Vector(self.x / scalar, self.y / scalar)
    
    def __repr__(self):
        return f"[{self.x}, {self.y}]"

def get_user_vector():
    x = float(input("Input x-coordinate: "))
    y = float(input("Input y-coordinate: "))
    return Vector(x, y)
    
def main():
    print("Enter coordinates for vector A: ")
    A = get_user_vector()
    
    print("Enter coordinates for vector B: ")
    B = get_user_vector()
    
    print("A + B = ", A + B)
    print("A - B = ", A - B)
    
    # dot product of the vector
    print("A * B = ", A.dot_product(B))
    
    # scalar product of the vector
    scalar = float(input("Enter scalar for multiplication and division: "))
    print("A * scalar = ", A.scalar_mult(scalar))
    print("A / scalar = ", A.scalar_div(scalar))
    
    
if __name__ == "__main__":
    main()