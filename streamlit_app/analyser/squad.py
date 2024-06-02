import pandas as pd
from st_aggrid import AgGrid


def get_squad_player_importance(df: pd.DataFrame):
    playing_time_groupby = df.groupby('Agreed Playing Time')

    playing_times_counts = playing_time_groupby[
        'UID'].describe()[['count']].reset_index().sort_values(
            by='count', ascending=False)

    importance_list = set(df['Agreed Playing Time'].values.tolist())

