import re

# Open the HTML file
file_path = 'task2.html'  # Adjust the file path as necessary
with open(file_path, 'r') as file:
    html_content = file.read()

# Regular expression to find image sizes (width and height attributes)
image_size_pattern = r'\b(?:width|height)\s*=\s*["\']?\d+["\']?'  # Matches width or height attributes with numeric values

# Find all matches
image_sizes = re.findall(image_size_pattern, html_content)

# Output the results
print("Image sizes found:", image_sizes)
