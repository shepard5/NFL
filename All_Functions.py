import requests
import pandas as pd
import openpyxl

def NFL_ATS_to_Excel():

    streak_data = []
    
    for x in range(1,35):
        if x in [31,32]:
            continue
        
        ATS_streak = NFL_ATS(str(x))
        streak_data.append([x, ATS_streak])
            
    print(streak_data)
    
    df = pd.DataFrame(streak_data, columns=['TeamID', 'Streak (2 or more ATS)'])

    with pd.ExcelWriter('ATS_Streak_output.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, index = False) 
    








def NFL_ATS():

    #See ESPN TeamID file for reference
    
    #response = requests.get('https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/' + year + '/types/2/teams/' + team_id + '/ats')
    #ATS_totals = response.json()

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

        #print(week_recent)
        #print(week_2nd_recent)
        print(team_url)
        print(week_recent["spreadWinner"])
        if week_recent["spreadWinner"] == week_2nd_recent["spreadWinner"]: #If a team is on an ATS win or lose streak prospect will return as hot or cold respectively.
            if week_recent["spreadWinner"] == True:
                prospect = 'hot'
            else:
                prospect = 'cold'
        else:
            prospect = ""
        
        ats_data.append([x,prospect])
    return ats_data

    







def QBR():


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

 #  excel_file_path = "C:\Users\Sam\Desktop\NFL-main\Script Outputs ETC\ATS_Streak_output.xlsx"
    sheet_name = "Sheet1"

    data = [] 
    #for x in range(1,35):
    #    data.append(x) 
    print(data)
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
            data.append([Team_ID, Team_QBR])
    print(data)

    
    sorted_data = sorted(data, key=lambda x: x[0])
    #print(sorted_data)

    TeamID_in_data = [sublist[0] for sublist in data]

    for x in range (1,35):
        if x not in TeamID_in_data:
            data.append([x,0])

    sorted_data = sorted(data, key=lambda x: x[0])
    print(sorted_data)


    file_path = r"C:\Users\Sam\Desktop\NFL-main\Team_Data.xlsx"
    sheet_name = 'Sheet1'  # Adjust this to your sheet's name if different

    df = pd.DataFrame(sorted_data)
    df.columns = ["Team ID","QBR"]

    
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)






##8/17 Notes - Trying to figure out how to get the data set formatted well. Filling in zeros for teams with byes and NFC AFC. Removing repeated players if a qb gets subbed in for the week. 



#Pull QBR data for desired team from Team_ID and season / week we just gathered
        
#    for x in range(0,len(QBR_data["items"])-1): 
#        correct_team = f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/teams/{Team_ID}?lang=en&region=us"
# 
#        if correct_team == str(QBR_data["items"][x]["team"]["$ref"]):
#            Team_QBR = QBR_data["items"][x]["splits"]["categories"][0]["stats"][17]["value"]
#            return(Team_QBR)


## For future use
#   return year
#   return week
