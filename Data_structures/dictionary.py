# Dictionary

# Q1. Write a program to add a key and value to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
print("--- Question 1: Adding to a Dictionary ---")
my_dict = {0: 10, 1: 20}
print(f"Original dictionary: {my_dict}")
my_dict[2] = 30
print(f"Dictionary after adding a new key-value pair: {my_dict}")
print("-" * 20, "\n")


# Q2. Write a program to concatenate the following dictionaries to create a new one.
# Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("--- Question 2: Concatenating Dictionaries ---")
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
combined_dict = {}
for d in [dic1, dic2, dic3]:
    combined_dict.update(d)
print(f"Dictionary 1: {dic1}")
print(f"Dictionary 2: {dic2}")
print(f"Dictionary 3: {dic3}")
print(f"Combined dictionary: {combined_dict}")
print("-" * 20, "\n")


# Q3. Write a program to check if a given key already exists in a dictionary.
print("--- Question 3: Checking for a Key ---")
sample_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
print(f"Our dictionary: {sample_dict}")
if key_to_check in sample_dict:
    print(f"Yes, the key '{key_to_check}' exists in the dictionary.")
else:
    print(f"No, the key '{key_to_check}' does not exist in the dictionary.")
print("-" * 20, "\n")


# Q4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
print("--- Question 4: Iterating Over a Dictionary ---")
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
print(f"The dictionary is: {fruit_colors}\n")

print("Printing keys:")
for key in fruit_colors.keys():
    print(key)

print("\nPrinting values:")
for value in fruit_colors.values():
    print(value)

print("\nPrinting both keys and values:")
for key, value in fruit_colors.items():
    print(f"{key}: {value}")
print("-" * 20, "\n")


# Q5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
print("--- Question 5: Dictionary of Squares ---")
squares_dict = {}
for number in range(1, 16):
    squares_dict[number] = number * number
print(squares_dict)
print("-" * 20, "\n")


# Q6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
print("--- Question 6: Summing Dictionary Values ---")
item_prices = {'apple': 2, 'banana': 1, 'orange': 3}
total_cost = sum(item_prices.values())
print(f"The dictionary of prices is: {item_prices}")
print(f"The sum of all values is: {total_cost}")
print("-" * 20, "\n")
