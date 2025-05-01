#EXAMPLE 

# Creating a set of 10 elements that are multiples of 5
my_set = {5 * i for i in range(1, 11)}

# Remove the 5th element (in this case, it's the element with value 25)
# Since sets are unordered, we need to convert it to a list to access the 5th element.
my_set_list = list(my_set)
my_set.remove(my_set_list[4])

# Get the highest and smallest value in the set
highest_value = max(my_set)
smallest_value = min(my_set)

# Add 33 to the set
my_set.add(33)

# Display the results
print(f"Updated set: {my_set}")
print(f"Highest value: {highest_value}")
print(f"Smallest value: {smallest_value}")

#Q.1 Write a program that converts words present in a list into uppercase and stores them in a set.

# List of words
words_list = ["hello", "world", "python", "programming"]

# Convert words to uppercase and store in a set
words_set = {word.upper() for word in words_list}

# Display the result
print(words_set)

#Q.2 Write a program to create a set containing 10 random numbers in the range 15 to 45.
#Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.

import random

# Generate a set of 10 random numbers between 15 and 45
random_numbers = {random.randint(15, 45) for _ in range(10)}

# Count how many numbers are less than 30
count_less_than_30 = sum(1 for num in random_numbers if num < 30)

# Delete numbers greater than 35
random_numbers = {num for num in random_numbers if num <= 35}

# Display the results
print("Random numbers:", random_numbers)
print("Count of numbers less than 30:", count_less_than_30)

#Q.3 Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.

# Create an empty set
names_set = set()

# Add five new names to the set
names_set.add("Alice")
names_set.add("Bob")
names_set.add("Charlie")
names_set.add("David")
names_set.add("Eva")

# Modify one existing name (we'll remove "Bob" and add "Robert" instead)
names_set.remove("Bob")  # Removing "Bob"
names_set.add("Robert")  # Adding "Robert"

# Delete two names from the set
names_set.remove("Charlie")
names_set.remove("Eva")

# Display the resulting set
print("Updated set of names:", names_set)

#Q.4 A set contains names which begin either with A or with B.
#Write a program to separate out the names into two sets, one containing names beginning with A and another with B.

# Set containing names
names_set = {"Alice", "Bob", "Andrew", "Benjamin", "Charlie", "Barbara", "Adam"}

# Create two empty sets for names starting with 'A' and 'B'
names_with_A = set()
names_with_B = set()

# Loop through the names and separate them into appropriate sets
for name in names_set:
    if name.startswith('A'):
        names_with_A.add(name)
    elif name.startswith('B'):
        names_with_B.add(name)

# Display the results
print("Names starting with A:", names_with_A)
print("Names starting with B:", names_with_B)

