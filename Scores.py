## A simple football model

import requests
import pandas as pd
def football_scores(): #rovides scores for previous week
    url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"  # replace this with the API endpoint
    headers = {
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        with open("ESPNdata.txt", "a") as f:
            print(data, file = f)
    else:
        print(f"Error: {response.status_code}")
    week_matchups = {}
    for x in range(0, len(data["events"])):
        week_matchups[data["events"][x]["shortName"]] = data["events"][x]["shortName"]
        for y in range (0,2):
            for item in data["events"][x]["competitions"][0]["competitors"][y]["score"]: #Provides each matchup for the week loaded from the URL
                if y == 1: 
                    week_matchups[data["events"][x]["shortName"]] = (home_team,data["events"][x]["competitions"][0]["competitors"][y]["score"]) #Storing scores as a tuple with home team first, away team second      
                home_team = item  # <- not bad out of me
    print(week_matchups)
    df = pd.DataFrame(week_matchups).T  # Transpose to have each key as a row
    df.to_excel('output.xlsx', engine='openpyxl', header=False, index=True)
    

