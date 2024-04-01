import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui

from streamlit import session_state as ss
from analyser import cleaning_data, attributes, plots

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

if 'data_cleaned' not in ss:
    ss['data_cleaned'] = False

if 'dna_calculated' not in ss:
    ss['dna_calculated'] = False

# Hide the File Uploader if the file is present.
if ss['squad_data'] is None:
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        ss['squad_data'] = pd.read_html(uploaded_file)[0]

        ss['show_file_uploader'] = False
        st.rerun()


if ss['squad_data'] is not None:

    if not ss['data_cleaned']:
        ss['squad_data'] = cleaning_data.drop_columns(ss['squad_data'], [
                                                      'Ability', 'Injury Risk',
                                                      'SHP', 'CON', 'Fatigue',
                                                      'Position Selected',
                                                      "Potential",
                                                      'Overall Happiness'])

        ss['squad_data'][['Appearances', 'Substitute Appearances']
                         ] = cleaning_data.appearances_fix(ss['squad_data'], col_name="Apps")

        cleaning_data.unit_values_to_numeric(
            ss['squad_data'], ['Height', 'Distance', 'Dist/90', 'Wage'])

        percentage_columns = cleaning_data.detect_percentage_columns(
            ss['squad_data'])

        ss['squad_data'].loc[:, percentage_columns] = cleaning_data.convert_percentage_to_numeric(
            ss['squad_data'][percentage_columns])

        ss['squad_data'] = cleaning_data.fill_na(ss['squad_data'])

        attributes.calculate_attributes_for_all_positions(ss['squad_data'])

    if not ss['dna_calculated']:
        ss['squad_data'] = attributes.get_dna_score(ss['squad_data'], dna_attribs=[
            'Tea', 'Ant', 'Vis', 'Dec', 'Cmp', 'Pas', 'Fir', 'Tec', 'OtB', 'Pos'
        ])
        ss['dna_calculated'] = True

    st.write(
        "#### Basic Squad Summary."
    )

    st.plotly_chart(plots.nationality_proportion(ss['squad_data']),
                    use_container_width=True)

    st.write(
        "#### Squad DNA score v/s the Age."
    )

    st.plotly_chart(plots.dnascore_vs_age(
        ss['squad_data']), use_container_width=True)

    st.write(
        '#### Squad DNA score v/s Wages'
    )

    st.plotly_chart(plots.dnascore_vs_wage(
        ss['squad_data']), use_container_width=True)
