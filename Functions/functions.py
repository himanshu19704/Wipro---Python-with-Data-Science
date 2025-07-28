# Q1. Write a function to return the sum of all numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
print("--- Question 1: Sum of Numbers in a List ---")
def sum_list(numbers):
    return sum(numbers)

sample_list = [8, 2, 3, 0, 7]
total = sum_list(sample_list)
print(f"The sum of {sample_list} is: {total}")
print("-" * 20, "\n")


# Q2. Write a function to return the reverse of a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
print("--- Question 2: Reverse a String ---")
def reverse_string(s):
    return s[::-1]

sample_string = "1234abcd"
reversed_str = reverse_string(sample_string)
print(f"The reverse of '{sample_string}' is '{reversed_str}'")
print("-" * 20, "\n")


# Q3. Write a function to calculate and return the factorial of a number (a non-negative integer).
print("--- Question 3: Calculate Factorial ---")
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

num = 5
print(f"The factorial of {num} is: {factorial(num)}")
print("-" * 20, "\n")


# Q4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
print("--- Question 4: Count Upper and Lower Case ---")
def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print(f"Original String: '{s}'")
    print(f"No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_count}")

count_case("The quick Brown Fox")
print("-" * 20, "\n")


# Q5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
print("--- Question 5: Print Even Numbers from a List ---")
def print_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    print(f"Original list: {numbers}")
    print(f"Even numbers: {even_list}")

print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("-" * 20, "\n")


# Q6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
print("--- Question 6: Check for Prime Number ---")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num_to_check = 7
if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")
print("-" * 20, "\n")
