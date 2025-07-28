import sys

# Q1. Write a program to accept two numbers as command line arguments and display their sum.
# Example execution: python your_script_name.py 10 20
print("--- Question 1: Sum of Two Numbers ---")
# sys.argv is a list containing the script name and the arguments.
# sys.argv[0] is the script name, sys.argv[1] is the first argument, etc.
if len(sys.argv) == 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(f"The sum of {num1} and {num2} is: {num1 + num2}")
    except ValueError:
        print("Please provide two integer numbers as arguments.")
else:
    # This part will run if the file is executed without the correct number of arguments
    print("Usage for Q1: python your_script_name.py <number1> <number2>")
print("-" * 20, "\n")


# Q2. Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
# Example execution: python your_script_name.py Welcome to Python
print("--- Question 2: Welcome Message ---")
if len(sys.argv) > 1:
    file_name = sys.argv[0]
    # Join all arguments from index 1 onwards to form the message
    welcome_message = " ".join(sys.argv[1:])
    print(f"File Name: {file_name}")
    print(f"Message: {welcome_message}")
else:
    print("Usage for Q2: python your_script_name.py <your welcome message>")
print("-" * 20, "\n")


# Q3. Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
# Example execution: python your_script_name.py 2 3 4 5 6 7 8 9 10 11
print("--- Question 3: Sum of Prime Numbers ---")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# To avoid conflict with other questions, we'll check for a specific number of arguments
# Let's assume the script is run with exactly 11 arguments (1 for script name + 10 numbers)
if len(sys.argv) == 11:
    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
        prime_sum = 0
        for num in numbers:
            if is_prime(num):
                prime_sum += num
        print(f"The numbers are: {numbers}")
        print(f"The sum of prime numbers among them is: {prime_sum}")
    except ValueError:
        print("Please provide 10 integer numbers as arguments.")
else:
    print("Usage for Q3: python your_script_name.py <10 numbers separated by spaces>")
print("-" * 20, "\n")
