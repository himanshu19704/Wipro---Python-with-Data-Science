# Project 1: Write a Python function that accepts a hyphen-separated sequence of colors
# as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
print("--- Project 1: Sort Hyphen-Separated Colors ---")
def sort_colors(color_string):
    colors = color_string.split('-')
    colors.sort()
    return "-".join(colors)

input_colors = "green-red-yellow-black-white"
sorted_colors = sort_colors(input_colors)
print(f"Original sequence: {input_colors}")
print(f"Sorted sequence: {sorted_colors}")
print("-" * 20, "\n")


# Project 2: Create a Python module with functions to analyze a name.
# (ispalindrome, count_the_vowels, frequency_of_letters)
# Then import and test the functions.
print("--- Project 2: Name Analyzer ---")

def ispalindrome(name):
    cleaned_name = name.lower().replace(" ", "")
    return cleaned_name == cleaned_name[::-1]

def count_the_vowels(name):
    vowels = "aeiou"
    count = 0
    for char in name.lower():
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    frequency = {}
    for char in name.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


# --- Code to test the functions ---
def analyze_name(user_name):
    print(f"\nAnalyzing '{user_name}'...")
    print("-" * 20)
    
    # Palindrome Check
    if string_utils.ispalindrome(user_name):
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")
    
    # Vowel Count
    vowel_count = string_utils.count_the_vowels(user_name)
    print(f"No of vowels: {vowel_count}")
    
    # Letter Frequency
    letter_freq = string_utils.frequency_of_letters(user_name)
    freq_parts = []
    for letter, count in sorted(letter_freq.items()):
        freq_parts.append(f"{letter}-{count}")
    output_string = ", ".join(freq_parts)
    print(f"Frequency of letters: {output_string}")
    print("-" * 20)

# Test with sample inputs
analyze_name("bob")
analyze_name("marcel bentok tanaka")
