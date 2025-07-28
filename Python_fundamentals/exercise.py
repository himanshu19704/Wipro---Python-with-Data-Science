# TM-01 Python Fundamentals
# ------------------------------------------------------
# EXERCISES

# Q1. Write a program to check if a given number is Positive, Negative or Zero.
num = int(input("Q1: Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q2. Write a program to check if a given number is odd or even.
num = int(input("Q2: Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3. Given two non-negative values, print true if they have the same last digit
a = int(input("Q3: Enter first number: "))
b = int(input("Q3: Enter second number: "))
if a % 10 == b % 10:
    print("True")
else:
    print("False")

# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
print("Q4:")
for i in range(1, 11):
    print(i, end="\t")
print()

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
print("Q5:")
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

# Q6. Write a program to check if a given number is prime or not.
num = int(input("Q6: Enter a number to check prime: "))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# Q7. Write a program to print prime numbers between 10 and 99.
print("Q7: Prime numbers between 10 and 99:")
for num in range(10, 100):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()

# Q8. Write a program to print the sum of all the digits of a given number.
num = int(input("Q8: Enter a number: "))
sum_digits = 0
temp = num
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print("Sum of digits:", sum_digits)

# Q9. Write a program to reverse a given number and print.
num = int(input("Q9: Enter a number: "))
rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reversed Number:", rev)

# Q10. Write a program to find if the given number is palindrome or not.
num = int(input("Q10: Enter a number: "))
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
