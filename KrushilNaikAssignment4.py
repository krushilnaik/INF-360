# INF360 - Programming in Python
# Krushil Naik
# Assignment 3


import re


# (2/2 points) - Read the file story.txt and store the lines as a variable called story.You must use relative paths, assume the story.txt file is in the same folder as your script.
story = open("./story.txt", encoding="utf-8").readlines()

# (5/5 points) - Write a regular expression that will find all occurances of the phrase,  "Sherlock Holmes".
sherlock = re.compile(r"Sherlock Holmes")

# (5/5 points) - Using the substitue method, replace all occurances of "Sherlock Holmes" with your name, storing the count of these occurances as a variable called foundCount.
# (2/2 points) - Write a regular expression that will find all occurances of the phrase, "the".
# (3/3 points) - Create a variable called theCount, that stores the total number of occurances of the phrase "the".
# (3/3 points) - Print to the user, the original name, the replacement name, and the total number of occurances using a print command with a formatted string literal using a string that starts with f".
# (3/3 points) - Print to the user the a string that tells the user the total number of occurances of "the" using a print command with a formatted string literal using a string that starts with f".
# (1/1 points) - Save the story out to a new file called new_story.txt.
