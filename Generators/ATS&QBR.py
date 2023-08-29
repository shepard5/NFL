import pandas as pd
import requests
import openpyxl

def NFL_Data():

    dict_ats = {i:0 for i in range (1,35)} 
    for x in range(1, 35):
        team_url = f'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams/{x}/odds/1002/past-performances?limit=300'
        response = requests.get(team_url)
        ats_historical = response.json()
        game_count = len(ats_historical['items'])
        if game_count > 1:
            week_recent = ats_historical["items"][game_count-1]
            week_2nd_recent = ats_historical["items"][game_count-2]
            if week_recent["spreadWinner"] == week_2nd_recent["spreadWinner"]: 
                if week_recent["spreadWinner"] == True:
                    prospect = 1
                elif week_recent["spreadWinner"] == False:
                    prospect = -1
            else:
                prospect = 0 
            dict_ats[x] = prospect
    for x in range(23,21,-1):
        for y in range(18,0,-1):
            url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/20{x}/types/2/weeks/{y}/qbr/10000?limit=300"       
            headers = {
    
            }
            response = requests.get(url, headers=headers)
            qbr_data = response.json()               
            if len(qbr_data["items"])>1:
                year = f"20{x}"
                week = y
                break       
    dict_qbr = {i:0 for i in range(1,35)}
    seen = set()   
    for x in range(0,len(qbr_data["items"])-1): 
        team_qbr = qbr_data["items"][x]["splits"]["categories"][0]["stats"][17]["value"]
        team_id_url = qbr_data["items"][x]["team"]["$ref"]
        if team_id_url[83] != "?":
            team_id = int(team_id_url[82] + team_id_url[83])
        else:
            team_id = int(team_id_url[82])
        if team_id not in seen and x<35 :
            seen.add(team_id)
            dict_qbr[team_id] = team_qbr            
    excel_data = {i:(dict_ats[i],dict_qbr[i]) for i in range(1,35)}
    df = pd.DataFrame(list(excel_data.items()), columns=['Team ID', 'Data'])
    df[['ATS Streak', 'QBR']] = pd.DataFrame(df['Data'].tolist(), index=df.index)
    df.drop('Data', axis=1, inplace=True)
    df.to_excel("NFL_Data.xlsx", index=False, engine='openpyxl')
