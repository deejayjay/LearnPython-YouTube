# color = input("Please enter a color: ")
# plural_noun = input("Please enter a plural noun: ")
# celebrity = input("Please enter a celebrity name: ")

# f-strings

# print(f"Roses are red {color}")
# print(f"{plural_noun} are blue")
# print(f"I love {celebrity}")

# Lists
# *****
friends = ["Arun", "Vishnu", "Kevin", "Kiran"]

print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

# List Functions
# **************
lucky_numbers = [42, 8, 15, 16, 23, 4]

friends.extend(["Coral", "Roberto", "David"])
friends.append("Monty")
friends.insert(0, "Subhash")
print(friends)

friends.remove("David")  # removes "David" from the list.
print(friends)
friends.pop(0)  # removes item at index 0 from the list. friends.pop() removes the last item in the list.
print(friends)

print(friends.index("Kevin"))

print(friends.count("Kevin"))  # Returns the number of occurrences of the given item in the list.

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)  # [4, 8, 15, 16, 23, 42]

lucky_numbers.reverse()
print(lucky_numbers)  # [42, 23, 16, 15, 8, 4]

friends_copy = friends.copy()
print(friends_copy)
