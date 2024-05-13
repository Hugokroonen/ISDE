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
        self.selected_measure = None # next job: deze gebruiken ipv st session state! Hij lijkt deze alleen niet te onthouden... 
        self.selected_type = None
        self.subsidy_amount= 0

    def run(self):
        format_option = lambda option: option.text

        # Initialize measure in session state
        if 'measure' not in st.session_state:
            st.session_state.measure = None    

        # 1. Welcome page 
        #if 'check_started' not in st.session_state:
            #with st.form(key='start_check', border=False):
                #st.markdown("<h2 style='color: #00007E; text-align: center;'>Begeleiding bij ISDE aanvraag </h2>", unsafe_allow_html=True)
                #column1, column2, colum3 = st.columns(3)
                #with column2:
                    #st.image("Wendy.png", caption="Samen ISDE aanvragen", use_column_width=False)
                #check_started = st.form_submit_button("Start ISDE check")
                #if check_started:
                    #st.session_state.check_started = True


        # 2. Check started 
        #if 'check_started' in st.session_state and st.session_state.measure is None:
        if st.session_state.measure is None:
            st.markdown("<h3 style='color: #00007E; text-align: center;'>Kies een maatregel voor de subsidieaanvraag</h3>", unsafe_allow_html=True)
            # Display clickable icons for each measure option
            #for measure in self.measures:
             #   st.image(measure.icon_path, use_column_width=False)
              #  if st.button("", key=measure.name, help=measure.name):
               #     st.session_state.measure = measure
            columns = st.columns(len(self.measures))

            for i, measure in enumerate(self.measures):
                with columns[i]:
                    column1, column2, column3 = st.columns(3)
                    with column2:
                        st.image(measure.icon_path, width=75)  # Set use_column_width to True for better sizing within the column
                    # Include a checkbox with a hidden label
                        if st.checkbox("", key=measure.name, help=measure.name, label_visibility='visible'):
                            st.session_state.measure = measure


        # 3. Heatpump selected 
        if st.session_state.measure is not None:
            if st.session_state.measure.name == 'Warmtepomp':
                    st.markdown("<h3 style='color: #00007E; text-align: center;'>Type warmtepomp</h3>", unsafe_allow_html=True)
                    with st.form(key="choose_heatpump_type", border=False):
                        measure_type = st.selectbox(
                            "Zoek het type warmtepomp", 
                            HEATPUMP_OPTIONS, 
                            format_func=format_option,
                            key = 'heatpump_selectbox'
                        )

                        measureTypeSelectionDone = st.form_submit_button("Check subsidie")
                    if measureTypeSelectionDone:
                        st.write("Je hebt gekozen voor het type warmtepomp:", measure_type.text)
                        st.session_state.measure_type = measure_type

        # 3. Insulation selected 
        if st.session_state.measure is not None:
            if st.session_state.measure.name == 'Isolatie':
                    st.markdown("<h3 style='color: #00007E; text-align: center;'>Type isolatie</h3>", unsafe_allow_html=True)
                    with st.form(key="choose_insulation_type", border=False):
                        measure_type = st.selectbox(
                            "Selecteer het type isolatie", 
                            INSULATION_OPTIONS, 
                            format_func=format_option,
                            key = 'insulation_selextbox'
                        )

                        measureTypeSelectionDone = st.form_submit_button("Verder")
                    if measureTypeSelectionDone:
                        st.write("Je hebt gekozen het type isolatie:", measure_type.text)
                        st.session_state.measure_type = measure_type

        # 4. Subsidy calculation
        if 'measure_type' in st.session_state:
            
            # Warmtepomp 
            if st.session_state.measure.name == 'Warmtepomp':
            # Read PDF and find subsidy amount based on selected measure_type
                self.subsidy_amount = get_heatpump_subsidy_amount(st.session_state.measure_type)

            # Isolatie (behalve glas)
            if st.session_state.measure.name == "Isolatie" and measure_type.value != 'window_insulation':
                with st.form(key="choose_insulated_m2", border=False):
                    # Numeric input for entering a number
                    number = st.number_input("Hoe veel M2 heb je geïsoleerd?", key='number_input')
                    # Submit button for the form
                    m2Done = st.form_submit_button("Verder")
                if m2Done:
                    self.subsidy_amount = get_insulation_subsidy_amount(st.session_state.measure_type, number)
            
            if 'glass_type_done' not in st.session_state:
                st.session_state.glass_type_done = False
            if 'submit_options' not in st.session_state:
                st.session_state.submit_options = False
            if 'glass_type_done' not in st.session_state:
                st.session_state.glass_type_done = False

            # Glas isolatie 
            if st.session_state.measure.name == "Isolatie" and measure_type.value == 'window_insulation':
                with st.form(key="choose_type_window", border=False):
                        measure_type = st.selectbox(
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
                                self.subsidy_amount = get_glass_subsidy_amount(m2, measure_type.value, 'glass', date)


        # 5. Print the result
        if self.subsidy_amount:
            st.success(f"Je kan €{self.subsidy_amount} subsidie krijgen voor deze maatregel!")
        if self.subsidy_amount is None:
            st.success(f"Je voldoet niet aan het minimum oppervlakte om voor subsidie in aanmerking te komen")

        # 6. Add another measure? Combinatie is x2 

if __name__ == '__main__':
    app=SubsidyApp()
    app.run()



