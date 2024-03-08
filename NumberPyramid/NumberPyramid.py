"""
    1
   1 1
  1 2 1
 1 3 3 1
    """
#Pascal Triangle ^^^

times=5

for i in range(times):
    n = 1                           # initial number in the triangle
    for _ in range(times - i):          # Space before the number
        print(" ", end="")
    for j in range(i + 1):          # Loop for triangle
        print(n, end=" ")           # Spacing between numbers
        n = n * (i - j) // (j + 1)  # Simplified Pascal triangle formula (n k) = n!/k!-(n-k)!
    print()





"""
Pascal triangle formula = (n k) = n!/k!-(n-k)!
(n k ) = n(n-1)*(n-2)...(n-k+1) / k(k-1)*(k-2)...1

1. output
2. spacing
3. function(15 line limit)
    """