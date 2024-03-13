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
"""# User input
pets = []    

# pet 1
pet_name_1 = input("Enter First Pet Name: ")
pet_age_1 = int(input("Enter First Pet Age: "))
pet_color_1 = input("Enter First Pet Color: ")
pets.append({"name": pet_name_1, "age": pet_age_1})

# pet 2
pet_name_2 = input("Enter Second Pet Name: ")
pet_age_2 = int(input("Enter Second Pet Age: "))
pet_color_2 = input("Enter Second Pet Color: ")
pets.append({"name": pet_name_2, "age": pet_age_2})

# pet 3
pet_name_3 = input("Enter Third Pet Name: ")
pet_age_3 = int(input("Enter Third Pet Age: "))
pet_color_3 = input("Enter Third Pet Color: ")
pets.append({"name": pet_name_3, "age": pet_age_3})

# Finding the Oldest and Youngest pet
oldest_pet = max(pets, key=lambda x: x["age"])
youngest_pet = min(pets, key=lambda x: x["age"])

# Print oldest and youngest pet
print(oldest_pet["name"], ", ", "The oldest one is", oldest_pet["age"], "years old")
print(youngest_pet["name"], ", ", "The youngest one is", youngest_pet["age"], "years old")
"""

"""
1. class
2. array/list

"""

class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
class PetList:
    def __init__(self):
        self.pets = []
    
    def add_pet(self, pet):
        self.pets.append(pet)
    
    def age_difference(self):
        oldest_pet = max(self.pets, key=lambda x: x.age)
        youngest_pet = min(self.pets, key=lambda x: x.age)
        return oldest_pet, youngest_pet

pet_lists = PetList()

for i in range(3):
    pet_name = input(f"Enter Pet {i+1} Name: ")
    pet_age = int(input(f"Enter Pet {i+1} Age: "))
    pet_color = input(f"Enter Pet {i+1} Color: ")
    pet = Pet(pet_name, pet_age, pet_color)
    pet_lists.add_pet(pet)

oldest_pet, youngest_pet = pet_lists.age_difference()

print(f"Name: {oldest_pet.name} Color: {oldest_pet.color}, The oldest one is {oldest_pet.age} years old")
print(f"{youngest_pet.name} Color: {youngest_pet.color}, The youngest one is {youngest_pet.age} years old")    
        