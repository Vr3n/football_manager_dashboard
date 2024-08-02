import pandas as pd
from typing import List, Dict




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



def get_dna_score(df: pd.DataFrame, dna_attribs: List[str]):
    total_dna_score = len(dna_attribs) * 20

    squad_dna_score = round(
        (df[dna_attribs].sum(axis=1) / total_dna_score) * 100,
        2)

    df = pd.concat([df, pd.DataFrame({'dna_score': squad_dna_score})], axis=1)

    return df



def calculate_player_abilities(df: pd.DataFrame) -> pd.DataFrame:
    ## Defining the attribute type of columns needed to filter.
    intelligence = ["Ant", "Fla", "Dec", "Tea", "Vis"]
    focus = ["Cmp", "Cnt"]
    endeavour = ["Agg", "Bra", "Det", "Wor"]

    # Type of Intelligence.
    creativity = ["Ant", "Dec", "Fla", "Tea", "Vis"]

    movement = ["Ant", "Dec", "Tea"]
    movement_att = ["OtB"] + ["Ant", "Dec", "Tea"]
    movement_def = ["Pos"] + ["Ant", "Dec", "Tea"]

    awareness_on_ball = ["Ant", "Tea", "Vis"]
    awareness_off_ball = ["Ant", "Tea"]

    decision_making_on_ball = ["Dec", "Fla", "Tea"]
    decision_making_off_ball = ["Dec", "Tea"]

    # Physical Abilities.
    physical_presence_primary = ["Bal", "Str"]
    physical_presence_key = endeavour
    physical_presence = physical_presence_primary + physical_presence_key

    aerial_presence_primary = ["Jum"]
    aerial_presence_key = ["Det", "Wor"]
    aerial_presence_rel = physical_presence
    aerial_presence_other = ['Height']
    aerial_presence = aerial_presence_primary + aerial_presence_key + aerial_presence_rel + aerial_presence_other

    mobility_primary = ["Acc", "Agi", "Pac"]
    mobility_key = ["Det", "Wor"]
    mobility = mobility_primary + mobility_key

    # Attacking Abilities.

    off_the_ball_primary = ["OtB", "Cmp"]
    off_the_ball_key = movement + focus + ['Det']
    off_the_ball_rel = mobility + physical_presence

    control_primary = ["Fir", "Tec", "Cmp"]
    control_key = ["Ant", "Dec", "Fla", "Tea", "Vis", "Cmp", "Cnt", "Det"]
    control_rel = aerial_presence + physical_presence

    passing_ability_primary = ["Pas", "Tec", "Cmp"]
    passing_ability_key = creativity + focus + ["Det"]


    dribbling_ability_primary = ["Dri", "Tec", "Cmp"]
    dribbling_ability_key = ["Ant", "Vis", "Dec", "Fla", "Cmp", "Cnt", "Det"]
    dribbling_ability_rel = mobility + physical_presence

    shooting_ability_primary = ["Fin", "Lon", "Tec", "Cmp"]
    shooting_ability_key = ["Ant", "Dec", "Fla", "Tea", "Vis", "Cmp", "Cnt", "Det"]
    shooting_ability_rel = aerial_presence + physical_presence

    holdup_primary = ["Cmp"]
    holdup_key = ["Ant", "Tea", "Dec", "Cmp", "Cnt", "Det"]
    holdup_rel = physical_presence

    # Defensive Abilities.

    marking_ability_primary = ["Mar", "Cmp", "Pos"]
    marking_ability_key = movement + focus + ["Det"]
    marking_ability_rel = mobility + physical_presence

    defensive_positioning_primary = ['Cmp', 'Pos']
    defensive_positioning_key = movement + focus + ['Det']
    defensive_positioning_rel = mobility + physical_presence

    closing_down_ability_primary = ['Cmp', "Pos"]
    closing_down_ability_key = movement + focus + endeavour
    closing_down_ability_rel = mobility

    tackling_ability_primary = ["Tck", "Cmp"]
    tackling_ability_key = ["Ant", "Dec", "Cmp", "Cnt", "Det"]
    tackling_ability_rel = physical_presence

    intercepting_ability_primary = ['Cmp']
    intercepting_ability_key = movement + focus + ['Det']
    intercepting_ability_physical_key = mobility + physical_presence + aerial_presence
    intercepting_ability = intercepting_ability_primary + intercepting_ability_key + intercepting_ability_physical_key

    tracking_back_ability_primary = ['Cmp']
    tracking_back_ability_key = movement + focus + ["Det"] + mobility
    tracking_back_ability = tracking_back_ability_primary + tracking_back_ability_key

    clearing_ability_primary = ['Hea', 'Tec', 'Cmp']
    clearing_ability_key = awareness_off_ball + awareness_on_ball + ['Dec'] + focus + ['Det']
    clearing_ability = clearing_ability_primary + clearing_ability_key

    # Calculating the abilities.
    df['intelligence'] =  (df[intelligence].sum(axis=1) / (len(intelligence) * 20)) * 100
    df['focus'] =  (df[focus].sum(axis=1) / (len(focus) * 20)) * 100
    df['endeavour'] =  (df[endeavour].sum(axis=1) / (len(endeavour) * 20)) * 100
    df['creativity'] =  (df[creativity].sum(axis=1) / (len(creativity) * 20)) * 100
    df['movement_att'] =  df[movement_att].sum(axis=1) / (len(movement_att) * 20)
    df['movement_def'] =  df[movement_def].sum(axis=1) / (len(movement_def) * 20)
    df['movement'] = round((df['movement_att'] * 0.5 +  df['movement_def'] * 0.5) * 100, 2)
    df['awareness_on_ball'] =  df[awareness_on_ball].sum(axis=1) / (len(awareness_on_ball) * 20)
    df['awareness_off_ball'] =  df[awareness_off_ball].sum(axis=1) / (len(awareness_off_ball) * 20)
    df['awareness'] = round((df['awareness_on_ball'] * 0.5 +  df['awareness_off_ball'] * 0.5) * 100, 2)
    df['decision_making_on_ball'] =  df[decision_making_on_ball].sum(axis=1) / (len(decision_making_on_ball) * 20)
    df['decision_making_off_ball'] =  df[decision_making_off_ball].sum(axis=1) / (len(decision_making_off_ball) * 20)
    df['decision_making'] = round((df['decision_making_on_ball'] * 0.5 +  df['decision_making_off_ball'] * 0.5) * 100, 2)

    df['physical_presence_primary'] =  df[physical_presence_primary].sum(axis=1) / (len(physical_presence_primary) * 20)
    df['physical_presence_key'] =  df[physical_presence_key].sum(axis=1) / (len(physical_presence_key) * 20)
    df['physical_presence'] = round((df['physical_presence_primary'] * 0.7 +  df['physical_presence_key'] * 0.3) * 100, 2)

    df['aerial_presence_primary'] =  df[aerial_presence_primary].sum(axis=1) / (len(aerial_presence_primary) * 20)
    df['aerial_presence_key'] =  df[aerial_presence_key].sum(axis=1) / (len(aerial_presence_key) * 20)
    df['aerial_presence_rel'] =  df[aerial_presence_rel].sum(axis=1) / (len(aerial_presence_rel) * 20)
    df['aerial_presence_other'] =  df[aerial_presence_other].sum(axis=1) / 200
    df['aerial_presence'] = round((df['aerial_presence_primary'] * 0.4 +  df['aerial_presence_key'] * 0.3 + df['aerial_presence_rel'] * 0.2 + df['aerial_presence_other'] * 0.1) * 100, 2)

    df['mobility_primary'] =  df[mobility_primary].sum(axis=1) / (len(mobility_primary) * 20)
    df['mobility_key'] =  df[mobility_key].sum(axis=1) / (len(mobility_key) * 20)
    df['mobility'] = round((df['mobility_primary'] * 0.7 +  df['mobility_key'] * 0.3) * 100, 2)

    df['off_the_ball_primary'] =  df[off_the_ball_primary].sum(axis=1) / (len(off_the_ball_primary) * 20)
    df['off_the_ball_key'] =  df[off_the_ball_key].sum(axis=1) / (len(off_the_ball_key) * 20)
    df['off_the_ball_rel'] =  df[off_the_ball_rel].sum(axis=1) / (len(off_the_ball_rel) * 20)
    df['off_the_ball'] = round((df['off_the_ball_primary'] * 0.5 +  df['off_the_ball_key'] * 0.3 + df['off_the_ball_rel'] * 0.2) * 100, 2)

    df['control_primary'] =  df[control_primary].sum(axis=1) / (len(control_primary) * 20)
    df['control_key'] =  df[control_key].sum(axis=1) / (len(control_key) * 20)
    df['control_rel'] =  df[control_rel].sum(axis=1) / (len(control_rel) * 20)
    df['control'] = round((df['control_primary'] * 0.5 +  df['control_key'] * 0.3 + df['control_rel'] * 0.2) * 100, 2)

    df['passing_ability_primary'] =  df[passing_ability_primary].sum(axis=1) / (len(passing_ability_primary) * 20)
    df['passing_ability_key'] =  df[passing_ability_key].sum(axis=1) / (len(passing_ability_key) * 20)
    df['passing_ability'] = round((df['passing_ability_primary'] * 0.7 +  df['passing_ability_key'] * 0.3) * 100, 2)

    df['dribbling_ability_primary'] =  df[dribbling_ability_primary].sum(axis=1) / (len(dribbling_ability_primary) * 20)
    df['dribbling_ability_key'] =  df[dribbling_ability_key].sum(axis=1) / (len(dribbling_ability_key) * 20)
    df['dribbling_ability_rel'] =  df[dribbling_ability_rel].sum(axis=1) / (len(dribbling_ability_rel) * 20)
    df['dribbling_ability'] = round((df['dribbling_ability_primary'] * 0.5 +  df['dribbling_ability_key'] * 0.3 + df['dribbling_ability_rel'] * 0.2) * 100, 2)

    df['shooting_ability_primary'] =  df[shooting_ability_primary].sum(axis=1) / (len(shooting_ability_primary) * 20)
    df['shooting_ability_key'] =  df[shooting_ability_key].sum(axis=1) / (len(shooting_ability_key) * 20)
    df['shooting_ability_rel'] =  df[shooting_ability_rel].sum(axis=1) / (len(shooting_ability_rel) * 20)
    df['shooting_ability'] = round((df['shooting_ability_primary'] * 0.5 +  df['shooting_ability_key'] * 0.3 + df['shooting_ability_rel'] * 0.2) * 100, 2)

    df['holdup_primary'] =  df[holdup_primary].sum(axis=1) / (len(holdup_primary) * 20)
    df['holdup_key'] =  df[holdup_key].sum(axis=1) / (len(holdup_key) * 20)
    df['holdup_rel'] =  df[holdup_rel].sum(axis=1) / (len(holdup_rel) * 20)
    df['holdup'] = round((df['holdup_primary'] * 0.5 +  df['holdup_key'] * 0.3 + df['holdup_rel'] * 0.2) * 100, 2)

    df['marking_ability_primary'] =  df[marking_ability_primary].sum(axis=1) / (len(marking_ability_primary) * 20)
    df['marking_ability_key'] =  df[marking_ability_key].sum(axis=1) / (len(marking_ability_key) * 20)
    df['marking_ability_rel'] =  df[marking_ability_rel].sum(axis=1) / (len(marking_ability_rel) * 20)
    df['marking_ability'] = round((df['marking_ability_primary'] * 0.5 +  df['marking_ability_key'] * 0.3 + df['marking_ability_rel'] * 0.2) * 100, 2)

    df['defensive_positioning_primary'] =  df[defensive_positioning_primary].sum(axis=1) / (len(defensive_positioning_primary) * 20)
    df['defensive_positioning_key'] =  df[defensive_positioning_key].sum(axis=1) / (len(defensive_positioning_key) * 20)
    df['defensive_positioning_rel'] =  df[defensive_positioning_rel].sum(axis=1) / (len(defensive_positioning_rel) * 20)
    df['defensive_positioning'] = round((df['defensive_positioning_primary'] * 0.5 +  df['defensive_positioning_key'] * 0.3 + df['defensive_positioning_rel'] * 0.2) * 100, 2)

    df['closing_down_ability_primary'] =  df[closing_down_ability_primary].sum(axis=1) / (len(closing_down_ability_primary) * 20)
    df['closing_down_ability_key'] =  df[closing_down_ability_key].sum(axis=1) / (len(closing_down_ability_key) * 20)
    df['closing_down_ability_rel'] =  df[closing_down_ability_rel].sum(axis=1) / (len(closing_down_ability_rel) * 20)
    df['closing_down_ability'] = round((df['closing_down_ability_primary'] * 0.5 +  df['closing_down_ability_key'] * 0.3 + df['closing_down_ability_rel'] * 0.2) * 100, 2)

    df['tackling_ability_primary'] =  df[tackling_ability_primary].sum(axis=1) / (len(tackling_ability_primary) * 20)
    df['tackling_ability_key'] =  df[tackling_ability_key].sum(axis=1) / (len(tackling_ability_key) * 20)
    df['tackling_ability_rel'] =  df[tackling_ability_rel].sum(axis=1) / (len(tackling_ability_rel) * 20)
    df['tackling_ability'] = round((df['tackling_ability_primary'] * 0.5 +  df['tackling_ability_key'] * 0.3 + df['tackling_ability_rel'] * 0.2) * 100, 2)

    df['intercepting_ability_primary'] =  df[intercepting_ability_primary].sum(axis=1) / (len(intercepting_ability_primary) * 20)
    df['intercepting_ability_key'] =  df[intercepting_ability_key].sum(axis=1) / (len(intercepting_ability_key) * 20)
    df['intercepting_ability_physical_key'] =  df[intercepting_ability_physical_key].sum(axis=1) / (len(intercepting_ability_physical_key) * 20)
    df['intercepting_ability'] = round((df['intercepting_ability_primary'] * 0.5 +  df['intercepting_ability_key'] * 0.25 + df['intercepting_ability_physical_key'] * 0.25) * 100, 2)

    df['tracking_back_ability_primary'] =  df[tracking_back_ability_primary].sum(axis=1) / (len(tracking_back_ability_primary) * 20)
    df['tracking_back_ability_key'] =  df[tracking_back_ability_key].sum(axis=1) / (len(tracking_back_ability_key) * 20)
    df['tracking_back_ability'] = round((df['tracking_back_ability_primary'] * 0.7 +  df['tracking_back_ability_key'] * 0.3) * 100, 2)
    
    df['clearing_ability_primary'] =  df[clearing_ability_primary].sum(axis=1) / (len(clearing_ability_primary) * 20)
    df['clearing_ability_key'] =  df[clearing_ability_key].sum(axis=1) / (len(clearing_ability_key) * 20)
    df['clearing_ability'] = round((df['clearing_ability_primary'] * 0.7 +  df['clearing_ability_key'] * 0.3) * 100, 2)









