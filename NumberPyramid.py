"""
    1
   1 1
  1 2 1
 1 3 3 1
    """
#Pascal Triangle ^^^


for i in range(4):
    n = 1                           # initial number in the triangle
    for j in range(i + 1):          # Loop for triangle
        print(n, end=" ")           # Spacing between numbers
        n = n * (i - j) // (j + 1)  # Simplified Pascal triangle formula (n k) = n!/k!-(n-k)!
    print()

pascal_triangle(4)



"""
Pascal triangle formula = (n k) = n!/k!-(n-k)!
(n k ) = n(n-1)*(n-2)...(n-k+1) / k(k-1)*(k-2)...1

    """