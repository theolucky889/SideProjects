"""
Enter pet information and find the oldest and youngest one
- Create a category to store attributes: pet name, age, coat color
- Stored in array
- After user completes input, find the oldest and youngest age
EX = 
Pet name, the oldest one is 12 years old
Pet name, the youngest is 5 years old

How to do:
1. save the names, ages and coat colors of the three pets and print
2. Find the oldest and youngest pet in the array
    """
# User input    
pet_name_1 = str(input("Enter First Pet Name: "))
pet_age_1 = float(input("Enter First Pet Age: "))
pet_color_1 = str(input("Enter First Pet Color: "))


pet_name_2 = str(input("Enter Second Pet Name: "))
pet_age_2 = float(input("Enter Second Pet Age: "))
pet_color_2 = str(input("Enter Second Pet Color: "))

pet_name_3 = str(input("Enter Third Pet Name: "))
pet_age_3 = float(input("Enter Third Pet Age: "))
pet_color_3 = str(input("Enter Third Pet Color: "))

pet_1 = (pet_name_1, pet_age_1, pet_color_1)
pet_2 = (pet_name_2, pet_age_2, pet_color_2)
pet_3 = (pet_name_3, pet_age_3, pet_color_3)

# Finding the Oldest and Youngest pet
oldest_pet = max(pet_age_1, pet_age_2, pet_age_3)
youngest_pet = min(pet_age_1, pet_age_2, pet_age_3)

# Print oldest and youngest pet