def calculate_attributes_of_positions(df: pd.DataFrame):
    # calculates Goalkeeper_Defend score
    df['gkd_key'] = ( df['Agi'] + df['Ref'] )
    df['gkd_green'] = ( df['Aer'] + df['Cmd'] + df['Han'] + df['Kic'] + df['Cnt'] + df['Pos'] )
    df['gkd_blue'] = ( df['1v1'] + df['Thr'] + df['Ant'] + df['Dec'] )
    df['gkd'] =( ( ( df['gkd_key'] * 5) + (df['gkd_green'] * 3) + (df['gkd_blue'] * 1) ) / 32)
    df.gkd= df.gkd.round(1)

    # calculates Sweeper_keeper_Defend score
    df['skd_key'] = ( df['Agi'] + df['Ref'] )
    df['skd_green'] = ( df['Cmd'] + df['Kic'] + df['1v1'] + df['Ant'] + df['Cnt'] + df['Pos'] )
    df['skd_blue'] = ( df['Aer'] + df['Fir'] + df['Han'] + df['Pas'] + df['TRO'] + df['Dec'] + df['Vis'] + df['Acc'] )
    df['skd'] =( ( ( df['skd_key'] * 5) + (df['skd_green'] * 3) + (df['skd_blue'] * 1) ) / 36)
    df.skd= df.skd.round(1)

    # calculates Sweeper_keeper_Support score
    df['sks_key'] = ( df['Agi'] + df['Ref'] )
    df['sks_green'] = ( df['Cmd'] + df['Kic'] + df['1v1'] + df['Ant'] + df['Cnt'] + df['Pos'] )
    df['sks_blue'] = ( df['Aer'] + df['Fir'] + df['Han'] + df['Pas'] + df['TRO'] + df['Dec'] + df['Vis'] + df['Acc'] )
    df['sks'] =( ( ( df['sks_key'] * 5) + (df['sks_green'] * 3) + (df['sks_blue'] * 1) ) / 36)
    df.sks= df.sks.round(1)
        


    # calculates Sweeper_keeper_Attack score
    df['ska_key'] = ( df['Agi'] + df['Ref'] )
    df['ska_green'] = ( df['Cmd'] + df['Kic'] + df['1v1'] + df['Ant'] + df['Cnt'] + df['Pos'] )
    df['ska_blue'] = ( df['Aer'] + df['Fir'] + df['Han'] + df['Pas'] + df['TRO'] + df['Dec'] + df['Vis'] + df['Acc'] )
    df['ska'] =( ( ( df['ska_key'] * 5) + (df['ska_green'] * 3) + (df['ska_blue'] * 1) ) / 36)
    df.ska= df.ska.round(1)
        


    # calculates Ball_playing_defender_Defend score
    df['bpdd_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['bpdd_green'] = ( df['Hea'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Str'] )
    df['bpdd_blue'] = ( df['Fir'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] + df['Vis'] )
    df['bpdd'] =( ( ( df['bpdd_key'] * 5) + (df['bpdd_green'] * 3) + (df['bpdd_blue'] * 1) ) / 46)
    df.bpdd= df.bpdd.round(1)
        


    # calculates Ball_playing_defender_Stopper score
    df['bpds_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['bpds_green'] = ( df['Hea'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Str'] + df['Agg'] + df['Bra'] + df['Dec'] )
    df['bpds_blue'] = ( df['Fir'] + df['Tec'] + df['Ant'] + df['Cnt'] + df['Vis'] + df['Mar'] )
    df['bpds'] =( ( ( df['bpds_key'] * 5) + (df['bpds_green'] * 3) + (df['bpds_blue'] * 1) ) / 50)
    df.bpds= df.bpds.round(1)
        


    # calculates Ball_playing_defender_Cover score
    df['bpdc_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['bpdc_green'] = ( df['Mar'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Ant'] + df['Cnt'] + df['Dec'] )
    df['bpdc_blue'] = ( df['Fir'] + df['Tec'] + df['Bra'] + df['Vis'] + df['Str'] + df['Hea'] )
    df['bpdc'] =( ( ( df['bpdc_key'] * 5) + (df['bpdc_green'] * 3) + (df['bpdc_blue'] * 1) ) / 47)
    df.bpdc= df.bpdc.round(1)
        


    # calculates Central_defender_Defend score
    df['cdd_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['cdd_green'] = ( df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'] )
    df['cdd_blue'] = ( df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] )
    df['cdd'] =( ( ( df['cdd_key'] * 5) + (df['cdd_green'] * 3) + (df['cdd_blue'] * 1) ) / 40)
    df.cdd= df.cdd.round(1)
        


    # calculates Central_defender_Stopper score
    df['cds_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['cds_green'] = ( df['Hea'] + df['Tck'] + df['Agg'] + df['Bra'] + df['Dec'] + df['Pos'] + df['Str'] )
    df['cds_blue'] = ( df['Mar'] + df['Ant'] + df['Cnt'] )
    df['cds'] =( ( ( df['cds_key'] * 5) + (df['cds_green'] * 3) + (df['cds_blue'] * 1) ) / 44)
    df.cds= df.cds.round(1)
        


    # calculates Central_defender_Cover score
    df['cdc_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['cdc_green'] = ( df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Pos'] )
    df['cdc_blue'] = ( df['Hea'] + df['Bra'] + df['Str'] )
    df['cdc'] =( ( ( df['cdc_key'] * 5) + (df['cdc_green'] * 3) + (df['cdc_blue'] * 1) ) / 41)
    df.cdc= df.cdc.round(1)
        


    # calculates Complete_wing_back_Support score
    df['cwbs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['cwbs_green'] = ( df['Cro'] + df['Dri'] + df['Tec'] + df['OtB'] + df['Tea'] )
    df['cwbs_blue'] = ( df['Fir'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Ant'] + df['Dec'] + df['Fla'] + df['Pos'] + df['Agi'] + df['Bal'] )
    df['cwbs'] =( ( ( df['cwbs_key'] * 5) + (df['cwbs_green'] * 3) + (df['cwbs_blue'] * 1) ) / 45)
    df.cwbs= df.cwbs.round(1)
        


    # calculates Complete_wing_back_Attack score
    df['cwba_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['cwba_green'] = ( df['Cro'] + df['Dri'] + df['Tec'] + df['Fla'] + df['OtB'] + df['Tea'] )
    df['cwba_blue'] = ( df['Fir'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Ant'] + df['Dec'] + df['Pos'] + df['Agi'] + df['Bal'] )
    df['cwba'] =( ( ( df['cwba_key'] * 5) + (df['cwba_green'] * 3) + (df['cwba_blue'] * 1) ) / 47)
    df.cwba= df.cwba.round(1)
        


    # calculates Full_back_Defend score
    df['fbd_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['fbd_green'] = ( df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Pos'] )
    df['fbd_blue'] = ( df['Cro'] + df['Pas'] + df['Dec'] + df['Tea'] )
    df['fbd'] =( ( ( df['fbd_key'] * 5) + (df['fbd_green'] * 3) + (df['fbd_blue'] * 1) ) / 42)
    df.fbd= df.fbd.round(1)
        


    # calculates Full_back_Support score
    df['fbs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['fbs_green'] = ( df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Tea'] )
    df['fbs_blue'] = ( df['Cro'] + df['Dri'] + df['Pas'] + df['Tec'] + df['Dec'] )
    df['fbs'] =( ( ( df['fbs_key'] * 5) + (df['fbs_green'] * 3) + (df['fbs_blue'] * 1) ) / 43)
    df.fbs= df.fbs.round(1)
        


    # calculates Full_back_Attack score
    df['fba_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['fba_green'] = ( df['Cro'] + df['Mar'] + df['Tck'] + df['Ant'] + df['Pos'] + df['Tea'] )
    df['fba_blue'] = ( df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cnt'] + df['Dec'] + df['OtB'] + df['Agi'] )
    df['fba'] =( ( ( df['fba_key'] * 5) + (df['fba_green'] * 3) + (df['fba_blue'] * 1) ) / 46)
    df.fba= df.fba.round(1)
        


    # calculates Inverted_full_back_Defend score
    df['ifbd_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['ifbd_green'] = ( df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'] )
    df['ifbd_blue'] = ( df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Agi'] + df['Jum'] )
    df['ifbd'] =( ( ( df['ifbd_key'] * 5) + (df['ifbd_green'] * 3) + (df['ifbd_blue'] * 1) ) / 47)
    df.ifbd= df.ifbd.round(1)
        


    # calculates Inverted_wing_back_Defend score
    df['iwbd_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['iwbd_green'] = ( df['Pas'] + df['Tck'] + df['Ant'] + df['Dec'] + df['Pos'] + df['Tea'] )
    df['iwbd_blue'] = ( df['Fir'] + df['Mar'] + df['Tec'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Agi'] )
    df['iwbd'] =( ( ( df['iwbd_key'] * 5) + (df['iwbd_green'] * 3) + (df['iwbd_blue'] * 1) ) / 45)
    df.iwbd= df.iwbd.round(1)
        


    # calculates Inverted_wing_back_Support score
    df['iwbs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['iwbs_green'] = ( df['Fir'] + df['Pas'] + df['Tck'] + df['Cmp'] + df['Dec'] + df['Tea'] )
    df['iwbs_blue'] = ( df['Mar'] + df['Tec'] + df['Ant'] + df['Cnt'] + df['OtB'] + df['Pos'] + df['Vis'] + df['Agi'] )
    df['iwbs'] =( ( ( df['iwbs_key'] * 5) + (df['iwbs_green'] * 3) + (df['iwbs_blue'] * 1) ) / 46)
    df.iwbs= df.iwbs.round(1)
        


    # calculates Inverted_wing_back_Attack score
    df['iwba_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['iwba_green'] = ( df['Fir'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Vis'] )
    df['iwba_blue'] = ( df['Cro'] + df['Dri'] + df['Lon'] + df['Mar'] + df['Ant'] + df['Cnt'] + df['Fla'] + df['Pos'] + df['Agi'] )
    df['iwba'] =( ( ( df['iwba_key'] * 5) + (df['iwba_green'] * 3) + (df['iwba_blue'] * 1) ) / 56)
    df.iwba= df.iwba.round(1)
        


    # calculates Libero_Defend score
    df['ld_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['ld_green'] = ( df['Fir'] + df['Hea'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Dec'] + df['Pos'] + df['Tea'] + df['Str'] )
    df['ld_blue'] = ( df['Ant'] + df['Bra'] + df['Cnt'] + df['Sta'] )
    df['ld'] =( ( ( df['ld_key'] * 5) + (df['ld_green'] * 3) + (df['ld_blue'] * 1) ) / 54)
    df.ld= df.ld.round(1)
        


    # calculates Libero_Support score
    df['ls_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['ls_green'] = ( df['Fir'] + df['Hea'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Dec'] + df['Pos'] + df['Tea'] + df['Str'] )
    df['ls_blue'] = ( df['Dri'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Vis'] + df['Sta'] )
    df['ls'] =( ( ( df['ls_key'] * 5) + (df['ls_green'] * 3) + (df['ls_blue'] * 1) ) / 56)
    df.ls= df.ls.round(1)
        


    # calculates No-nonsense_centre_back_Defend score
    df['ncbd_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['ncbd_green'] = ( df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'] )
    df['ncbd_blue'] = ( df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] )
    df['ncbd'] =( ( ( df['ncbd_key'] * 5) + (df['ncbd_green'] * 3) + (df['ncbd_blue'] * 1) ) / 39)
    df.ncbd= df.ncbd.round(1)
        


    # calculates No-nonsense_centre_back_Stopper score
    df['ncbs_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['ncbs_green'] = ( df['Hea'] + df['Tck'] + df['Agg'] + df['Bra'] + df['Pos'] + df['Str'] )
    df['ncbs_blue'] = ( df['Mar'] + df['Ant'] + df['Cnt'] )
    df['ncbs'] =( ( ( df['ncbs_key'] * 5) + (df['ncbs_green'] * 3) + (df['ncbs_blue'] * 1) ) / 41)
    df.ncbs= df.ncbs.round(1)
        


    # calculates No-nonsense_centre_back_Cover score
    df['ncbc_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['ncbc_green'] = ( df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] )
    df['ncbc_blue'] = ( df['Hea'] + df['Bra'] + df['Str'] )
    df['ncbc'] =( ( ( df['ncbc_key'] * 5) + (df['ncbc_green'] * 3) + (df['ncbc_blue'] * 1) ) / 38)
    df.ncbc= df.ncbc.round(1)
        


    # calculates No-nonsense_full_back_Defend score
    df['nfbd_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['nfbd_green'] = ( df['Mar'] + df['Tck'] + df['Ant'] + df['Pos'] + df['Str'] )
    df['nfbd_blue'] = ( df['Hea'] + df['Agg'] + df['Bra'] + df['Cnt'] + df['Tea'] )
    df['nfbd'] =( ( ( df['nfbd_key'] * 5) + (df['nfbd_green'] * 3) + (df['nfbd_blue'] * 1) ) / 40)
    df.nfbd= df.nfbd.round(1)
        


    # calculates Wide_centre_back_Defend score
    df['wcbd_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['wcbd_green'] = ( df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'] )
    df['wcbd_blue'] = ( df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] + df['Wor'] + df['Agi'] )
    df['wcbd'] =( ( ( df['wcbd_key'] * 5) + (df['wcbd_green'] * 3) + (df['wcbd_blue'] * 1) ) / 46)
    df.wcbd= df.wcbd.round(1)
        


    # calculates Wide_centre_back_Support score
    df['wcbs_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['wcbs_green'] = ( df['Dri'] + df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'] )
    df['wcbs_blue'] = ( df['Cro'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] + df['OtB'] + df['Wor'] + df['Agi'] + df['Sta'] )
    df['wcbs'] =( ( ( df['wcbs_key'] * 5) + (df['wcbs_green'] * 3) + (df['wcbs_blue'] * 1) ) / 51)
    df.wcbs= df.wcbs.round(1)
        


    # calculates Wide_centre_back_Attack score
    df['wcba_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
    df['wcba_green'] = ( df['Cro'] + df['Dri'] + df['Hea'] + df['Mar'] + df['Tck'] + df['OtB'] + df['Sta'] + df['Str'] )
    df['wcba_blue'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Wor'] + df['Agi'] )
    df['wcba'] =( ( ( df['wcba_key'] * 5) + (df['wcba_green'] * 3) + (df['wcba_blue'] * 1) ) / 55)
    df.wcba= df.wcba.round(1)
        


    # calculates Wing_back_Defend score
    df['wbd_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wbd_green'] = ( df['Mar'] + df['Tck'] + df['Ant'] + df['Pos'] + df['Tea'] )
    df['wbd_blue'] = ( df['Cro'] + df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cnt'] + df['Dec'] + df['OtB'] + df['Agi'] + df['Bal'] )
    df['wbd'] =( ( ( df['wbd_key'] * 5) + (df['wbd_green'] * 3) + (df['wbd_blue'] * 1) ) / 45)
    df.wbd= df.wbd.round(1)
        


    # calculates Wing_back_Support score
    df['wbs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wbs_green'] = ( df['Cro'] + df['Dri'] + df['Mar'] + df['Tck'] + df['OtB'] + df['Tea'] )
    df['wbs_blue'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Agi'] + df['Bal'] )
    df['wbs'] =( ( ( df['wbs_key'] * 5) + (df['wbs_green'] * 3) + (df['wbs_blue'] * 1) ) / 47)
    df.wbs= df.wbs.round(1)
        


    # calculates Wing_back_Attack score
    df['wba_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wba_green'] = ( df['Cro'] + df['Dri'] + df['Tck'] + df['Tec'] + df['OtB'] + df['Tea'] )
    df['wba_blue'] = ( df['Fir'] + df['Mar'] + df['Pas'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Fla'] + df['Pos'] + df['Agi'] + df['Bal'] )
    df['wba'] =( ( ( df['wba_key'] * 5) + (df['wba_green'] * 3) + (df['wba_blue'] * 1) ) / 48)
    df.wba= df.wba.round(1)
        


    # calculates Advanced_playmaker_Support score
    df['aps_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['aps_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Vis'] )
    df['aps_blue'] = ( df['Dri'] + df['Ant'] + df['Fla'] + df['Agi'] )
    df['aps'] =( ( ( df['aps_key'] * 5) + (df['aps_green'] * 3) + (df['aps_blue'] * 1) ) / 48)
    df.aps= df.aps.round(1)
        


    # calculates Advanced_playmaker_Attack score
    df['apa_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['apa_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Vis'] )
    df['apa_blue'] = ( df['Dri'] + df['Ant'] + df['Fla'] + df['Agi'] )
    df['apa'] =( ( ( df['apa_key'] * 5) + (df['apa_green'] * 3) + (df['apa_blue'] * 1) ) / 48)
    df.apa= df.apa.round(1)
        


    # calculates Anchor_Defend score
    df['ad_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['ad_green'] = ( df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Pos'] )
    df['ad_blue'] = ( df['Cmp'] + df['Tea'] + df['Str'] )
    df['ad'] =( ( ( df['ad_key'] * 5) + (df['ad_green'] * 3) + (df['ad_blue'] * 1) ) / 41)
    df.ad= df.ad.round(1)
        


    # calculates Attacking_midfielder_Support score
    df['ams_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['ams_green'] = ( df['Fir'] + df['Lon'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Dec'] + df['Fla'] + df['OtB'] )
    df['ams_blue'] = ( df['Dri'] + df['Cmp'] + df['Vis'] + df['Agi'] )
    df['ams'] =( ( ( df['ams_key'] * 5) + (df['ams_green'] * 3) + (df['ams_blue'] * 1) ) / 48)
    df.ams= df.ams.round(1)
        


    # calculates Attacking_midfielder_Attack score
    df['ama_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['ama_green'] = ( df['Dri'] + df['Fir'] + df['Lon'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Dec'] + df['Fla'] + df['OtB'] )
    df['ama_blue'] = ( df['Fin'] + df['Cmp'] + df['Vis'] + df['Agi'] )
    df['ama'] =( ( ( df['ama_key'] * 5) + (df['ama_green'] * 3) + (df['ama_blue'] * 1) ) / 51)
    df.ama= df.ama.round(1)
        


    # calculates Ball_winning_midfielder_Defend score
    df['bwmd_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['bwmd_green'] = ( df['Tck'] + df['Agg'] + df['Ant'] + df['Tea'] )
    df['bwmd_blue'] = ( df['Mar'] + df['Bra'] + df['Cnt'] + df['Pos'] + df['Agi'] + df['Str'] )
    df['bwmd'] =( ( ( df['bwmd_key'] * 5) + (df['bwmd_green'] * 3) + (df['bwmd_blue'] * 1) ) / 38)
    df.bwmd= df.bwmd.round(1)
        


    # calculates Ball_winning_midfielder_Support score
    df['bwms_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['bwms_green'] = ( df['Tck'] + df['Agg'] + df['Ant'] + df['Tea'] )
    df['bwms_blue'] = ( df['Mar'] + df['Pas'] + df['Bra'] + df['Cnt'] + df['Agi'] + df['Str'] )
    df['bwms'] =( ( ( df['bwms_key'] * 5) + (df['bwms_green'] * 3) + (df['bwms_blue'] * 1) ) / 38)
    df.bwms= df.bwms.round(1)
        


    # calculates Box_to_box_midfielder_Support score
    df['b2bs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['b2bs_green'] = ( df['Pas'] + df['Tck'] + df['OtB'] + df['Tea'] )
    df['b2bs_blue'] = ( df['Dri'] + df['Fin'] + df['Fir'] + df['Lon'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['Pos'] + df['Bal'] + df['Str'] )
    df['b2bs'] =( ( ( df['b2bs_key'] * 5) + (df['b2bs_green'] * 3) + (df['b2bs_blue'] * 1) ) / 44)
    df.b2bs= df.b2bs.round(1)
        


    # calculates Carrilero_Support score
    df['cars_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['cars_green'] = ( df['Fir'] + df['Pas'] + df['Tck'] + df['Dec'] + df['Pos'] + df['Tea'] )
    df['cars_blue'] = ( df['Tec'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Vis'] )
    df['cars'] =( ( ( df['cars_key'] * 5) + (df['cars_green'] * 3) + (df['cars_blue'] * 1) ) / 44)
    df.cars= df.cars.round(1)
        


    # calculates Central_midfielder_Defend score
    df['cmd_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['cmd_green'] = ( df['Tck'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Tea'] )
    df['cmd_blue'] = ( df['Fir'] + df['Mar'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Cmp'] )
    df['cmd'] =( ( ( df['cmd_key'] * 5) + (df['cmd_green'] * 3) + (df['cmd_blue'] * 1) ) / 42)
    df.cmd= df.cmd.round(1)
        


    # calculates Central_midfielder_Support score
    df['cms_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['cms_green'] = ( df['Fir'] + df['Pas'] + df['Tck'] + df['Dec'] + df['Tea'] )
    df['cms_blue'] = ( df['Tec'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Vis'] )
    df['cms'] =( ( ( df['cms_key'] * 5) + (df['cms_green'] * 3) + (df['cms_blue'] * 1) ) / 41)
    df.cms= df.cms.round(1)
        


    # calculates Central_midfielder_Attack score
    df['cma_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['cma_green'] = ( df['Fir'] + df['Pas'] + df['Dec'] + df['OtB'] )
    df['cma_blue'] = ( df['Lon'] + df['Tck'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['Tea'] + df['Vis'] )
    df['cma'] =( ( ( df['cma_key'] * 5) + (df['cma_green'] * 3) + (df['cma_blue'] * 1) ) / 39)
    df.cma= df.cma.round(1)
        


    # calculates Deep_lying_playmaker_Defend score
    df['dlpd_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['dlpd_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Tea'] + df['Vis'] )
    df['dlpd_blue'] = ( df['Tck'] + df['Ant'] + df['Pos'] + df['Bal'] )
    df['dlpd'] =( ( ( df['dlpd_key'] * 5) + (df['dlpd_green'] * 3) + (df['dlpd_blue'] * 1) ) / 45)
    df.dlpd= df.dlpd.round(1)
        


    # calculates Deep_lying_playmaker_Support score
    df['dlps_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['dlps_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Tea'] + df['Vis'] )
    df['dlps_blue'] = ( df['Ant'] + df['OtB'] + df['Pos'] + df['Bal'] )
    df['dlps'] =( ( ( df['dlps_key'] * 5) + (df['dlps_green'] * 3) + (df['dlps_blue'] * 1) ) / 45)
    df.dlps= df.dlps.round(1)
        


    # calculates Defensive_midfielder_Defend score
    df['dmd_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['dmd_green'] = ( df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Tea'] )
    df['dmd_blue'] = ( df['Mar'] + df['Pas'] + df['Agg'] + df['Cmp'] + df['Str'] + df['Dec'] )
    df['dmd'] =( ( ( df['dmd_key'] * 5) + (df['dmd_green'] * 3) + (df['dmd_blue'] * 1) ) / 41)
    df.dmd= df.dmd.round(1)
        


    # calculates Defensive_midfielder_Support score
    df['dms_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['dms_green'] = ( df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Tea'] )
    df['dms_blue'] = ( df['Fir'] + df['Mar'] + df['Pas'] + df['Agg'] + df['Cmp'] + df['Dec'] + df['Str'] )
    df['dms'] =( ( ( df['dms_key'] * 5) + (df['dms_green'] * 3) + (df['dms_blue'] * 1) ) / 42)
    df.dms= df.dms.round(1)
        


    # calculates Defensive_winger_Defend score
    df['dwd_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['dwd_green'] = ( df['Tec'] + df['Ant'] + df['OtB'] + df['Pos'] + df['Tea'] )
    df['dwd_blue'] = ( df['Cro'] + df['Dri'] + df['Fir'] + df['Mar'] + df['Tck'] + df['Agg'] + df['Cnt'] + df['Dec'] )
    df['dwd'] =( ( ( df['dwd_key'] * 5) + (df['dwd_green'] * 3) + (df['dwd_blue'] * 1) ) / 43)
    df.dwd= df.dwd.round(1)
        


    # calculates Defensive_winger_Support score
    df['dws_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['dws_green'] = ( df['Cro'] + df['Pas'] + df['Tec'] + df['OtB'] + df['Tea'] )
    df['dws_blue'] = ( df['Dri'] + df['Fir'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Agg'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Pos'] )
    df['dws'] =( ( ( df['dws_key'] * 5) + (df['dws_green'] * 3) + (df['dws_blue'] * 1) ) / 46)
    df.dws= df.dws.round(1)
        


    # calculates Enganche_Support score
    df['engs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['engs_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Vis'] )
    df['engs_blue'] = ( df['Dri'] + df['Ant'] + df['Fla'] + df['OtB'] + df['Tea'] + df['Agi'] )
    df['engs'] =( ( ( df['engs_key'] * 5) + (df['engs_green'] * 3) + (df['engs_blue'] * 1) ) / 44)
    df.engs= df.engs.round(1)
        


    # calculates Half_back_Defend score
    df['hbd_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['hbd_green'] = ( df['Mar'] + df['Tck'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Tea'] )
    df['hbd_blue'] = ( df['Fir'] + df['Pas'] + df['Agg'] + df['Bra'] + df['Jum'] + df['Str'] )
    df['hbd'] =( ( ( df['hbd_key'] * 5) + (df['hbd_green'] * 3) + (df['hbd_blue'] * 1) ) / 50)
    df.hbd= df.hbd.round(1)
        


    # calculates Inside_forward_Support score
    df['ifs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['ifs_green'] = ( df['Dri'] + df['Fin'] + df['Fir'] + df['Tec'] + df['OtB'] + df['Agi'] )
    df['ifs_blue'] = ( df['Lon'] + df['Pas'] + df['Ant'] + df['Cmp'] + df['Fla'] + df['Vis'] + df['Bal'] )
    df['ifs'] =( ( ( df['ifs_key'] * 5) + (df['ifs_green'] * 3) + (df['ifs_blue'] * 1) ) / 45)
    df.ifs= df.ifs.round(1)
        


    # calculates Inside_forward_Attack score
    df['ifa_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['ifa_green'] = ( df['Dri'] + df['Fin'] + df['Fir'] + df['Tec'] + df['Ant'] + df['OtB'] + df['Agi'] )
    df['ifa_blue'] = ( df['Lon'] + df['Pas'] + df['Cmp'] + df['Fla'] + df['Bal'] )
    df['ifa'] =( ( ( df['ifa_key'] * 5) + (df['ifa_green'] * 3) + (df['ifa_blue'] * 1) ) / 46)
    df.ifa= df.ifa.round(1)
        


    # calculates Inverted_winger_Support score
    df['iws_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['iws_green'] = ( df['Cro'] + df['Dri'] + df['Pas'] + df['Tec'] + df['Agi'] )
    df['iws_blue'] = ( df['Fir'] + df['Lon'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Vis'] + df['Bal'] )
    df['iws'] =( ( ( df['iws_key'] * 5) + (df['iws_green'] * 3) + (df['iws_blue'] * 1) ) / 42)
    df.iws= df.iws.round(1)
        


    # calculates Inverted_winger_Attack score
    df['iwa_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['iwa_green'] = ( df['Cro'] + df['Dri'] + df['Pas'] + df['Tec'] + df['Agi'] )
    df['iwa_blue'] = ( df['Fir'] + df['Lon'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Vis'] + df['Bal'] )
    df['iwa'] =( ( ( df['iwa_key'] * 5) + (df['iwa_green'] * 3) + (df['iwa_blue'] * 1) ) / 44)
    df.iwa= df.iwa.round(1)
        


    # calculates Mezzala_Support score
    df['mezs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['mezs_green'] = ( df['Pas'] + df['Tec'] + df['Dec'] + df['OtB'] )
    df['mezs_blue'] = ( df['Dri'] + df['Fir'] + df['Lon'] + df['Tck'] + df['Ant'] + df['Cmp'] + df['Vis'] + df['Bal'] )
    df['mezs'] =( ( ( df['mezs_key'] * 5) + (df['mezs_green'] * 3) + (df['mezs_blue'] * 1) ) / 40)
    df.mezs= df.mezs.round(1)
        


    # calculates Mezzala_Attack score
    df['meza_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['meza_green'] = ( df['Dri'] + df['Pas'] + df['Tec'] + df['Dec'] + df['OtB'] + df['Vis'] )
    df['meza_blue'] = ( df['Fin'] + df['Fir'] + df['Lon'] + df['Ant'] + df['Cmp'] + df['Fla'] + df['Bal'] )
    df['meza'] =( ( ( df['meza_key'] * 5) + (df['meza_green'] * 3) + (df['meza_blue'] * 1) ) / 45)
    df.meza= df.meza.round(1)
        


    # calculates Raumdeuter_Attack score
    df['raua_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['raua_green'] = ( df['Fin'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['OtB'] + df['Bal'] )
    df['raua_blue'] = ( df['Fir'] + df['Tec'] )
    df['raua'] =( ( ( df['raua_key'] * 5) + (df['raua_green'] * 3) + (df['raua_blue'] * 1) ) / 43)
    df.raua= df.raua.round(1)
        


    # calculates Regista_Support score
    df['regs_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['regs_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Tea'] + df['Vis'] )
    df['regs_blue'] = ( df['Dri'] + df['Lon'] + df['Ant'] + df['Bal'] )
    df['regs'] =( ( ( df['regs_key'] * 5) + (df['regs_green'] * 3) + (df['regs_blue'] * 1) ) / 51)
    df.regs= df.regs.round(1)
        


    # calculates Roaming_playmaker_Support score
    df['rps_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['rps_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Vis'] )
    df['rps_blue'] = ( df['Dri'] + df['Lon'] + df['Cnt'] + df['Pos'] + df['Agi'] + df['Bal'] )
    df['rps'] =( ( ( df['rps_key'] * 5) + (df['rps_green'] * 3) + (df['rps_blue'] * 1) ) / 53)
    df.rps= df.rps.round(1)
        


    # calculates Segundo_volante_Support score
    df['svs_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['svs_green'] = ( df['Mar'] + df['Pas'] + df['Tck'] + df['OtB'] + df['Pos'] )
    df['svs_blue'] = ( df['Fin'] + df['Fir'] + df['Lon'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Bal'] + df['Str'] )
    df['svs'] =( ( ( df['svs_key'] * 5) + (df['svs_green'] * 3) + (df['svs_blue'] * 1) ) / 44)
    df.svs= df.svs.round(1)
        


    # calculates Segundo_volante_Attack score
    df['sva_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
    df['sva_green'] = ( df['Fin'] + df['Lon'] + df['Pas'] + df['Tck'] + df['Ant'] + df['OtB'] + df['Pos'] )
    df['sva_blue'] = ( df['Fir'] + df['Mar'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Bal'] )
    df['sva'] =( ( ( df['sva_key'] * 5) + (df['sva_green'] * 3) + (df['sva_blue'] * 1) ) / 47)
    df.sva= df.sva.round(1)
        


    # calculates Shadow_striker_Attack score
    df['ssa_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['ssa_green'] = ( df['Dri'] + df['Fin'] + df['Fir'] + df['Ant'] + df['Cmp'] + df['OtB'] )
    df['ssa_blue'] = ( df['Pas'] + df['Tec'] + df['Cnt'] + df['Dec'] + df['Agi'] + df['Bal'] )
    df['ssa'] =( ( ( df['ssa_key'] * 5) + (df['ssa_green'] * 3) + (df['ssa_blue'] * 1) ) / 44)
    df.ssa= df.ssa.round(1)
        


    # calculates Wide_midfielder_Defend score
    df['wmd_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wmd_green'] = ( df['Pas'] + df['Tck'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Tea'] )
    df['wmd_blue'] = ( df['Cro'] + df['Fir'] + df['Mar'] + df['Tec'] + df['Ant'] + df['Cmp'] )
    df['wmd'] =( ( ( df['wmd_key'] * 5) + (df['wmd_green'] * 3) + (df['wmd_blue'] * 1) ) / 44)
    df.wmd= df.wmd.round(1)
        


    # calculates Wide_midfielder_Support score
    df['wms_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wms_green'] = ( df['Pas'] + df['Tck'] + df['Dec'] + df['Tea'] )
    df['wms_blue'] = ( df['Cro'] + df['Fir'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Pos'] + df['Vis'] )
    df['wms'] =( ( ( df['wms_key'] * 5) + (df['wms_green'] * 3) + (df['wms_blue'] * 1) ) / 41)
    df.wms= df.wms.round(1)
        


    # calculates Wide_midfielder_Attack score
    df['wma_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wma_green'] = ( df['Cro'] + df['Fir'] + df['Pas'] + df['Dec'] + df['Tea'] )
    df['wma_blue'] = ( df['Tck'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['OtB'] + df['Vis'] )
    df['wma'] =( ( ( df['wma_key'] * 5) + (df['wma_green'] * 3) + (df['wma_blue'] * 1) ) / 41)
    df.wma= df.wma.round(1)
        


    # calculates Wide_playmaker_Support score
    df['wps_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wps_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Tea'] + df['Vis'] )
    df['wps_blue'] = ( df['Dri'] + df['OtB'] + df['Agi'] )
    df['wps'] =( ( ( df['wps_key'] * 5) + (df['wps_green'] * 3) + (df['wps_blue'] * 1) ) / 44)
    df.wps= df.wps.round(1)
        


    # calculates Wide_playmaker_Attack score
    df['wpa_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wpa_green'] = ( df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Vis'] )
    df['wpa_blue'] = ( df['Ant'] + df['Fla'] + df['Agi'] )
    df['wpa'] =( ( ( df['wpa_key'] * 5) + (df['wpa_green'] * 3) + (df['wpa_blue'] * 1) ) / 50)
    df.wpa= df.wpa.round(1)
        


    # calculates Wide_target_forward_Support score
    df['wtfs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wtfs_green'] = ( df['Hea'] + df['Bra'] + df['Tea'] + df['Jum'] + df['Str'] )
    df['wtfs_blue'] = ( df['Cro'] + df['Fir'] + df['Ant'] + df['OtB'] + df['Bal'] )
    df['wtfs'] =( ( ( df['wtfs_key'] * 5) + (df['wtfs_green'] * 3) + (df['wtfs_blue'] * 1) ) / 40)
    df.wtfs= df.wtfs.round(1)
        


    # calculates Wide_target_forward_Attack score
    df['wtfa_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wtfa_green'] = ( df['Hea'] + df['Bra'] + df['OtB'] + df['Jum'] + df['Str'] )
    df['wtfa_blue'] = ( df['Cro'] + df['Fin'] + df['Fir'] + df['Ant'] + df['Tea'] + df['Bal'] )
    df['wtfa'] =( ( ( df['wtfa_key'] * 5) + (df['wtfa_green'] * 3) + (df['wtfa_blue'] * 1) ) / 41)
    df.wtfa= df.wtfa.round(1)
        


    # calculates Winger_Support score
    df['ws_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['ws_green'] = ( df['Cro'] + df['Dri'] + df['Tec'] + df['Agi'] )
    df['ws_blue'] = ( df['Fir'] + df['Pas'] + df['OtB'] + df['Bal'] )
    df['ws'] =( ( ( df['ws_key'] * 5) + (df['ws_green'] * 3) + (df['ws_blue'] * 1) ) / 36)
    df.ws= df.ws.round(1)
        


    # calculates Winger_Attack score
    df['wa_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
    df['wa_green'] = ( df['Cro'] + df['Dri'] + df['Tec'] + df['Agi'] )
    df['wa_blue'] = ( df['Fir'] + df['Pas'] + df['Ant'] + df['Fla'] + df['OtB'] + df['Bal'] )
    df['wa'] =( ( ( df['wa_key'] * 5) + (df['wa_green'] * 3) + (df['wa_blue'] * 1) ) / 38)
    df.wa= df.wa.round(1)
        


    # calculates Advanced_forward_Attack score
    df['afa_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['afa_green'] = ( df['Dri'] + df['Fir'] + df['Tec'] + df['Cmp'] + df['OtB'] )
    df['afa_blue'] = ( df['Pas'] + df['Ant'] + df['Dec'] + df['Wor'] + df['Agi'] + df['Bal'] + df['Sta'] )
    df['afa'] =( ( ( df['afa_key'] * 5) + (df['afa_green'] * 3) + (df['afa_blue'] * 1) ) / 37)
    df.afa= df.afa.round(1)
        


    # calculates Complete_forward_Support score
    df['cfs_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['cfs_green'] = ( df['Dri'] + df['Fir'] + df['Hea'] + df['Lon'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Vis'] + df['Agi'] + df['Str'] )
    df['cfs_blue'] = ( df['Tea'] + df['Wor'] + df['Bal'] + df['Jum'] + df['Sta'] )
    df['cfs'] =( ( ( df['cfs_key'] * 5) + (df['cfs_green'] * 3) + (df['cfs_blue'] * 1) ) / 59)
    df.cfs= df.cfs.round(1)
        


    # calculates Complete_forward_Attack score
    df['cfa_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['cfa_green'] = ( df['Dri'] + df['Fir'] + df['Hea'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['OtB'] + df['Agi'] + df['Str'] )
    df['cfa_blue'] = ( df['Lon'] + df['Pas'] + df['Dec'] + df['Tea'] + df['Vis'] + df['Wor'] + df['Bal'] + df['Jum'] + df['Sta'] )
    df['cfa'] =( ( ( df['cfa_key'] * 5) + (df['cfa_green'] * 3) + (df['cfa_blue'] * 1) ) / 51)
    df.cfa= df.cfa.round(1)
        


    # calculates Deep_lying_forward_Support score
    df['dlfs_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['dlfs_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] )
    df['dlfs_blue'] = ( df['Ant'] + df['Fla'] + df['Vis'] + df['Bal'] + df['Str'] )
    df['dlfs'] =( ( ( df['dlfs_key'] * 5) + (df['dlfs_green'] * 3) + (df['dlfs_blue'] * 1) ) / 41)
    df.dlfs= df.dlfs.round(1)
        


    # calculates Deep_lying_forward_Attack score
    df['dlfa_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['dlfa_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] )
    df['dlfa_blue'] = ( df['Dri'] + df['Ant'] + df['Fla'] + df['Vis'] + df['Bal'] + df['Str'] )
    df['dlfa'] =( ( ( df['dlfa_key'] * 5) + (df['dlfa_green'] * 3) + (df['dlfa_blue'] * 1) ) / 42)
    df.dlfa= df.dlfa.round(1)
        


    # calculates False_nine_Support score
    df['f9s_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['f9s_green'] = ( df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Vis'] + df['Agi'] )
    df['f9s_blue'] = ( df['Ant'] + df['Fla'] + df['Tea'] + df['Bal'] )
    df['f9s'] =( ( ( df['f9s_key'] * 5) + (df['f9s_green'] * 3) + (df['f9s_blue'] * 1) ) / 46)
    df.f9s= df.f9s.round(1)
        


    # calculates Poacher_Attack score
    df['pa_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['pa_green'] = ( df['Ant'] + df['Cmp'] + df['OtB'] )
    df['pa_blue'] = ( df['Fir'] + df['Hea'] + df['Tec'] + df['Dec'] )
    df['pa'] =( ( ( df['pa_key'] * 5) + (df['pa_green'] * 3) + (df['pa_blue'] * 1) ) / 28)
    df.pa= df.pa.round(1)
        


    # calculates Pressing_forward_Defend score
    df['pfd_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['pfd_green'] = ( df['Agg'] + df['Ant'] + df['Bra'] + df['Dec'] + df['Tea'] + df['Wor'] + df['Sta'] )
    df['pfd_blue'] = ( df['Fir'] + df['Cmp'] + df['Cnt'] + df['Agi'] + df['Bal'] + df['Str'] )
    df['pfd'] =( ( ( df['pfd_key'] * 5) + (df['pfd_green'] * 3) + (df['pfd_blue'] * 1) ) / 42)
    df.pfd= df.pfd.round(1)
        


    # calculates Pressing_forward_Support score
    df['pfs_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['pfs_green'] = ( df['Agg'] + df['Ant'] + df['Bra'] + df['Dec'] + df['Tea'] + df['Wor'] + df['Sta'] )
    df['pfs_blue'] = ( df['Fir'] + df['Pas'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Agi'] + df['Bal'] + df['Str'] )
    df['pfs'] =( ( ( df['pfs_key'] * 5) + (df['pfs_green'] * 3) + (df['pfs_blue'] * 1) ) / 44)
    df.pfs= df.pfs.round(1)
        


    # calculates Pressing_forward_Attack score
    df['pfa_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['pfa_green'] = ( df['Agg'] + df['Ant'] + df['Bra'] + df['OtB'] + df['Tea'] + df['Wor'] + df['Sta'] )
    df['pfa_blue'] = ( df['Fir'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Agi'] + df['Bal'] + df['Str'] )
    df['pfa'] =( ( ( df['pfa_key'] * 5) + (df['pfa_green'] * 3) + (df['pfa_blue'] * 1) ) / 43)
    df.pfa= df.pfa.round(1)
        


    # calculates Target_forward_Support score
    df['tfs_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['tfs_green'] = ( df['Hea'] + df['Bra'] + df['Tea'] + df['Bal'] + df['Jum'] + df['Str'] )
    df['tfs_blue'] = ( df['Fir'] + df['Agg'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['OtB'] )
    df['tfs'] =( ( ( df['tfs_key'] * 5) + (df['tfs_green'] * 3) + (df['tfs_blue'] * 1) ) / 39)
    df.tfs= df.tfs.round(1)
        


    # calculates Target_forward_Attack score
    df['tfa_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['tfa_green'] = ( df['Hea'] + df['Bra'] + df['Cmp'] + df['OtB'] + df['Bal'] + df['Jum'] + df['Str'] )
    df['tfa_blue'] = ( df['Fir'] + df['Agg'] + df['Ant'] + df['Dec'] + df['Tea'] )
    df['tfa'] =( ( ( df['tfa_key'] * 5) + (df['tfa_green'] * 3) + (df['tfa_blue'] * 1) ) / 41)
    df.tfa= df.tfa.round(1)
        


    # calculates Trequartista_Attack score
    df['trea_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
    df['trea_green'] = ( df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Vis'] )
    df['trea_blue'] = ( df['Ant'] + df['Agi'] + df['Bal'] )
    df['trea'] =( ( ( df['trea_key'] * 5) + (df['trea_green'] * 3) + (df['trea_blue'] * 1) ) / 45)
    df.trea= df.trea.round(1)