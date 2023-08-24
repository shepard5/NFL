# Shepard5 NFL Model
The goal of this repo is to identify favorable week to week nfl spreads, win/loss, over/under lines such that in the long term a sportsbettor will return a positive rate of return.
The repo consists primarily of data collection modules along with R scripts that tinker data extracted from the python functions. 
I suggest you refer to the TeamID excel sheet to link NFL teams with their corresponding indices in the automatically generated excel sheets.


#
Developing models for individual teams rather than using all available data to summarize into one singular model will improve predictability game outcomes. For example, QB-centric teams (KC, BAL, Bills, Rams) will find that QBR is a better predictor variable than teams with a more homogeneous offense (49ers, Patriots, Steelers, Titans). 

I ran a quick linear regression in R for QB heavy and QB light teams with the teams I just listed plus a few more. I also balanced it with defensive metrics (season interceptions and sacks) so that we aren't getting hit by too many invisible variables. While it is a small sample size, the results support our intuition. 

![Capture](https://github.com/shepard5/NFL/assets/108085853/c1721095-68b1-42e9-88bc-9459e8ee0471)
![Capture_light](https://github.com/shepard5/NFL/assets/108085853/935b3811-8490-44df-9321-9b2547e33b71)

#
Introducing logistic regression model to predict over/under and moneyline outcomes. Teams will be selected based on predictability - If a team's roster has changed heavily since last season, will have to wait until data comes out from the first few weeks to make decisions. Need to make a detailed list of teams whose rosters are highly similar or differnet compared to the 2022 season; factors to consider - young players improving, older players depreciating, coaching changes for struggling teams, qb changes, maybe consider changes that have been overcompensated (Falcons - Bijon Robinson, Desmond Ridder ?). Teams with high predictability will be selected for specialized model development. Will then look for identical matchups (or close to) present in both 2022 and 2023 between teams with high (and possibly low predictability) and run regression using 2022 season data. 
