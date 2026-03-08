# print("hello Nihal")

# def hello(n):
#     print(n)

# # hello(5)


# hello_one = "Good Morning"
# hello_second = "Good night"



# name = input("Enter you name ")
# print(name)
# print(type(name))

# user = int(input("Enter your age "))

# if user < 13:
#     print("Child")
# elif user < 20:
#     print("Adult")
# else:
#     print("Senior")

# age = 25
# day = "Sat"

# price = 12 if age  >= 18 else 8

# if day == "Sat":
#     # price = price - 2
#     price -= 2

# print("Prices is you", price)


# score = 95

# if score >= 101:
#     print("Please verify your grade again")
#     exit()

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("Grade: ", grade)


# fruit = "apple"
# color = "green"

# if fruit == "apple":
#     if color == "green":
#         print("wait")
#     elif color == "red":
#         print("eat")
#     else:
#         print("throww")



# year = 2028

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print( year, " is a leap year")
# else:
#     print(year, "is NOT a leap year")



# Problem: Recommend a type of pet food based on the pet's species and age. 
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# def recommend_pet_food(species, age):
#     species = species.lower()

#     if species == "dog":
#         if age < 2:
#             return "Puppy food"
#         elif 2 <= age <= 7:
#             return "Adult dog food"
#         else:
#             return "Senior dog food"

#     elif species == "cat":
#         if age < 1:
#             return "Kitten food"
#         elif 1 <= age <= 7:
#             return "Adult cat food"
#         else:
#             return "Senior cat food"

#     else:
#         return "Species not supported"


# # Example usage
# species = input("Enter pet species (Dog/Cat): ")
# age = float(input("Enter pet age in years: "))

# food = recommend_pet_food(species, age)
# print("Recommended food:", food)
