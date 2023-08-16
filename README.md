# NFL Momentum Algo
The goal of this script / function is to identify favorable week to week nfl spreads such that in the long term a sportsbettor will return a positive rate of return.
Machine learning may be a good course of action using prior seasons as testing samples. 
As of right now the script will utilize team momentum as the primary predictor variable. Teams that have two or more consecutive wins or losses against the spread will be considered as candidates week to week; determining whether the spread has adjusted sufficiently based on new information (game outcomes) may be considered as well.
8/15 - Need to find a data pipeline sufficient for the script; namely one that provides current and historical spreads from at least one sportsbook as well as game outcomes. Will then proceed to run through each matchup for the upcoming week and store potentially favorable matchups (arbitratily 2 consecutive ATS wins or losses) and run simulations on historical seasons. 

