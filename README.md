# NFL Betting Model
The goal of this script / function is to identify favorable week to week nfl spreads such that in the long term a sportsbettor will return a positive rate of return.
Machine learning may be a good course of action using prior seasons as testing samples. 
As of right now the script will utilize team momentum as the primary predictor variable. Teams that have two or more consecutive wins or losses against the spread will be considered as candidates week to week; determining whether the spread has adjusted sufficiently based on new information (game outcomes) may be considered as well.

As of 8/17 - Focusing on developing scripts that can seamlessly transmit predicting variables to an excel file to be imported to R Studio. Seamlessly enough to circumstantially produce datasheets that will be interpreted by R Studio week to week without interruption - fluctuating bye-weeks, AFC NFC TeamIDs, multiple inputs of a statistic when only one is desired, and all other unexpected results - should be accounted for and blended into each pipeline.

