import pandas as pd
import requests
import openpyxl

def combined_stats(year):

    offense_stats = offensive_team_stats(year)
    defensive_stats = defensive_team_stats(year)
    misc_stats = misc_team_stats(year)
    combined_stats = offense_stats
    for key in combined_stats:
        combined_stats[key].update(defensive_stats[key])

    for key in combined_stats:
        combined_stats[key].update(misc_stats[key])

    df = pd.DataFrame.from_dict(combined_stats, orient='index')
    df_transposed = df.transpose()
    df.to_excel('full_team_stats.xlsx', engine='openpyxl')

#    return combined_stats




def offensive_team_stats(year):
    dict_off_stats = {}
    for teamID in range(1,35):         

        if teamID not in (31,32):
            team_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/+"+f"{year}"+"/types/2/teams/" + f"{teamID}" + "/statistics/0?lang=en&region=us"
            response = requests.get(team_url)
            team_stats = response.json()
            passing_stats = team_stats["splits"]["categories"][1]["stats"]
            dict_off_stats[teamID] = {stat["displayName"]:stat["value"] for stat in passing_stats}

    return dict_off_stats





def defensive_team_stats(year):

    dict_def_stats = {}

    for teamID in range(1,35):

        if teamID not in (31,32):
            team_url =f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/"+f"{year}"+"/types/2/teams/" + f"{teamID}" + "/statistics/0?lang=en&region=us"
            response = requests.get(team_url)
            team_stats = response.json()
            def_stats = team_stats["splits"]["categories"][4]["stats"]
            dict_def_stats[teamID] = {stat["displayName"]:stat["value"] for stat in def_stats}

    return dict_def_stats





def misc_team_stats(year):

    dict_misc_stats = {}

    for teamID in range(1,35):

        if teamID not in (31,32):
            team_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/" + f"{year}" + "/types/2/teams/" + f"{teamID}" + "/statistics/0?lang=en&region=us"
            response = requests.get(team_url)
            team_stats = response.json()
            misc_stats = team_stats["splits"]["categories"][10]["stats"]
            dict_misc_stats[teamID] = {stat["displayName"]:stat["value"] for stat in misc_stats}

    return dict_misc_stats
