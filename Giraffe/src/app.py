# color = input("Please enter a color: ")
# plural_noun = input("Please enter a plural noun: ")
# celebrity = input("Please enter a celebrity name: ")
import datetime
import math
import string


# f-strings

# print(f"Roses are red {color}")
# print(f"{plural_noun} are blue")
# print(f"I love {celebrity}")

# Lists
# *****
# friends = ["Arun", "Vishnu", "Kevin", "Kiran"]
#
# print(friends[0])
# print(friends[-1])
# print(friends[1:])
# print(friends[1:3])

# List Functions
# **************
# lucky_numbers = [42, 8, 15, 16, 23, 4]

# friends.extend(["Coral", "Roberto", "David"])
# friends.append("Monty")
# friends.insert(0, "Subhash")
# print(friends)
#
# friends.remove("David")  # removes "David" from the list.
# print(friends)
# friends.pop(0)  # removes item at index 0 from the list. friends.pop() removes the last item in the list.
# print(friends)
#
# print(friends.index("Kevin"))
#
# print(friends.count("Kevin"))  # Returns the number of occurrences of the given item in the list.
#
# friends.sort()
# print(friends)
#
# lucky_numbers.sort()
# print(lucky_numbers)  # [4, 8, 15, 16, 23, 42]
#
# lucky_numbers.reverse()
# print(lucky_numbers)  # [42, 23, 16, 15, 8, 4]
#
# friends_copy = friends.copy()
# print(friends_copy)

# Tuples
# ******
# coordinate = (4, 5)
# coordinates = [(0, 0), (3, 2), (4, 10)]
# print(coordinates)
# print(coordinates[1])

# Function
# ********
# def say_hi(name):
#     print(f"Hi {name}")
#
#
# say_hi("Deon")
#
#
# def add_num(num1, num2):
#     sum_of_numbers = num1 + num2
#     return sum_of_numbers
#
#
# print(add_num(265, 43))
#
#
# def cube(num):
#     return num * num * num
#
#
# print(cube(4))


# Conditional Statements (if, if-else, elif)
# ******************************************
# is_over_18 = True
# is_male = True
#
# if is_over_18 and is_male:
#     print("You are a guy over 18.")
# elif is_over_18:
#     print("You are over 18.")
# elif is_male:
#     print("You are a guy.")
# else:
#     print("You are either not a guy or you are under 18.")
#
# if is_over_18 or is_male:
#     print("You are either a guy or you are over 18.")
# else:
#     print("You are neither a guy nor you are over 18.")
#
# if not is_male:
#     print("You are a female.")

# Calculates the maximum of the 3 given numbers.
# def get_max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print(get_max(21, 111, 3))

# Advanced Calculator
# def calculate(num_one, num_two, op):
#     if op == "+":
#         print(num_one + num_two)
#     elif op == "-":
#         print(num_one - num_two)
#     elif op == "*":
#         print(num_one * num_two)
#     elif op == "/":
#         print(num_one / num_two)
#     else:
#         print("Invalid operation")
#
#
# num1 = float(input("Enter number 1: "))
# operation = input("Enter operation: ")
# num2 = float(input("Enter number 2: "))
#
# calculate(num1, num2, operation)


# Dictionaries
# ************
# months = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
#
# print(months)
# print(months["Oct"])
# print(months.get("Sep"))
#
# # Second parameter is the default/fallback value that will be returned
# # if the item with the given key doesn't exist.
# print(months.get("Aad", "Not a valid key"))


# while loops
# ***********
# count = 0
#
# while count < 5:
#     stars = 0
#
#     while stars < count + 1:
#         print("*", end='')  # end='' prevents addition of a line-break after printing '*'
#         stars += 1
#
#     print("\r")
#     count += 1


# Guessing Game
# *************
# secret_word = "Orange"
# guess_count = 0
# GUESS_LIMIT = 3
#
# while guess_count < GUESS_LIMIT:
#     guess = input("Please enter a string: ")
#
#     if guess.strip().lower() == secret_word.lower():
#         print(f"You guessed the secret word correctly. You win 🎉🎉🎉.")
#         break
#
#     guess_count += 1
#     if guess_count == GUESS_LIMIT:
#         print("You are out of guesses 😥😥😥.")
#     else:
#         print(f"You have only {GUESS_LIMIT - guess_count} guesses left 🤔🤔🤔.")


# for loops
# *********
# friends = ['Arun', 'Vishnu', 'John', 'Coral', 'Roberto']
#
# # Prints all friend's name in separate line.
# print("\nWithout using index:")
# for friend in friends:
#     print(friend)
#
# # Another method to print all friend's name in separate line.
# print("\nUsing index:")
# for index in range(len(friends)):
#     print(friends[index])
#
# # Prints out each letter in the name Arun.
# print(f"\nIndividual letters in the name {friends[0]}:")
# for letter in friends[0]:
#     print(letter)
#
# # Print numbers from 1 to 10.
# print(f"\nNumbers from 1 to 10:")
# for num in range(1, 11):
#     print(num)


# Exponent function
# *****************
# def exponent(base, power):
#     result = 1
#     for times in range(power):
#         result *= base
#     return result
#
#
# print(exponent(3, 4))


# Lists and Nested Loops
# **********************
# Nested list
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10]
# ]
#
# print(number_grid[0][1])  # Prints 2.
# print(number_grid[3][0])  # Prints 10.
#
# # Nested for loop
# print("\nDisplaying all values in the nested list:")
# for row in number_grid:
#     for num in row:
#         print(num, end='\t')
#     print('\r')


# Building a translator
# *********************
# Rule: All vowels should be translated to 'g'
def translate(input_sentence):
    translation = ""

    for letter in input_sentence:
        if letter in "aeiouAEIOU":
            translation += "G" if letter.isupper() else "g"  # Ternary expression.
        else:
            translation += letter

    return translation


print(f"dog => {translate('dog')}")
print(f"rhythm => {translate('rhythm')}")
print(f"aeroplane => {translate('aeroplane')}")
print(f"Orbit => {translate("Orbit")}")
