import streamlit as st
import pandas as pd
import numpy as np
from streamlit import session_state as ss
from analyser import cleaning_data

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    page_title="Football manager analysis"
)

st.title("Football Manager Dashboard.")


if 'show_file_uploader' not in ss:
    ss['show_file_uploader'] = True

if 'squad_data' not in ss:
    ss['squad_data'] = None

## Hide the File Uploader if the file is present.
if ss['squad_data'] is None:
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        ss['squad_data'] = pd.read_html(uploaded_file)[0]

        ss['show_file_uploader'] = False
        st.rerun()

if ss['squad_data'] is not None:
    ss['squad_data'] = cleaning_data.drop_columns(ss['squad_data'], ['Ability','Injury Risk', 'SHP', 'CON', 'Fatigue', 'Position Selected', "Potential", 'Overall Happiness'])


    ss['squad_data'][['Appearances', 'Substitute Appearances']] = cleaning_data.appearances_fix(ss['squad_data'], col_name="Apps")

    cleaning_data.unit_values_to_numeric(ss['squad_data'],['Height', 'Distance', 'Dist/90', 'Wage'])


    percentage_columns = cleaning_data.detect_percentage_columns(ss['squad_data'])

    ss['squad_data'].loc[:, percentage_columns] = cleaning_data.convert_percentage_to_numeric(ss['squad_data'][percentage_columns])

    ss['squad_data'] = cleaning_data.fill_na(ss['squad_data'])


