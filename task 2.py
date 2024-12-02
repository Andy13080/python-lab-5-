import re


file_path = 'task2.html'  
with open(file_path, 'r') as file:
    html_content = file.read()


image_size_pattern = r'\b(?:width|height)\s*=\s*["\']?\d+["\']?'  


image_sizes = re.findall(image_size_pattern, html_content)


print("Image sizes found:", image_sizes)
