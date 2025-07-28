import string

# Project 1: Find the Secret Message
print("--- Project 1: Secret Message Finder ---")

def find_secret_message(file_name, file_content):
    # Create the sample file for the project
    with open(file_name, 'w') as f:
        f.write(file_content)

    # Now read the file to find the hints
    with open(file_name, 'r') as f:
        lines = f.readlines()
        # Hint 1: Find meeting time from number of lines
        num_lines = len(lines)
        meeting_time = ""
        if 1 <= num_lines <= 12:
            meeting_time = f"{num_lines} AM"
        elif 12 < num_lines <= 24:
            meeting_time = f"{num_lines - 12} PM"

        # Hint 2: Find meeting place from most frequent word
        f.seek(0) # Go back to the start of the file to read again
        content = f.read().lower()
        translator = str.maketrans('', '', string.punctuation)
        cleaned_content = content.translate(translator)
        words = cleaned_content.split()
        
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        most_frequent_word = ""
        if word_freq:
                most_frequent_word = max(word_freq, key=word_freq.get)
        
        meeting_place = f"{most_frequent_word.capitalize()} Street"

        print(f"Analyzing {file_name}...")
        print(f"Meeting time: {meeting_time}")
        print(f"Meeting place: {meeting_place}\n")


# --- Sample 1 ---
sample1_content = """Cricket, a bat-and-ball park game played between two teams of eleven park
players on a field at the park center of which is a 20-metre (22-yard) pitch with
a wicket at each end, each"""
find_secret_message("project_sample1.txt", sample1_content)

# --- Sample 2 ---
sample2_content = """Football is a family of team sports that involve, to varying degrees, kicking a
ball to score a goal. Unqualified, the word football normally means the form of
football that is the most popular where the word is used. Sports commonly
called football include association football (known as soccer in some
countries); gridiron football (specifically American football or Canadian
football); Australian rules football; rugby football (either rugby league or rugby
union); and Gaelic football. These various forms of football share to
varying extent common origins.
The first grand "football" match in the USA was played between Rutgers and
Princeton in 1869.
The game was played at the College Avenue Gymnasium at Rutgers University,
New Brunswick.
This football game is often considered to be the first-ever intercollegiate
football game."""
find_secret_message("project_sample2.txt", sample2_content)
