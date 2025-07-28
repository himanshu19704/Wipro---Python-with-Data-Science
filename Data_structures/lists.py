#List

# Q1. Make a list of 5 whole numbers and show it. Then, show a few items from the list using their position (index).
print("--- Question 1: Creating and Accessing a List ---")
my_numbers = [10, 20, 30, 40, 50]
print(f"Here is the full list: {my_numbers}")
first_item = my_numbers[0]
print(f"The first item (at index 0) is: {first_item}")
third_item = my_numbers[2]
print(f"The third item (at index 2) is: {third_item}")
print("-" * 20, "\n")


# Q2. Add a new number to the end of our list.
print("--- Question 2: Appending to a List ---")
print(f"The list before adding anything was: {my_numbers}")
my_numbers.append(60)
print(f"Now the list is: {my_numbers}")
print("-" * 20, "\n")


# Q3. Flip the order of the list.
print("--- Question 3: Reversing a List ---")
print(f"Our list right now is: {my_numbers}")
my_numbers.reverse()
print(f"After reversing it, the list is: {my_numbers}")
print("-" * 20, "\n")


# Q4. In a new list, count how many times a specific number shows up.
print("--- Question 4: Counting Occurrences ---")
another_list = [1, 4, 2, 6, 4, 7, 4]
number_to_find = 4
print(f"We have a new list: {another_list}")
times_found = another_list.count(number_to_find)
print(f"The number {number_to_find} appears {times_found} times in the list.")
print("-" * 20, "\n")


# Q5. Take two lists and join them, with the first list's items at the beginning.
print("--- Question 5: Combining two Lists ---")
list_one = [1, 2, 3]
list_two = [4, 5, 6]
print(f"Here is the first list: {list_one}")
print(f"And the second list: {list_two}")
new_combined_list = list_one + list_two
print(f"When we join them, we get: {new_combined_list}")
print("-" * 20, "\n")


# Q6. Insert a new number right before the second item in a list.
print("--- Question 6: Inserting an Item ---")
some_list = [10, 30, 40]
print(f"Let's start with this list: {some_list}")
some_list.insert(1, 20)
print(f"After inserting 20, the list becomes: {some_list}")
print("-" * 20, "\n")


# Q7. Remove an item from a list using its position (index).
print("--- Question 7: Removing by Index ---")
a_list_to_edit = [11, 22, 33, 44, 55]
print(f"Here's our list: {a_list_to_edit}")
removed_value = a_list_to_edit.pop(2)
print(f"We just removed the value: {removed_value}")
print(f"The list now looks like this: {a_list_to_edit}")
print("-" * 20, "\n")


# Q8. Remove the first matching item from a list.
print("--- Question 8: Removing by Value ---")
list_with_a_duplicate = [5, 15, 25, 15, 35]
value_to_remove = 15
print(f"Our list is: {list_with_a_duplicate}")
list_with_a_duplicate.remove(value_to_remove)
print(f"After removing it, the list is: {list_with_a_duplicate}")
print("-" * 20, "\n")
