import re

# Open the file
file_path = 'task_add.txt'  # Adjust the path if needed
with open(file_path, 'r') as file:
    text = file.read()

# Regular expression patterns
date_pattern = r'\s(?:\d{4}[-/.]\d{2}[-/.]\d{2}|\d{2}[-/.]\d{2}[-/.]\d{4})'  # Matches dates in various formats
email_pattern = r'\s[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Matches email addresses preceded by a space
website_pattern = r'\shttps?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Matches websites preceded by a space

# Find all matches
dates = re.findall(date_pattern, text)
emails = re.findall(email_pattern, text)
websites = re.findall(website_pattern, text)

# Clean up results to remove leading spaces
dates = [date.strip() for date in dates]
emails = [email.strip() for email in emails]
websites = [website.strip() for website in websites]

# Output the results
print("Dates found:", dates[:5])  # Ensure to get only 5
print("Emails found:", emails[:5])  # Ensure to get only 5
print("Websites found:", websites[:5])  # Ensure to get only 5
