
# Q1. Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
print("--- Question 1: Division with Exception Handling ---")
try:
    num1 = float(input("Enter the first number (numerator): "))
    num2 = float(input("Enter the second number (denominator): "))
    result = num1 / num2
    print(f"The result of {num1} / {num2} is: {result}")
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
print("-" * 20, "\n")


# Q2. Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.
print("--- Question 2: Prime Number Check with Exception Handling ---")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    num_to_check = int(input("Enter a number to check if it's prime: "))
    if is_prime(num_to_check):
        print(f"{num_to_check} is a prime number.")
    else:
        print(f"{num_to_check} is not a prime number.")
except ValueError:
    print("Error: Invalid input. Please enter a whole number.")
print("-" * 20, "\n")


# Q3. Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
print("--- Question 3: Open File with Exception Handling ---")
file_name_to_open = input("Enter the file name to open (e.g., test_file.txt): ")
try:
    with open(file_name_to_open, 'r') as f:
        content = f.read()
        print(f"\nContents of '{file_name_to_open}' in title case:")
        print(content.title())
except FileNotFoundError:
    print(f"Error: The file '{file_name_to_open}' was not found.")
print("-" * 20, "\n")


# Q4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
print("--- Question 4: Check List Index with Exception Handling ---")
my_list = [10, -20, 30, 40, -50, 60, 70, -80, 90, 100]
print(f"The list is: {my_list}")
try:
    index = int(input("Enter an index to check (0-9): "))
    number = my_list[index]
    if number >= 0:
        print(f"The number at index {index} is {number}, which is positive.")
    else:
        print(f"The number at index {index} is {number}, which is negative.")
except IndexError:
    print(f"Error: Invalid index. Please enter an index between 0 and {len(my_list) - 1}.")
except ValueError:
    print("Error: Invalid input. Please enter a whole number for the index.")
print("-" * 20, "\n")
