import pandas as pd
from typing import Dict


def get_all_position_players_details(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    defensive_players = df[df['Position'].apply(lambda x: ('D (C)' in x) | ('D (RC)' in x) | ('D/WB (L)' in x) | ('D/WB (R)' in x) | ('D (LC)' in x) | ('WB (L)' in x) | ('WB (R)' in x))]

    defensive_midfielder_players = df[df['Position'].apply(lambda x: ('DM' in x))]

    midfield_players = df[df['Position'].apply(lambda x: ('M (C)' in x) | ('M/AM (C)' in x))]

    attacking_midfield_players = df[df['Position'].apply(lambda x: ('M/AM (C)' in x) | ('AM ' in x))]

    goalkeeping_players = df[df['Position'].apply(lambda x: ('SK' in x) | ('GK' in x))]

    attacking_midfield_players = df[df['Position'].apply(lambda x: ('M/AM (C)' in x) | ('AM ' in x))]

    attacking_players = df[df['Position'].apply(lambda x: ('ST ' in x))]

    positions: Dict[str, pd.DataFrame] = {
        'goalkeepers': goalkeeping_players,
        'defense': defensive_players,
        'defensive_midfielders': defensive_midfielder_players,
        'midfielders': midfield_players,
        'attacking_midfielders': attacking_midfield_players,
        'attackers': attacking_players
    }

    return positions

