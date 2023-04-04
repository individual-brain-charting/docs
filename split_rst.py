import os
import re

# Open the input RST file
with open('index.rst', 'r') as input_file:
    content = input_file.read()

# Split the file into sections based on section headings
sections = re.split(r'\n\n(?=[A-Za-z0-9_\- ]+\n={3,}\n)', content)

# Create a directory to store the output files
os.makedirs('output', exist_ok=True)

# Write each section to a separate output file
for i, section in enumerate(sections):
    # Skip the first section, which contains the document title
    if i == 0:
        continue

    # Find the section title
    title_match = re.match(r'([A-Za-z0-9_\- ]+)\n={3,}\n', section)
    if title_match:
        title = title_match.group(1)
    else:
        title = f'section{i}'

    # Clean up the title (remove any special characters and spaces)
    title = title.replace(' ', '_').lower()
    title = ''.join(c for c in title if c.isalnum() or c == '_')

    # Write the section to a new RST file
    with open(f'output/{title}.rst', 'w') as output_file:
        output_file.write(section)