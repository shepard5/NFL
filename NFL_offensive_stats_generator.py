import pandas as pd
import requests
import openpyxl

def offensive_team_stats(team_ID):
#    url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2022/types/2/teams/" + f"{team_ID}" + "/statistics/0?lang=en&region=us"
#    response = requests.get(url)
#    team_stats = response.json()
    
#    total_off_stats = len(team_stats["splits"]["categories"])


#    for x in range(0,11):
#        team_url = f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2022/types/2/teams/" + f"{team_ID}" + "/statistics/0?lang=en&region=us",
#        response = requests.get(url)
#        team_stats = response.json()

#        passing_stats = team_stats["splits"]["categories"][1]["stats"]
#        rushing_stats = team_stats["splits"][2]
#        receiving_stats = team_stats["splits"][3]
#        defensive_stats = team_stats["splits"][4]

#Collect all stats for team 16

        dict_off_stats = {i:{
        
        for y in range(1,35):
            if y == 31 or y == 32:
                
            print(y)
            team_ID = y
            team_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2022/types/2/teams/" + f"{team_ID}" + "/statistics/0?lang=en&region=us"
            print(team_url)
            response = requests.get(team_url)
            team_stats = response.json()

            passing_stats = team_stats["splits"]["categories"][1]["stats"]
            
            dict_off_stats = {i:
                              {stat["displayName"]:stat["value"] for stat in passing_stats[i]

                               }
                              for i in range(1,35
                              }            
            print(dict_off_stats)
