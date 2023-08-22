import pandas as pd
import requests
import openpyxl
from Defensive_stats_gen import *
from NFL_offensive_stats_gen import *
from Misc_stat_generator import *

def combined_stats():
    offense_stats = offensive_team_stats()
    defensive_stats = defensive_team_stats()
    misc_stats = misc_team_stats()
    for key in offense_stats:
        offense_stats[key].update(defensive_stats[key])
    for key in offense_stats:
        offense_stats[key].update(misc_stats[key])

    df = pd.DataFrame.from_dict(offense_stats, orient='index')
    df_transposed = df.transpose()
    df.to_excel('full_team_stats.xlsx', engine='openpyxl')
