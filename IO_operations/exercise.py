import string

# --- Setup: Create a dummy file for the exercises to use ---
# This part creates a file named 'sample.txt' in the same directory.
with open('sample.txt', 'w') as f:
    f.write("Hello world.\n")
    f.write("This is a test file for Python file handling.\n")
    f.write("Python is a powerful programming language.\n")
    f.write("File handling is an essential skill.\n")


# Q1. Write a program to read the entire content from a txt file and display it to the user.
print("--- Question 1: Read Entire File ---")
with open('sample.txt', 'r') as f:
    content = f.read()
    print("Content of sample.txt:")
    print(content)
print("-" * 20, "\n")


# Q2. Write a program to read first n lines from a txt file. Get n as user input.
print("--- Question 2: Read First N Lines ---")
n = int(input("Enter the number of lines to read: "))
with open('sample.txt', 'r') as f:
    print(f"First {n} lines of sample.txt:")
    for i in range(n):
        line = f.readline()
        if not line: # Stop if we reach the end of the file
            break
        print(line, end="")
print("\n" + "-" * 20, "\n")


# Q3. Write a program to accept input from user and append it to a txt file.
print("--- Question 3: Append to File ---")
text_to_append = input("Enter text to append to the file: ")
with open('sample.txt', 'a') as f:
    f.write("\n" + text_to_append)
print("Text has been appended successfully.")
print("-" * 20, "\n")


# Q4. Write a program to read contents from a txt file line by line and store each line into a list.
print("--- Question 4: Read Lines into a List ---")
with open('sample.txt', 'r') as f:
    lines_list = f.readlines()
    # Removing newline characters for cleaner output
    lines_list = [line.strip() for line in lines_list]
    print("Lines stored in a list:")
    print(lines_list)
print("-" * 20, "\n")


# Q5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
print("--- Question 5: Find Longest Word ---")
with open('sample.txt', 'r') as f:
    words = f.read().split()
    longest_word = max(words, key=len)
    print(f"The longest word in the file is: '{longest_word}'")
print("-" * 20, "\n")


# Q6. Write a program to count the frequency of a user entered word in a txt file.
print("--- Question 6: Count Word Frequency ---")
word_to_find = input("Enter a word to count its frequency: ")
with open('sample.txt', 'r') as f:
    content = f.read().lower()
    # To be accurate, we remove punctuation before splitting
    translator = str.maketrans('', '', string.punctuation)
    cleaned_content = content.translate(translator)
    words = cleaned_content.split()
    count = words.count(word_to_find.lower())
    print(f"The word '{word_to_find}' appears {count} times.")
print("-" * 20, "\n")
