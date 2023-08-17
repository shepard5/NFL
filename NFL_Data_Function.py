import pandas as pd
import requests
import openpyxl

def NFL_Data():

#ATS Streak
    
    ats_data = [] 
    for x in range(1, 35):
        if x == 31 or x == 32:
            prospect = ""
            ats_data.append([x,prospect])
            continue
        team_url = f'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams/{x}/odds/1002/past-performances?limit=300'
        response = requests.get(team_url)
        ATS_historical = response.json()

        week_recent = ATS_historical["items"][len(ATS_historical['items'])-1]
        week_2nd_recent = ATS_historical["items"][len(ATS_historical['items'])-2]

        if week_recent["spreadWinner"] == week_2nd_recent["spreadWinner"]: #If a team is on an ATS win or lose streak prospect will return as hot or cold respectively.
            if week_recent["spreadWinner"] == True:
                prospect = 'hot'
            else:
                prospect = 'cold'
        else:
            prospect = ""
        
        ats_data.append(prospect)
    #return ats_data
    print(ats_data)


#QBR

    for x in range(23,21,-1):
        for y in range(18,0,-1):
            url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/20{x}/types/2/weeks/{y}/qbr/10000?limit=300"       
            headers = {
    
            }

            response = requests.get(url, headers=headers)
            QBR_data = response.json()
            
            Team_QBR = 0
        
            if len(QBR_data["items"])>1:

                url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/20{x}/types/2/weeks/{y}/qbr/10000?limit=300"
                headers = {
    
                }
                response = requests.get(url, headers=headers)
                QBR_data = response.json()
                Team_QBR = 1
                year = f"20{x}"
                week = y
                break       

        if Team_QBR == 1:    
            break

    data = [] 
    seen = set()
    
    for x in range(0,len(QBR_data["items"])-1): 

        Team_QBR = QBR_data["items"][x]["splits"]["categories"][0]["stats"][17]["value"]
        Team_ID_url = QBR_data["items"][x]["team"]["$ref"]
        Team_ID = ""

        if Team_ID_url[83] != "?":
            Team_ID = int(Team_ID_url[82] + Team_ID_url[83])

        else:
            Team_ID = int(Team_ID_url[82])

        if Team_ID not in seen and x<35 :
            seen.add(Team_ID)
            data.append([Team_ID,Team_QBR])

    
    sorted_data = sorted(data, key=lambda x: x[0])
    #return sorted_data
    print(sorted_data)

 #   complete_data = [] 
 #   for x in range(1,35):
 #       complete_data.append([) 
 #   for x in ats_data:
 #       complete_data.append[
