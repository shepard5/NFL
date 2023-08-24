import pandas as pd
import requests

def team_wins(year,teamID):
    team_url = f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/"+f"{year}"+"/types/2/teams/"+f"{teamID}"+"/record?lang=en&region=us"
    response = requests.get(team_url)
    team_stats = response.json()
    wins = team_stats["items"][0]["stats"][19]["value"]
    return wins

def all_team_wins(year):
    data = {i:0 for i in range(1, 35) if i not in (31, 32)}   
    for x in data:
        data[x] = int(team_wins(year,x))
    df = pd.DataFrame([data])
    df_transposed = df.transpose()
    df_transposed.to_excel('team_wins.xlsx', engine='openpyxl')

    
        
            
