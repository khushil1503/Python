#Q.1  A list contains names of boys and girls as its elements. Boys’ names are stored as tuples.
#Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))

names = ["Alice", ("Het",), "Meet", ("Mayur",), "Heer", ("Parv",), "Sophia"]

boys_count = sum(1 for name in names if isinstance(name, tuple))
girls_count = len(names) - boys_count

print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")

#Q.2 A list contains tuples containing roll no., name and age of student.
#Write a python program to create three lists separately for roll no., name and age

students = [(101, "Alice", 20), (102, "Bob", 21), (103, "Charlie", 22), (104, "David", 20)]

roll_nos = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)

#Q.3 Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.

from datetime import date

date1 = (10, 2, 2024)  
date2 = (25, 3, 2024)  

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

days_diff = abs((d2 - d1).days)
print(f"Number of days between {date1} and {date2}: {days_diff}")

#Q.4 Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.

food_items = [("Burger", 150), ("Pizza", 300), ("Pasta", 200), ("Sandwich", 120), ("Salad", 100)]

sorted_food_items = sorted(food_items, key=lambda x: x[1], reverse=True)

print("Food items sorted by price (descending):", sorted_food_items)

#Q.5 Remove empty tuple(s) from the list of tuples.

tuples_list = [(1, 2), (), (3, 4, 5), (), (6,)]

filtered_list = [t for t in tuples_list if t]

print("List after removing empty tuples:", filtered_list)

#Q.6 Modify an element of a tuple.

t = (1, 2, 3, 4)
temp_list = list(t)
temp_list[1] = 99  # Modifying the second element
t = tuple(temp_list)

print("Modified tuple:", t)

#Q.7 Delete an element of a tuple.

t = (1, 2, 3, 4, 5)
temp_list = list(t)
del temp_list[2]  # Deleting the element at index 2 (value 3)
t = tuple(temp_list)

print("Tuple after deletion:", t)

#EXTRA. What will be the output of the following code?
#1) lst = [ (‘X’, ‘Y’, ‘Z’), 40, 50 , 60]
#a = lst[0]
#print (a)
#a) X b) 0 c) (x, y, z) d) (‘x’, ‘y’, ‘z’)

The list `lst = [('X', 'Y', 'Z'), 40, 50, 60]` contains a tuple as the first element. When we do `a = lst[0]`, we are assigning the entire first element, which is the tuple `('X', 'Y', 'Z')`, to `a`.

Thus, the output of `print(a)` will be:

**d) ('X', 'Y', 'Z')**






