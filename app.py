import streamlit as st
import pandas as pd
import numpy as np
from streamlit import session_state as ss

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
    st.dataframe(ss['squad_data'].sample(5))