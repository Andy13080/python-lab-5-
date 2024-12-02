import re


file_path = 'task1_en.txt'  
with open(file_path, 'r') as file:
    text = file.read()


words_ending_in_e_pattern = r'\b\w*e\b'  
numbers_in_parentheses_pattern = r'\(\d+\)'  


words_ending_in_e = re.findall(words_ending_in_e_pattern, text) 
numbers_in_parentheses = re.findall(numbers_in_parentheses_pattern, text)


print("Words ending in 'e':", words_ending_in_e)
print("Numbers in parentheses:", numbers_in_parentheses)
