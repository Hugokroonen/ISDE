import streamlit as st
from options import *
from pypdf import PdfReader 
from calculations import * 

st.set_page_config(
    page_title="ISDE Regelhulp", 
    page_icon="🏠", 
    layout="centered", 
    initial_sidebar_state="auto", 
    menu_items={"Get help" : 'https://www.rvo.nl'}
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

/* Apply the font family to all elements */
* {
    font-family: 'Poppins', sans-serif;
}

/* Center align text in main container */
main .block-container {
    text-align: center; 
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

/* Override Streamlit's default alignment for markdown text, including headers */
.markdown-text-container, .markdown-text-container h1, .markdown-text-container h2, .markdown-text-container h3 {
    text-align: center !important;
}

/* Center images and buttons */
.stImage, .stButton>button {
    margin: 0 auto !important;
    display: block;
}

/* Custom class for specifically aligned text if necessary */
.custom-text {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

class Measure:
    def __init__(self, name, options, icon_path, subsidy_file=None):
        self.name = name
        self.options = options
        self.icon_path = icon_path
        self.subsidy_file = subsidy_file
    

class SubsidyApp:
    def __init__(self):
        self.measures = [
            Measure("Warmtepomp", HEATPUMP_OPTIONS, "heatpump_icon.png", "/path/to/heatpump_subsidy.pdf"),
            Measure("Isolatie", INSULATION_OPTIONS, "insulation_icon.png"),
            #Measure('zonneboiler', None, 'solar_icon.png')
        ]
        self.selected_measure = None 
        self.selected_type = None
        self.heatpump_subsidy_amount= None
        self.insulation_subsidy_amount= None
        self.check_started = None


        if 'measure' not in st.session_state:
            st.session_state["measure"] = None  

        if 'check_started' not in st.session_state:
            st.session_state["check_started"] = False

        if 'check_done' not in st.session_state:
            st.session_state["done"] = False 

        if 'aanvraag_ingediend' not in st.session_state:
            st.session_state["aanvraag_ingediend"] = False 
        
        if 'selected_measures' not in st.session_state:
            st.session_state["selected_measures"] = []

    def run(self):
    
        format_option = lambda option: option.text

        # 1. Start check 
        if st.session_state["check_started"] == False and st.session_state["measure"] is None:
            with st.form(key='measure_selection', border=False):
                columns = st.columns(len(self.measures))
                for i, measure in enumerate(self.measures):
                     with columns[i]:
                        column1, column2, column3 = st.columns(3)
                        with column2:
                            st.markdown(f"<h6 style='color: #00007E; text-align: left;'>{measure.name}</h6>", unsafe_allow_html=True)
                            st.image(measure.icon_path, width=70)  
                            if st.checkbox("", key=measure.name, help=measure.name, label_visibility='hidden'):
                                st.session_state["selected_measures"].append(measure)
                                self.selected_measure = measure
            # Button to confirm the selection
                if st.form_submit_button('Start ISDE check'):
                    if self.selected_measure:
                        st.session_state["measure"] = self.selected_measure
                        st.session_state["check_started"] = True
                    else:
                        st.error("Selecteer eerst een maatregel!")
                        st.session_state["check_started"] = False


        # 2. Select heatpump 
        if st.session_state["check_started"] and any(measure.name == 'Warmtepomp' for measure in st.session_state["selected_measures"]):
            #if st.session_state.measure.name == 'Warmtepomp':
                    st.markdown("<h3 style='color: #00007E; text-align: center;'>Type warmtepomp</h3>", unsafe_allow_html=True)
                    with st.form(key="choose_heatpump_type", border=False):
                        heatpump_type = st.selectbox(
                            "Zoek het type warmtepomp", 
                            HEATPUMP_OPTIONS, 
                            format_func=format_option,
                            key = 'heatpump_selectbox'
                        )

                        col1, col2, col3, col4, col5, col6 = st.columns(6)
                        with col4:
                            measureTypeSelectionDone = st.form_submit_button("Verder")
                        with col3:
                            if st.form_submit_button('Terug'):
                                st.session_state.check_started = False
                                st.session_state.measure = None
                                st.rerun()
                        if measureTypeSelectionDone:
                            if heatpump_type.value is None:
                                st.success("Je kunt de ISDE hulp beginnen zonder merk en type, en deze later aanvullen voor een indicatief subsidiebedrag!")
                            else:
                                st.write("Je hebt gekozen voor het type warmtepomp:", heatpump_type.text)
                                st.session_state.heatpump_type = heatpump_type

            

        # 2. Select insulation 
        if st.session_state["check_started"] and any(measure.name == 'Isolatie' for measure in st.session_state["selected_measures"]):
                    st.markdown("<h3 style='color: #00007E; text-align: center;'>Type isolatie</h3>", unsafe_allow_html=True)
                    with st.form(key="choose_insulation_type", border=False):
                        insulation_type = st.selectbox(
                            "Selecteer het type isolatie", 
                            INSULATION_OPTIONS, 
                            format_func=format_option,
                            key = 'insulation_selextbox'
                        )

                        col1, col2, col3, col4, col5, col6 = st.columns(6)
                        with col4:
                            measureTypeSelectionDone = st.form_submit_button("Verder")
                        with col3:
                            if st.form_submit_button('Terug'):
                                st.session_state.check_started = False
                                st.session_state.measure = None
                                st.rerun()

                    if measureTypeSelectionDone:
                        st.write("Je hebt gekozen het type isolatie:", insulation_type.text)
                        st.session_state.insulation_type = insulation_type

        # 3. Subsidy calculation
        if ('heatpump_type' in st.session_state or 'insulation_type' in st.session_state) and st.session_state["measure"] is not None:
            # 3.1 Warmtepomp 
            if any(measure.name == 'Warmtepomp' for measure in st.session_state["selected_measures"]):
            # Read PDF and find subsidy amount based on selected measure_type
                self.heatpump_subsidy_amount = get_heatpump_subsidy_amount(st.session_state.heatpump_type)

            # 3.2 Isolatie (behalve glas)
            if any(measure.name == 'Isolatie' for measure in st.session_state["selected_measures"]) and insulation_type.value != 'window_insulation':
                with st.form(key="choose_insulated_m2", border=False):
                    # Numeric input for entering a number
                    number = st.number_input("Hoe veel M2 heb je geïsoleerd?", key='number_input')
                    # Submit button for the form
                    col1, col2, col3, col4, col5, col6 = st.columns(6)
                    with col4:
                            m2Done = st.form_submit_button("Verder")
                    with col3:
                            if st.form_submit_button('Terug'):
                                st.session_state.check_started = False
                                st.session_state.measure = None
                                st.rerun()

                if m2Done:
                    self.insulation_subsidy_amount = get_insulation_subsidy_amount(st.session_state.insulation_type, number)
            
            if 'glass_type_done' not in st.session_state:
                st.session_state.glass_type_done = False
            if 'submit_options' not in st.session_state:
                st.session_state.submit_options = False
            if 'glass_type_done' not in st.session_state:
                st.session_state.glass_type_done = False

            # 3.3 Glas isolatie 
            if any(measure.name == 'Isolatie' for measure in st.session_state["selected_measures"]) and insulation_type.value == 'window_insulation':
                with st.form(key="choose_type_window", border=False):
                        insulation_type = st.selectbox(
                            "Triple of HR?", 
                            GLASS_OPTIONS, 
                            format_func=format_option,
                            key = 'glass_type_selection'
                        )
                        glass_type_done = st.form_submit_button("Verder")
                if glass_type_done:
                    st.session_state.glass_type_done = True

            if st.session_state.glass_type_done:
                    # New form for choosing options
                    with st.form(key="options_form", border=False):
                        st.text('Kies of je een of meerdere van de volgende maatregelen getroffen hebt')
                        option1 = st.checkbox("Isolerende panelen in kozijnen", key='panelen')
                        option2 = st.checkbox("Isolerende deuren", key='deuren')
                        option3 = st.checkbox("Geen van beiden", key='None')

                        submit_options = st.form_submit_button("Submit Options")

                    if submit_options:
                        st.session_state.submit_options = True 

                    if st.session_state.submit_options and st.session_state.glass_type_done:
                        if option3 and not option1 and not option2:
                            with st.form(key="choose_insulated_m2", border=False):
                                # Numeric input for entering a number
                                m2 = st.number_input("Hoe veel M2 heb je geïsoleerd?", key='number_input')
                                # Submit button for the for
                                m2Done = st.form_submit_button("Verder")
                            if m2Done:
                                date_string = '2022-12-31'
                                date = datetime.strptime(date_string, '%Y-%m-%d')
                                self.insulation_subsidy_amount = get_glass_subsidy_amount(m2, insulation_type.value, 'glass', date)


        # . Print the result. If we obtain a subsidy amount, we format is as string. If requirements are not met, we return an integer, which is the minimum amount of m2 that is needed. 
        if self.heatpump_subsidy_amount is not None and self.insulation_subsidy_amount is None:
            if isinstance(self.heatpump_subsidy_amount, str):
                st.success(f"Je kunt tot €{self.heatpump_subsidy_amount} subsidie krijgen voor deze warmtepomp!")
                st.session_state["done"] = True
    
            else:
                st.success(f"Er is iets misgegaan.")


        if self.heatpump_subsidy_amount is None and self.insulation_subsidy_amount is not None:
            if isinstance(self.insulation_subsidy_amount, str):
                st.success(f"Je kunt tot €{self.insulation_subsidy_amount} subsidie krijgen voor deze isolatiemaatregel!")
                st.session_state["done"] = True
    
            if isinstance(self.insulation_subsidy_amount, int):
                st.error(f"Je voldoet niet aan het minimum oppervlakte ({self.insulation_subsidy_amount}m2) om voor subsidie in aanmerking te komen")
                st.session_state["done"] = True

        if self.heatpump_subsidy_amount is not None and self.insulation_subsidy_amount is not None:
             
            if isinstance(self.heatpump_subsidy_amount, str):
                st.success(f"Je kunt tot €{self.heatpump_subsidy_amount} subsidie krijgen voor deze warmtepomp!")
                st.session_state["done"] = True
    
            elif isinstance(self.heatpump_subsidy_amount, int):
                st.error(f"Er is iets misgegaan")

            if isinstance(self.insulation_subsidy_amount, str):
                st.success(f"Je kunt tot €{self.insulation_subsidy_amount} subsidie krijgen voor deze isolatiemaatregel!")
                st.session_state["done"] = True
    
            if isinstance(self.insulation_subsidy_amount, int):
                st.error(f"Je voldoet niet aan het minimum oppervlakte ({self.insulation_subsidy_amount}m2) om voor subsidie in aanmerking te komen")
                st.session_state["done"] = True


        

        if st.session_state["done"]:
            with st.form(key='aanvragen', border=False):
                aanvragen = st.form_submit_button("Direct ISDE aanvragen!") 
            if aanvragen: 
                st.session_state["aanvraag_ingediend"] = True

        if st.session_state["aanvraag_ingediend"]:
            with st.form(key = 'personal_details', border=False):
                naam = st.text_input("Voornaam")
                email = st.text_input("Email")
                IBAN = st.text_input("IBAN")
                submission_done = st.form_submit_button("Dien je aanvraag in") 
                if submission_done: 
                    st.success("Je ISDE aanvraag is ingediend. Wij gaan direct voor je aan de slag. Binnen 2 werkdagen ontvang je feedback op je aanvraag")

  # 6. Add another measure? Combinatie is x2 

if __name__ == '__main__':
        app=SubsidyApp()
        app.run()
        print('run')
