import requests
import pandas as pd

#Use pandas to export all QBR data to an excel sheet

def QBR(Team_ID):


#Find most recently played week for most recent QBR data
    
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

#Pull QBR data for desired team from Team_ID and season / week we just gathered
        
    for x in range(0,len(QBR_data["items"])-1): 
        correct_team = f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/teams/{Team_ID}?lang=en&region=us"
 
        if correct_team == str(QBR_data["items"][x]["team"]["$ref"]):
            Team_QBR = QBR_data["items"][x]["splits"]["categories"][0]["stats"][17]["value"]
            return(Team_QBR)


## For future use
#   return year
#   return week

