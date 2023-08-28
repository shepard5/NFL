import pandas as pd
import requests as r
import openpyxl

def Get_Weekly_Matchups():
    current_week_url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events"
    response = r.get(current_week_url)
    matchups = response.json()
    dict_all_odds = {}
    dict_spreads = {}
    dict_over_under = {}
    dict_moneyline = {}
    for x in range(len(matchups["items"])):

        #Matchup Details Request
    
        url = matchups["items"][x]["$ref"]

        matchup_response = r.get(url)
        ind_matchup = matchup_response.json()
        matchup_id = ind_matchup["id"]
        matchup_name = ind_matchup["shortName"]
        if matchup_name not in dict_all_odds:
            dict_all_odds[matchup_name] = {}
            
        #Odds Request

        odds_url = ind_matchup["competitions"][0]["odds"]["$ref"]
        odds_response = r.get(odds_url)
        odds_json = odds_response.json()
    
        spreads = [odds_json["items"][x]["spread"] for x in range(len(odds_json["items"])) if "spread" in odds_json["items"][x]]
        over_under = [odds_json["items"][x]["overUnder"] for x in range(len(odds_json["items"])) if "overUnder" in odds_json["items"][x]]
        moneyline = [[odds_json["items"][x]["awayTeamOdds"]["moneyLine"],odds_json["items"][x]["homeTeamOdds"]["moneyLine"]] for x in range(len(odds_json["items"])) if "awayTeamOdds" and "homeTeamOdds" in odds_json["items"][x]]

        #Initialize dictionary containing all stats
        dict_all_odds[matchup_name]["Spreads"] = spreads
        dict_all_odds[matchup_name]["MoneyLine"] = moneyline
        dict_all_odds[matchup_name]["OverUnder"] = over_under

    for item in dict_all_odds:
            
        dict_spreads[item] = dict_all_odds[item]["Spreads"]
        dict_over_under[item] = dict_all_odds[item]["OverUnder"]
        dict_moneyline[item] = dict_all_odds[item]["MoneyLine"]
        
    df = pd.DataFrame.from_dict('Replace with desired dictionary here', orient='index')
    df_transposed = df.transpose()
    df_transposed.to_excel('weekly_odds.xlsx', engine='openpyxl')

