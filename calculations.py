from pypdf import PdfReader 
from datetime import datetime



def get_heatpump_subsidy_amount(measure_type):
    # Read RVO PDF and find subsidy amount based on selected measure_type
    reader = PdfReader('/Users/hugokroonen/ISDE-regelhulp/warmtepompen.pdf') 
    subsidy_amount = None
    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number] 
        text = page.extract_text() 
        lines = text.split('\n')
        for line in lines:
            if measure_type.text in line:
                elements = line.split()
                for element in elements:
                    if element.endswith(",00") and element.count(",") == 1:
                        subsidy_amount = element
                        break
                break
        if subsidy_amount:
            break
    return subsidy_amount


def get_insulation_subsidy_amount(measure_type, m2):
    if measure_type.value == 'floor_insulation':
        subsidy_per_square_meter = 5.50
        min = 20
        max = 130

    if measure_type.value == 'subfloor_insulation':
        subsidy_per_square_meter = 3
        min = 20
        max = 130 

    if measure_type.value == 'wall_insulation':
        subsidy_per_square_meter = 4
        min = 10
        max = 170

    if measure_type.value == 'facade_insulation':
        subsidy_per_square_meter = 19
        min = 10
        max = 170

    if measure_type.value == 'roof_insulation':
        subsidy_per_square_meter = 15
        min = 20
        max = 200 

    if measure_type.value == 'attic_insulation':
        subsidy_per_square_meter = 4
        min = 20
        max = 130 

    if m2 >= min and m2 <= max:
        subsidy = m2 * subsidy_per_square_meter
        formatted_subsidy = f"{subsidy:.2f}".replace('.', ',')
        return formatted_subsidy

    elif m2 > max:
        subsidy = 130 * subsidy_per_square_meter
        formatted_subsidy = f"{subsidy:.2f}".replace('.', ',')
        return formatted_subsidy

    else:
        return None

def get_glass_subsidy_amount(m2, u_value, glass_type, date):
    subsidy = 0
    if glass_type == 'glass':
        if u_value == 'HR++':
            if date < datetime(2023, 1, 1):
                subsidy = m2 * 26.50
            else:
                subsidy = m2 * 23
        elif u_value == 'Triple':
            if date < datetime(2023, 1, 1):
                subsidy = m2 * 75
            else:
                subsidy = m2 * 65,50

    elif glass_type == 'panels':
        if u_value <= 0.7:
            if date < datetime(2023, 1, 1):
                subsidy = m2 * 57.50
            else:
                subsidy = m2 * 45
        elif u_value <= 1.2:
            if date < datetime(2023, 1, 1):
                subsidy = m2 * 11.50
            else:
                subsidy = m2 * 10
    
    elif glass_type == 'doors':
        if u_value <= 1.0:
            if date < datetime(2023, 1, 1):
                subsidy = m2 * 26.50
            else:
                subsidy = m2 * 23
        elif u_value <= 1.5:
            if date < datetime(2023, 1, 1):
                subsidy = m2 * 11.50
            else:
                subsidy = m2 * 10

    formatted_subsidy = f"{subsidy:.2f}".replace('.', ',')
    return formatted_subsidy

