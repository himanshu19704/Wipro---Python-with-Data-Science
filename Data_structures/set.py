#Set

# Q1. Write a program to remove a given item from the set.
print("--- Question 1: Removing an Item from a Set ---")
my_set = {1, 2, 3, 4, 5}
item_to_remove = 3
print(f"Original set: {my_set}")
my_set.remove(item_to_remove)
print(f"Set after removing {item_to_remove}: {my_set}")
print("-" * 20, "\n")


# Q2. Write a program to create an intersection of sets.
print("--- Question 2: Intersection of Sets ---")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")
print("-" * 20, "\n")


# Q3. Write a program to create an union of sets.
print("--- Question 3: Union of Sets ---")
setA = {'a', 'b', 'c'}
setB = {'c', 'd', 'e'}
print(f"Set A: {setA}")
print(f"Set B: {setB}")
union_set = setA.union(setB)
print(f"Union: {union_set}")
print("-" * 20, "\n")


# Q4. Write a program to find the maximum and minimum value in a set.
print("--- Question 4: Max and Min in a Set ---")
number_set = {15, 8, 23, 4, 42, 16}
print(f"The set is: {number_set}")
max_value = max(number_set)
min_value = min(number_set)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print("-" * 20, "\n")
