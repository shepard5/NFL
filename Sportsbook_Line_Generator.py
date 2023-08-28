import pandas as pd
import requests as r
import openpyxl

def Get_Weekly_Matchups(year,week):
    url_1 = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/" + f"{year}" + "/types/2/weeks/" + f"{week}" + "/events?lang=en%C2%AEion=us"
    response = r.get(url_1)
    matchups = response.json()
    dict_schedules = {}
    dict_spreads = {}
    dict_over_under = {}
    dict_moneyline = {}
    for x in range(len(matchups["items"])):
        print(x)
        #Matchup Details Request
    
        url = matchups["items"][x]["$ref"]

        matchup_response = r.get(url)
        ind_matchup = matchup_response.json()
        matchup_id = ind_matchup["id"]
        matchup_name = ind_matchup["shortName"]
        if matchup_name not in dict_schedules:
            dict_schedules[matchup_name] = {}
            
        #Odds Request

        odds_url = ind_matchup["competitions"][0]["odds"]["$ref"]
        odds_response = r.get(odds_url)
        odds_json = odds_response.json()
    
        spreads = [odds_json["items"][x]["spread"] for x in range(len(odds_json["items"])) if "spread" in odds_json["items"][x]]
        over_under = [odds_json["items"][x]["overUnder"] for x in range(len(odds_json["items"])) if "overUnder" in odds_json["items"][x]]
        moneyline = [
            [
                odds_json["items"][x]["awayTeamOdds"].get("moneyLine", None),
                odds_json["items"][x]["homeTeamOdds"].get("moneyLine", None)
            ]
            for x in range(len(odds_json["items"]))
            if "awayTeamOdds" and "homeTeamOdds" in odds_json["items"][x]
        ]

        #Initialize dictionary containing all stats
        dict_schedules[matchup_name]["Spreads"] = spreads
        dict_schedules[matchup_name]["MoneyLine"] = moneyline
        dict_schedules[matchup_name]["OverUnder"] = over_under

    for item in dict_schedules:
            
        dict_spreads[item] = dict_schedules[item]["Spreads"]
        dict_over_under[item] = dict_schedules[item]["OverUnder"]
        dict_moneyline[item] = dict_schedules[item]["MoneyLine"]
        
    df = pd.DataFrame.from_dict(dict_schedules, orient='index')
    df_transposed = df.transpose()
    df.to_excel('weekly_odds.xlsx', engine='openpyxl')

