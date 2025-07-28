import sys

# Project 1: Happiness Score from Command Line Arguments
# Through command line arguments three strings separated by space are given to you.
# Each string is a series of numbers separated by hyphen(-).
# You like all the numbers in string 1 and dislike all the numbers in string 2.
# Third string contains the numbers given to you.
# When you encounter a number which is present in string 1, add 1 to your happiness,
# if it is present in string 2, add -1 to your happiness.
# Example execution: python your_script_name.py 3-1 5-7 1-5-3-8
print("--- Project 1: Happiness Score ---")
# We expect 4 arguments: script name, string1, string2, string3
if len(sys.argv) == 4:
    # sys.argv[1] is the 'like' string, e.g., '3-1'
    # sys.argv[2] is the 'dislike' string, e.g., '5-7'
    # sys.argv[3] is the numbers to check, e.g., '1-5-3-8'
    
    # Using sets for fast lookups
    like_set = set(sys.argv[1].split('-'))
    dislike_set = set(sys.argv[2].split('-'))
    numbers_to_check = sys.argv[3].split('-')
    
    happiness = 0
    for num in numbers_to_check:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1
            
    print(f"Like numbers: {like_set}")
    print(f"Dislike numbers: {dislike_set}")
    print(f"Numbers to check: {numbers_to_check}")
    print(f"Final happiness: {happiness}")
else:
    print("Usage for Project 1: python your_script_name.py <like-nums> <dislike-nums> <nums-to-check>")
    print("Example: python your_script_name.py 3-1 5-7 1-5-3-8")
print("-" * 20, "\n")
