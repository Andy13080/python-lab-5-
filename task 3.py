import re
import csv

# Open the file
input_file_path = 'task3.txt'  # Adjust the path if needed
output_file_path = 'output.csv'

with open(input_file_path, 'r') as file:
    text = file.read()

# Regular expressions for each field
id_pattern = r'\b\d{1,}\b'  # Matches IDs (integers)
last_name_pattern = r'\b[A-Z][a-zA-Z]*\b'  # Matches last names (words starting with a capital letter)
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Matches email addresses
registration_date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'  # Matches dates in the format YYYY-MM-DD
website_pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Matches URLs

# Extract fields
ids = re.findall(id_pattern, text)
last_names = re.findall(last_name_pattern, text)
emails = re.findall(email_pattern, text)
registration_dates = re.findall(registration_date_pattern, text)
websites = re.findall(website_pattern, text)

# Ensure all lists are of the same length
data_length = min(len(ids), len(last_names), len(emails), len(registration_dates), len(websites))
data = zip(ids[:data_length], last_names[:data_length], emails[:data_length], registration_dates[:data_length], websites[:data_length])

# Write to CSV
with open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['ID', 'Last Name', 'Email', 'Registration Date', 'Website'])
    # Write data
    writer.writerows(data)

print(f"Data has been written to {output_file_path}")
