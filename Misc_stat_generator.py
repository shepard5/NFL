import pandas as pd
import requests
import openpyxl

def misc_team_stats():
    teamIDs=[]
    for x in range (1,35):
        if x==31 or x==32:
            continue
        else:
            teamIDs.append(x)
    dict_misc_stats = {}

    for teamID in teamIDs:
        team_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2022/types/2/teams/" + f"{teamID}" + "/statistics/0?lang=en&region=us"
        response = requests.get(team_url)
        team_stats = response.json()

        misc_stats = team_stats["splits"]["categories"][10]["stats"]
        dict_misc_stats[teamID] = {stat["displayName"]:stat["value"] for stat in misc_stats}


        df = pd.DataFrame(dict_misc_stats)
        df_transposed = df.transpose()
        df_transposed.to_excel('defensive_stats.xlsx', engine='openpyxl')

    return dict_misc_stats
