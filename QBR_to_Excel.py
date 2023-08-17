import requests
import pandas as pd

#Use pandas to export all QBR data to an excel sheet

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
    for x in range(1,35):
        data.append(x) 
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

        if data[x] not in seen and x<35 :
            seen.add(x)
            data[Team_ID].append((Team_ID, Team_QBR))
    print(data)

    
    sorted_data = sorted(data, key=lambda x: x[0])
    print(sorted_data)



# 1. Read the existing Excel file
    file_path = r"C:\Users\Sam\Desktop\NFL-main\Team_Data.xlsx"
    sheet_name = 'Sheet1'  # Adjust this to your sheet's name if different
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

# 2. Modify the specific column in the DataFrame
# For instance, if you want to overwrite the 'existing_col' column with new data
     # Adjust this to your new data
    df['QBR'] = sorted_data

# 3. Write the updated DataFrame back to the Excel file
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
        writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
        if sheet_name in writer.sheets:
            for column in writer.sheets[sheet_name].iter_cols(min_col=writer.sheets[sheet_name].max_column, max_col=writer.sheets[sheet_name].max_column):
                for cell in column:
                    cell.value = None  # Clear the existing content in the column
            df.to_excel(writer, sheet_name=sheet_name, index=False, startrow=0, startcol=writer.sheets[sheet_name].max_column - 1, columns=['existing_col'])
        else:
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Updated the Excel file successfully!")





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

