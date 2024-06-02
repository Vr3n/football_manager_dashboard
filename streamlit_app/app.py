import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from st_aggrid import AgGrid

from streamlit import session_state as ss
from analyser import cleaning_data, attributes, plots, position
from components import containers

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
            ss['squad_data'], ['Height', 'Distance', 'Dist/90'])

        if ss['squad_data']["Wage"].dtypes == 'O':
            ss['squad_data']['Wage'] = ss['squad_data']['Wage'].str.extract(
                r'£?(\d+,?\d*)').fillna(0)
            ss['squad_data']['Wage'] = ss['squad_data']['Wage'].str.replace(
                ',', '').fillna(0.0).astype(float)

        percentage_columns = cleaning_data.detect_percentage_columns(
            ss['squad_data'])

        ss['squad_data'].loc[:, percentage_columns] = cleaning_data.convert_percentage_to_numeric(
            ss['squad_data'][percentage_columns])

        ss['squad_data'] = cleaning_data.fill_na(ss['squad_data'])

        attributes.calculate_attributes_of_positions(ss['squad_data'])

    if not ss['dna_calculated']:
        ss['squad_data'] = attributes.get_dna_score(ss['squad_data'], dna_attribs=[
            'Tea', 'Ant', 'Vis', 'Dec', 'Cmp', 'Pas', 'Fir', 'Tec', 'OtB', 'Pos'
        ])
        ss['dna_calculated'] = True

    st.write(
        "#### Basic Squad Summary."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        ui.metric_card(title="Total Players ", content=str(
            ss['squad_data']['UID'].count()), key="total_players")
        # with containers.card_container(key="nationalities_chart", styles=["height: 15px"]):
        #     st.plotly_chart(plots.nationality_proportion(ss['squad_data']), use_container_width=True)

    with col2:
        ui.metric_card(title="Average Wage (£) p/w 💷",
                       content=round(ss['squad_data']['Wage'].mean(), 2), key="average_wage")

    with col3:
        ui.metric_card(title="Average age ", content=round(
            ss["squad_data"]['Age'].mean(), 2), key="average_age")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    postion_details = position.get_all_position_players_details(
        ss['squad_data'])

    with col1:
        ui.metric_card(
            "Goalkeepers", postion_details['goalkeepers'].shape[0], key="gk_count")

    with col2:
        ui.metric_card(
            "Defense", postion_details['defense'].shape[0], key="def_count")

    with col3:
        ui.metric_card(
            "Defensive Midfielders", postion_details['defensive_midfielders'].shape[0], key="dm_count")

    with col4:
        ui.metric_card(
            "Midfielders", postion_details['midfielders'].shape[0], key="mid_count")

    with col5:
        ui.metric_card(
            "Attacking Midfielders", postion_details['attacking_midfielders'].shape[0], key="am_count")

    with col6:
        ui.metric_card(
            "Strickers", postion_details['attackers'].shape[0], key="att_count")

    col1, col2 = st.columns(2)

    with col1:
        with containers.card_container(key="nationalities_chart"):
            st.plotly_chart(plots.nationality_proportion(
                ss['squad_data']), use_container_width=True, theme=None)

    with col2:
        with containers.card_container(key="age_spread"):
            st.plotly_chart(plots.age_spread(
                ss['squad_data']), use_container_width=True, theme=None)

    col1, col2 = st.columns(2)

    with col1:
        with containers.card_container(key="wage_spread"):
            st.plotly_chart(plots.wage_spread(
                ss['squad_data']), use_container_width=True, theme=None)

    with col2:
        with containers.card_container(key="wage_by_importance"):
            st.plotly_chart(plots.wage_by_importance_bar(
                ss['squad_data']), use_container_width=True, theme=None)

    col1, col2 = st.columns(2)

    with col1:
        with containers.card_container(key="player_imp_card") as pltd:
            grid_options = {
                'columnDefs': [
                    {
                        'headerName': "Agreed Pla:ing Time",
                        "field": "Agreed Playing Time",
                        "checkboxSelection": True,
                    },
                    {
                        'headerName': "Count",
                        "field": "count"

                    }
                ],
                'rowSelection': 'multiple',
            }

            player_by_importance = ss['squad_data'].groupby('Agreed Playing Time')[
                'UID'].describe()[['count']].reset_index().sort_values(by='count', ascending=False)

            st.write("""##### Player Importance Counts""")
            AgGrid(player_by_importance, grid_options,
                   fit_columns_on_grid_load=True, key="playing_time_table")
            # grid_return = AgGrid(player_by_importance, grid_options)
            # new_df = grid_return["data"]

            # st.write(new_df)

    with col2:
        playing_time_hapiness = ss['squad_data'].groupby('Playing Time Happiness')[
            'Agreed Playing Time'].describe()[['count']].reset_index().sort_values(by='count', ascending=False)

        with containers.card_container(key="playing_hapiness_card") as plt:

            grid_options = {
                'columnDefs': [
                    {
                        'headerName': "Playing Time Happiness",
                        "field": "Playing Time Happiness",
                        "checkboxSelection": True,
                    },
                    {
                        'headerName': "Count",
                        "field": "count"
                    }
                ],
                'rowSelection': 'multiple',
            }

            st.write("##### Playing time hapiness")
            AgGrid(playing_time_hapiness, grid_options,
                   fit_columns_on_grid_load=True, key="playing_time_happiness_table")

    st.write(
        """
        ### Player Types.
        Get to know what types of players you have.
        """
    )

    abilities_names = {'mental': ['intelligence', 'focus', 'endeavour'],
                       'intelligence': ['creativity',
                                        'movement',
                                        'movement_att',
                                        'movement_def',
                                        'awareness_on_ball',
                                        'awareness_off_ball',
                                        'awareness',
                                        'decision_making_off_ball',
                                        'decision_making_on_ball',
                                        'decision_making'],
                       'physical': ['physical_presence', 'aerial_presence', 'mobility'],
                       'attacking': ['off_the_ball',
                                     'control',
                                     'passing_ability',
                                     'dribbling_ability',
                                     'shooting_ability',
                                     'holdup'],
                       'defense': ['marking_ability',
                                   'defensive_positioning',
                                   'closing_down_ability',
                                   'tackling_ability',
                                   'intercepting_ability',
                                   'tracking_back_ability',
                                   'clearing_ability']}

    attributes.calculate_player_abilities(
        ss['squad_data'])

    position_wise_player = position.get_all_position_players_details(
        ss['squad_data'])

    ss['filtered_by_ability_type'] = dict()

    for ability in abilities_names.keys():
        ss['filtered_by_ability_type'][ability] = ss['squad_data'][[
            'Name', 'Position', *abilities_names[ability]]]
        ss['filtered_by_ability_type'][ability]['best_ability'] = ss[
            'filtered_by_ability_type'][ability][abilities_names[ability]].idxmax(axis=1)

    with containers.card_container(key="goal_keepers"):
        st.write("### Goalkeepers")
        gk_df = position_wise_player['goalkeepers']
        st.dataframe(gk_df)