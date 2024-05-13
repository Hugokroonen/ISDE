# importing required modules 
from pypdf import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader('warmtepompen.pdf') 
  
# Iterate through all pages
for page_number in range(len(reader.pages)):
    # getting a specific page from the pdf file 
    page = reader.pages[page_number] 

    # extracting text from page 
    text = page.extract_text() 

    # Split the text into lines
    lines = text.split('\n')

    # Iterate through the lines to find the one containing "KA19525"
    for line in lines:
        if "Elga Ace 4 kW" in line:
            # Split the line by spaces to extract individual elements
            elements = line.split()
            # Iterate through the elements to find the one with ",00"
            for element in elements:
                # Check if the element ends with ",00" and contains only one comma
                if element.endswith(",00") and element.count(",") == 1:
                    print(element)
                    break  # Stop searching once the element is found
            break  # Stop searching once the line is found
