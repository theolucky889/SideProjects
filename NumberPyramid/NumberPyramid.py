"""
    1       a
   1 1      b
  1 2 1     c
 1 3 3 1    d
    """
#Pascal Triangle ^^^
"""
times=25

for i in range(times):
    n = 1                           # initial number in the triangle
    for _ in range(times - i):          # Space before the number
        print(" ", end="")
    for j in range(i + 1):          # Loop for triangle
        print(n, end=" ")           # Spacing between numbers
        n = n * (i - j) // (j + 1)  # Simplified Pascal triangle formula (n k) = n!/k!-(n-k)!
    print()
"""




"""
Pascal triangle formula = (n k) = n!/k!-(n-k)!
(n k ) = n(n-1)*(n-2)...(n-k+1) / k(k-1)*(k-2)...1

1. output
2. spacing
3. function(15 line limit)
    """

a1 = "1"

b1 = "1"
b2 = "1"

c1 = "1"
c2 = "2"
c3 = "1"

d1 = "1"
d2 = "3"
d3 = "3"
d4 = "1"

    
a = " " + a1 + "\n"
b = " " + b1 + " " + b2 + "\n"
c = " " + c1 + " " + c2 + " " + c3 + "\n"
d = " " + d1 + " " + d2 + " " + d3 + " " + d4 + "\n"

print ("".join(a+b+c+d))

def generate_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        initial = [1]
        if i > 0:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                initial.append(prev_row[j] + prev_row[j + 1])
            initial.append(1)
        triangle.append(initial)
    return triangle

def print_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))
    triangle_center = ("\n".join(" ".join(map(str, row)).center(max_width) for row in triangle))
    return triangle_center    
        #print(" ".join(map(str, row)).center(len(triangle[-1])))
num_rows = int(input("Enter the number of rows in the Pascal Triangle: "))
pascal_triangle = generate_triangle(num_rows)
triangle_output = print_triangle(pascal_triangle)
print(triangle_output)
