import requests
import pandas as pd

def NFL_ATS(team_id):

    #See ESPN TeamID file for reference
    
    #response = requests.get('https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/' + year + '/types/2/teams/' + team_id + '/ats')
    #ATS_totals = response.json()

    response_2 = requests.get('https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams/' + team_id + '/odds/1002/past-performances?limit=300')
    ATS_historical = response_2.json()

    week_recent = ATS_historical["items"][len(ATS_historical['items'])-1]
    week_2nd_recent = ATS_historical["items"][len(ATS_historical['items'])-2]
    
    if week_recent["spreadWinner"] == week_2nd_recent["spreadWinner"]: #If a team is on an ATS win or lose streak prospect will return as hot or cold respectively.
        if week_recent["spreadWinner"] == True:
            prospect = 'hot'
        else:
            prospect = 'cold'
    else:
        prospect = None
        
    return prospect

    
