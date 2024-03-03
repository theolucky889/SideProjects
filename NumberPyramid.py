"""
    1
   1 1
  1 2 1
 1 3 3 1
    """
#Pascal Triangle ^^^

def pascal_triangle(rows):

    for i in range(rows):
        n = 1
        for j in range(i + 1):
            print(n, end=" ")
            n = n * (i - j) // (j + 1)
        print()

pascal_triangle(4)