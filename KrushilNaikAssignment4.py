# INF360 - Programming in Python
# Krushil Naik
# Assignment 3


from functools import reduce
from pathlib import Path
import re

# (2/2 points) - Read the file story.txt and store the lines as a variable called story.
# You must use relative paths, assume the story.txt file is in the same folder as your script.
story = open("./story.txt", encoding="utf-8").readlines()

# (5/5 points) - Write a regular expression that will
# find all occurances of the phrase,  "Sherlock Holmes".
sherlock = re.compile(r"\bSherlock Holmes\b")

# (5/5 points) - Using the substitue method,
# replace all occurances of "Sherlock Holmes" with your name,
# storing the count of these occurances as a variable called foundCount.
foundCount = 0

for i, line in enumerate(story):
    if not line.strip():
        continue

    foundCount += len(sherlock.findall(line))
    story[i] = sherlock.sub("Krushil", line)


# (2/2 points) - Write a regular expression that will
# find all occurances of the phrase, "the".
the = re.compile(r"\bthe\b", re.IGNORECASE)

# (3/3 points) - Create a variable called theCount,
# that stores the total number of occurances of the phrase "the".
theCount = reduce(lambda a, b: a + b, [len(the.findall(_x)) for _x in story])


# (3/3 points) - Print to the user, the original name, the replacement name,
# and the total number of occurances using a print command
# with a formatted string literal using a string that starts with f".
print("Original Name: Sherlock Holmes")
print("Replacement Name: Krushil")
print(f"Total number replaced: {foundCount}")

# (3/3 points) - Print to the user the a string that tells the user
# the total number of occurances of "the" using a print command
# with a formatted string literal using a string that starts with f".
print(f"Number of 'the': {theCount}")

# (1/1 points) - Save the story out to a new file called new_story.txt.
NEW_FILE = "new_story.txt"

Path(NEW_FILE).write_text("\n".join(story))

print(f"New story saved to '{NEW_FILE}'")
