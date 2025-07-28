#Mini Project :

# MINI PROJECT: Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and his or her interesting fact to the screen. Next, change a fact about one of
# the people. Also add an additional person and corresponding fact. Display the new list of people
# and facts. Run the program multiple times and notice if the order changes.
print("--- Mini Project: Interesting Facts ---")
facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original facts:")
for person, fact in facts.items():
    print(f"{person}: {fact}")

print("\n...Updating facts...\n")

# Change a fact about one person
facts["Jeff"] = "Is afraid of heights."

# Add a new person and fact
facts["Jill"] = "Can hula dance."

print("Updated facts:")
for person, fact in facts.items():
    print(f"{person}: {fact}")
print("-" * 20)



# MINI PROJECT: Given the participant's score sheet for your University Sports Day, you are
# required to find the runner-up score. You have scores. Store them in a list and
# find the score of the runner-up.
print("--- Mini Project: Finding the Runner-Up Score ---")
participant_scores = [2, 3, 6, 6, 5]
print(f"Here are the scores: {participant_scores}")

unique_scores = list(set(participant_scores))
unique_scores.sort(reverse=True)

if len(unique_scores) >= 2:
    runner_up = unique_scores[1]
    print(f"\nThe runner-up score is: {runner_up}")
else:
    print("\nThere aren't enough unique scores to have a runner-up.")
print("-" * 20)


# You have a record of n students. Each record contains the student's name, and
# their percent marks in Math, Physics and Chemistry. The marks can be floating
# values. You are required to save the record in a dictionary data type.
#
# Student's name is the key. Marks stored in a list is the value. The user enters a
# student's name. Output the average percentage marks obtained by that
# student.
#
# Formula: (sum of marks) / (no of subjects)
#
# Sample input: { "Krishna" : [67, 68, 69],
#                 "Arjun" : [70, 98, 63],
#                 "Malika" : [52, 56, 60] }
#
# Sample output:
# Enter a name: Malika
# Average percentage mark: 56
student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

student_name = input("Enter a name: ")

if student_name in student_marks:
    marks = student_marks[student_name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark for {student_name}: {average:.2f}")
else:
    print(f"Sorry, no record found for {student_name}.")
print("-" * 20, "\n")



# Project 4: Given a string of n words, help Alex to find out how many times his name
# appears in the string.
#
# Constraint: 1 <= n <= 200
#
# Sample input: Hi Alex WelcomeAlex Bye Alex.
# Sample output: 3

print("--- Project 4: Count Alex's Name ---")

input_string = "Hi Alex WelcomeAlex Bye Alex."
name_to_find = "Alex"

occurrence_count = input_string.count(name_to_find)

print(f"The input string is: '{input_string}'")
print(f"The name '{name_to_find}' appears {occurrence_count} times.")
print("-" * 20, "\n")
