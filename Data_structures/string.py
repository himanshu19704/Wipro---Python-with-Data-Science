#String

# Q1. Write a program to count the number of upper and lower case letters in a String.
print("--- Question 1: Count Upper and Lower Case Letters ---")
my_string = "Hello World! This is Python."
upper_count = 0
lower_count = 0
for char in my_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print(f"Original String: '{my_string}'")
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")
print("-" * 20, "\n")


# Q2. Write a program that will check whether a given String is Palindrome or not.
print("--- Question 2: Check for Palindrome ---")
test_string = "madam"
# A string is a palindrome if it reads the same forwards and backwards.
# We can check this by comparing the string to its reverse (string[::-1]).
if test_string == test_string[::-1]:
    print(f"The string '{test_string}' is a palindrome.")
else:
    print(f"The string '{test_string}' is not a palindrome.")
print("-" * 20, "\n")


# Q3. Given a string, return a new string made of n copies of the first 2 chars of the original string
# where n is the length of the string. The string length will be >=2.
# If input is "Wipro" then output should be "WiWiWiWiWi".
print("--- Question 3: Copies of First 2 Chars ---")
input_str = "Wipro"
n = len(input_str)
first_two = input_str[:2]
result = first_two * n
print(f"Input string: '{input_str}'")
print(f"Result: {result}")
print("-" * 20, "\n")


# Q4. Given a string, if the first or last character is 'x', return the string without those 'x'
# character, else return the string unchanged. If the input is "xHix", then output is "Hi".
print("--- Question 4: Remove 'x' from Ends ---")
input_val = "xHix"
print(f"Original string: '{input_val}'")
if input_val.endswith('x'):
    input_val = input_val[:-1]
if input_val.startswith('x'):
    input_val = input_val[1:]
print(f"Modified string: '{input_val}'")
print("-" * 20, "\n")


# Q5. Given a string and an integer n, return a string made of n repetitions of the last n characters
# of the string. You may assume that n is between 0 and the length of the string inclusive. For example
# if the inputs are "Wipro" and 3, then the output should be "propropro".
print("--- Question 5: Repetitions of Last N Chars ---")
source_string = "Wipro"
num = 3
last_n_chars = source_string[-num:]
final_result = last_n_chars * num
print(f"Input string: '{source_string}', n: {num}")
print(f"Result: {final_result}")
print("-" * 20, "\n")
