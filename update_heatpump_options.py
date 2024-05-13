import re
from pypdf import PdfReader

# Creating a pdf reader object 
reader = PdfReader('warmtepompen.pdf')

# List to hold all the options
options = [
    "Option(text='Ik weet het merk en type nog niet', value=None)"
]

# Regular expression pattern to match 'number-number-R' or 'number-R'
pattern = re.compile(r"\d+-?\d*R")

# Iterate through all pages
for page_number in range(len(reader.pages)):
    page = reader.pages[page_number]  # Get a specific page from the PDF
    text = page.extract_text()        # Extract text from the page
    lines = text.split('\n')          # Split the text into lines

    # Iterate through each line
    for line in lines:
        elements = line.split()
        if len(elements) > 1:  # Check if there is more than one element
            relevant_elements = elements[1:]  # Exclude the first element

            for i, element in enumerate(relevant_elements):
                if pattern.match(element):  # Check if the element matches the pattern
                    # Join all elements before the matched element
                    extracted_text = " ".join(relevant_elements[:i])
                    value_text = extracted_text.lower().replace(' ', '_')  # Replace spaces with underscores for the value
                    options.append(f"Option(text='{extracted_text}', value='{value_text}'),")
                    break

# Print the resulting Python list
for option in options:
    print(option)

# Save the result to a text file
output_path = '/Users/hugokroonen/ISDE-regelhulp/opties.txt'
with open(output_path, 'w') as file:
    for option in options:
        file.write(option + '\n')
