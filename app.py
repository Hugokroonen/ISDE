import streamlit as st
from options import *
from pypdf import PdfReader 

st.set_page_config(
    page_title="ISDE Regelhulp", 
    page_icon="🏠", 
    layout="centered", 
    initial_sidebar_state="auto", 
    menu_items={"Get help" : 'https://www.rvo.nl'}
)

format_option = lambda option: option.text
measure_type = None 
m2 = 0 


# Initialize measure in session state
if 'measure' not in st.session_state:
    st.session_state.measure = None    

if 'form1_submitted' not in st.session_state:
    with st.form(key='form1'):
        st.markdown("<h3 style='color: #00007E;'>Begeleiding bij ISDE subsidie aanvragen</h3>", unsafe_allow_html=True)
        st.image("Wendy.png", caption="Samen ISDE aanvragen", use_column_width=False)
        step_1_done = st.form_submit_button("Start ISDE check")
        if step_1_done:
            st.session_state.form1_submitted = True

if 'form1_submitted' in st.session_state and st.session_state.measure is None:
    st.markdown("<h3 style='color: #00007E;'>Kies voor welke maatregelen je subsidie aan wilt vragen</h3>", unsafe_allow_html=True)
    # Display clickable icons for each measure option
    for option in MEASURE_OPTIONS:
        st.image(option.icon_path, use_column_width=False)
        if st.button("", key=option.value, help=option.text):
            measure = option
            st.session_state.measure = measure

    
if 'form1_submitted' in st.session_state and st.session_state.measure is not None:
    if st.session_state.measure.value == 'heatpump':
            st.markdown("<h3 style='color: #00007E;'>Selecteer type warmtepomp</h3>", unsafe_allow_html=True)
            with st.form(key="heatpump_form"):
                measure_type = st.selectbox(
                    "Welke warmtepomp heb je aangeschaft", 
                    HEATPUMP_OPTIONS, 
                    format_func=format_option,
                    key = 'heatpump_selectbox'
                )

                measureTypeSelectionDone = st.form_submit_button("Check subsidie")
            if measureTypeSelectionDone:
                st.write("Je hebt gekozen voor de volgende maatregel:", measure_type.text)
                st.session_state.measure_type = measure_type

if 'form1_submitted' in st.session_state and st.session_state.measure is not None:
    if st.session_state.measure.value == 'insulation':
            st.markdown("<h3 style='color: #00007E;'>Selecteer type isolatie</h3>", unsafe_allow_html=True)
            with st.form(key="insulation_form"):
                measure_type = st.selectbox(
                    "Welke isolatie heb je gedaan", 
                    INSULATION_OPTIONS, 
                    format_func=format_option,
                    key = 'insulation_selextbox'
                )

                measureTypeSelectionDone = st.form_submit_button("Verder")
            if measureTypeSelectionDone:
                st.write("Je hebt gekozen voor de volgende maatregel:", measure_type.text)
                st.session_state.measure_type = measure_type

if 'measure_type' in st.session_state and measureTypeSelectionDone:
    if st.session_state.measure.value == 'heatpump':
    # Read PDF and find subsidy amount based on selected measure_type
        reader = PdfReader('/Users/hugokroonen/Downloads/warmtepompen.pdf') 
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

        if subsidy_amount:
            st.success(f"Je kan {subsidy_amount} subsidie krijgen voor deze maatregel!")
        else:
            st.warning("Subsidiebedrag niet gevonden voor deze maatregel.")

# Vloer en bodem 
if 'measure_type' in st.session_state:
    if st.session_state.measure_type.value == 'floor_insulation':
    # vloer 5,50 per m2 
        with st.form(key="floor_insulation_form"):
            # Numeric input for entering a number
            number = st.number_input("Hoe veel M2 heb je geïsoleerd?", key='number_input')
            # Submit button for the form
            m2Done = st.form_submit_button("Verder")
        if m2Done:
            st.session_state.m2 = number
            if st.session_state.measure_type.value == 'floor_insulation':
                subsidy_per_square_meter = 5.50
            if st.session_state.measure_type.value == 'bodem_isolatie':
                subsidy_per_square_meter = 3

            if st.session_state.m2 >= 20 and st.session_state.m2 <= 130:
                subsidy = number * subsidy_per_square_meter
                formatted_subsidy = f"€{subsidy:.2f}".replace('.', ',')
                st.success(f"Je kan {formatted_subsidy} krijgen voor deze maatregel!")

            elif st.session_state.m2 > 130:
                subsidy = 130 * subsidy_per_square_meter
                formatted_subsidy = f"€{subsidy:.2f}".replace('.', ',')
                st.success(f"Je kan {formatted_subsidy} krijgen voor deze maatregel!")

            else:
                st.success(f"Je voldoet niet aan het minimum oppervlakte om voor subsidie in aanmerking te komen")
        