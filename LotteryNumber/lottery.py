# Power Lotto Lottery Number generator
"""
Generate power lotto numbers

Choose any 6 numbers from the numbers 01 to 38 in the first zone
and choose 1 number from the numbers 01 to 08 in the second zone

Loop to generate a complete set of random lottery numbers
"""

import random       # Generate random numbers

# Range of numbers in each area
area1_numbers = list(range(1, 38))
area2_numbers = list(range(1, 8))

# Select the numbers from each area
select_area1_numbers = random.sample(area1_numbers, 6)     # 6 because we need to select 6 numbers randomly
select_area2_numbers = random.choice(area2_numbers)        # no number because we need to select just 1 number

print("Area 1: ", select_area1_numbers)
print("Area 2: ", select_area2_numbers)