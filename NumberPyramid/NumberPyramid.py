"""
    1       a
   1 1      b
  1 2 1     c
 1 3 3 1    d
    """
#Pascal Triangle ^^^

"""
times=25
>>>>>>> 97385dd0de713493344d70c69457764d5d7a4259

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
""""
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
"""




def generate_triangle(num_rows):
    triangle = [["01"]]
    for i in range(1, num_rows):
        initial = ["01"]
        for j in range(1, i):
            new_row = int(triangle[i - 1][j - 1]) + int(triangle[i - 1][j])
            initial.append(str(new_row).zfill(2))
        initial.append("01")
        triangle.append(initial)
    return triangle

def print_triangle(triangle):
    max_length = len(max(triangle[-1], key=len))    # Check for the biggest number at the bottom of the triangle
    max_width = len(" ".join([num.zfill(max_length)for num in triangle[-1]]))  # placing triangle and adding 0's according to the biggest number at the bottom of the triangle
    for row in triangle:
        print(" ".join(num.zfill(max_length) for num in row).center(max_width))
num_rows = int(input("Enter the number of rows in the Pascal Triangle: "))
pascal_triangle = generate_triangle(num_rows)
print_triangle(pascal_triangle)