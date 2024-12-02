import re

# Open the file
file_path = 'task1_en.txt'  # Adjust the path if the file is located elsewhere
with open(file_path, 'r') as file:
    text = file.read()

# Regular expression patterns
words_ending_in_e_pattern = r'\b\w*e\b'  # Matches words ending in 'e'
numbers_in_parentheses_pattern = r'\(\d+\)'  # Matches numbers in parentheses

# Find all matches
words_ending_in_e = re.findall(words_ending_in_e_pattern, text) 
numbers_in_parentheses = re.findall(numbers_in_parentheses_pattern, text)

# Output the results
print("Words ending in 'e':", words_ending_in_e)
print("Numbers in parentheses:", numbers_in_parentheses)
