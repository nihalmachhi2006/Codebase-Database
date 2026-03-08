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


# def sayhello ( name):
#     print("hello", name)


# sayhello(name="nihal")

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
# print("Final count of Positive number is: ", positive_number_count)


# n = 10

# sum_even = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         sum_even += 1

# print(sum_even)



# n = 3

# for i in range(1,11):
#     if i==5:
#         continue
#     print(n, 'x', i, '=', n*i)


# input_str = "Nihal"

# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str 

# print(reversed_str)


## second methond -
# input_str = "Nihal"
# print(input_str[::-1])


# input_str = "NiihalNihal2"

# for char in input_str:
#     if input_str.count(char) == 1:
#         print(char)
#         break

# n = 5

# fact = 1

# while n > 0:
#     fact = fact * n
#     n = n-1

# print(fact)


# while True:
#     n = int(input("Enter Value b/w 1 & 10 "))
#     if 1<= n <=10:
#         print("thx")
#         break
#     else:
#         print("error try again")

# n=28
# isprime = True

# if n > 1:
#     for i in range(2,n):
#         if (n % i) == 0:
#             isprime = False
#             break

# print(isprime)


# items = ["apple", "banana", "orange", "apple", "mango"]

# uitem = set()

# for item in items:
#     if item in uitem:
#         print(item)
#         break
#     uitem.add(item)


# import time

# wtime = 1
# mtry = 5
# att = 0

# while att < mtry:
#     print("Attempt", att, +1, "wait time",wtime)
#     time.sleep(wtime)
#     wtime += 2
#     att += 1



# def square(n):
#     return(n ** 2)


# result = square(5)

# print(result)

# def add(n,m):
#     return n+m

# print(add(4,5))


# def muti(p1,p2):
#     return p1 * p2

# print(muti(5,6))


# import math

# def cstatus(readius):
#     area =  math.pi * readius ** 2

#     circum = 2 * math.pi * readius
    
#     return area,circum

# a,c = cstatus(3)
# print(a,c)

# cude = lambda x: x ** 3

# print(cude(3))


# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#     return sum(args)

# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))

