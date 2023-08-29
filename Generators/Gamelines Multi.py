import pandas as pd
import requests as r
import openpyxl

def Get_Weekly_Matchups(year,week):
    url_1 = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/" + f"{year}" + "/types/2/weeks/" + f"{week}" + "/events?lang=en%C2%AEion=us"
    response = r.get(url_1)
    matchups = response.json()
    
    dict_all_odds = {}
    dict_spreads = {}
    dict_over_under = {}
    dict_moneyline = {}

    providers = [3,5,7,8,11,12] #Caesar's, DraftKings, MGM, Point House, Titan House, Unibet; Respectively
    
    for y in range(len(matchups["items"])):
        print(y)

        #Matchup Details Request
    
        url_2 = matchups["items"][y]["$ref"]

        matchup_response = r.get(url_2)
        ind_matchup = matchup_response.json()
        matchup_id = ind_matchup["id"]
        matchup_name = ind_matchup["shortName"]

        if matchup_name not in dict_all_odds:
            dict_all_odds[matchup_name] = {}
            dict_spreads[matchup_name] = {}
            dict_over_under[matchup_name] = {}
            dict_moneyline[matchup_name] = {}
            
        #Odds Request

        odds_url = ind_matchup["competitions"][0]["odds"]["$ref"]
        odds_response = r.get(odds_url)
        odds_json = odds_response.json()
    
        spread = {x: odds_json["items"][x]["spread"] for x in providers if "spread" in odds_json["items"][x]} 
        over_under = {x: odds_json["items"][x]["overUnder"] for x in providers if "overUnder" in odds_json["items"][x]} 
        moneyline = {x : [american_to_decimal(odds_json["items"][x]["awayTeamOdds"].get("moneyLine", None)),american_to_decimal(odds_json["items"][x]["homeTeamOdds"].get("moneyLine", None))] for x in providers if "awayTeamOdds" and "homeTeamOdds" in odds_json["items"][x]}
        
        #Initialize dictionary containing all stats

        dict_spreads[matchup_name]["Spreads"] = spread
        dict_over_under[matchup_name]["OverUnder"] = moneyline
        dict_moneyline[matchup_name]["Moneyline"] = over_under
        
        dict_all_odds[matchup_name]["Spreads"] = spread
        dict_all_odds[matchup_name]["Moneyline"] = moneyline
        dict_all_odds[matchup_name]["OverUnder"] = over_under

    for item in dict_all_odds:
            
        dict_spreads[item] = dict_all_odds[item]["Spreads"]
        dict_over_under[item] = dict_all_odds[item]["OverUnder"]
        dict_moneyline[item] = dict_all_odds[item]["Moneyline"]
        
    df = pd.DataFrame.from_dict(dict_moneyline, orient='index')
    df_transposed = df.transpose()
    df.to_excel('weekly_odds.xlsx', engine='openpyxl')


def american_to_decimal(american_odds):
    if american_odds is None:
        return None
    elif american_odds > 0:
        decimal_value = (american_odds / 100) + 1
    else:
        decimal_value = (100 / abs(american_odds)) + 1
    return round(decimal_value, 3)

