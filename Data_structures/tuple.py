#Tuple

# Q1. Write a program to print the 4th element from first and 4th element from last in a tuple.
print("--- Question 1: Accessing Elements in a Tuple ---")
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"The tuple is: {my_tuple}")
fourth_element_from_start = my_tuple[3]
print(f"The 4th element from the start is: {fourth_element_from_start}")
fourth_element_from_end = my_tuple[-4]
print(f"The 4th element from the end is: {fourth_element_from_end}")
print("-" * 20, "\n")


# Q2. Write a program to check whether an element exists in a tuple or not.
print("--- Question 2: Checking for an Element ---")
another_tuple = ('a', 'b', 'c', 'd', 'e')
element_to_find = 'c'
print(f"Our tuple is: {another_tuple}")
if element_to_find in another_tuple:
    print(f"Yes, the element '{element_to_find}' exists in the tuple.")
else:
    print(f"No, the element '{element_to_find}' does not exist in the tuple.")
print("-" * 20, "\n")


# Q3. Write a program to convert a list into a tuple.
print("--- Question 3: Converting a List to a Tuple ---")
my_list = [10, 20, 30, 40, 50]
print(f"The original list is: {my_list}")
converted_tuple = tuple(my_list)
print(f"The converted tuple is: {converted_tuple}")
print("-" * 20, "\n")


# Q4. Write a program to find the index of an item in a tuple.
print("--- Question 4: Finding the Index of an Item ---")
yet_another_tuple = (11, 22, 33, 44, 55, 66)
item_to_find = 44
print(f"The tuple is: {yet_another_tuple}")
index_of_item = yet_another_tuple.index(item_to_find)
print(f"The item '{item_to_find}' is at index: {index_of_item}")
print("-" * 20, "\n")


# Q5. Write a program to replace last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
print("--- Question 5: Replacing Last Value in a List of Tuples ---")
list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(f"Original list of tuples: {list_of_tuples}")
updated_list = [t[:-1] + (100,) for t in list_of_tuples]
print(f"Updated list of tuples: {updated_list}")
print("-" * 20, "\n")
