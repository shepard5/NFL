# Shepard5 NFL Model MAT 525 (Continued)
The goal of this project is to sufficiently predict all NFL teams' season win totals with sufficient accuracy.

As of 2021, sportsbooks' preseason lines have an MSE of 2.6 when compared to actual season results. The goal of this project is to produce an MSE that is confidently under the 2.6 benchmark for future seasons. 


#
Developing models for individual teams rather than using all available data to summarize into one singular model will improve predictability game outcomes. For example, QB-centric teams (KC, BAL, Bills, Rams) will find that QBR is a better predictor variable than teams with a more homogeneous offense (49ers, Patriots, Steelers, Titans). 

I ran a quick linear regression in R for QB-centric (QB heavy) (BUF,NYJ,CIN,BAL,JAX,KC,DEN,PHI,CHI,ARI) and QB-non-centric (QB light) (NE,CLE,PIT,HOU,TEN,LV,WSH,DET,SEA,49ers) teams. I also balanced it with sacks to account for influences of team defenses on win totals. While it is a small sample size, the results support intuition. 


![Inkednflregressionpic](https://github.com/shepard5/NFL/assets/108085853/dce8d5f4-d47c-49f2-bf61-e0a0b4cebda6)


#
Introducing logistic regression model to predict over/under and moneyline outcomes. Teams will be selected based on predictability - If a team's roster has changed heavily since last season, will have to wait until data comes out from the first few weeks to make decisions. Need to make a detailed list of teams whose rosters are highly similar or differnet compared to the 2022 season; factors to consider - young players improving, older players depreciating, coaching changes for struggling teams, qb changes, maybe consider changes that have been overcompensated (Falcons - Bijon Robinson, Desmond Ridder ?). Teams with high predictability will be selected for specialized model development. Will then look for identical matchups (or close to) present in both 2022 and 2023 between teams with high (and possibly low predictability) and run regression using 2022 season data. 

While linear regression may be good at estimating team outcomes and eliminating human bias, football is a very complex sport where several unexpected variables may alter a team's win totals over the course of 18 weeks (trades, injuries, rookie variability, etc). Delving deeper into the data and exploring the near-endless landscape of potentially predictable variables would surely reveal easter eggs, but mastering other modeling techniques and building a model on theory would serve better for the sport of football.

I encourage you to take a look at my other projects, particularly my project building horse racing models where I plan on exploring other model building techniques. 



Neural Network Predictions vs Actual (Average MSE ~ 8.5):

![Capture](https://github.com/shepard5/NFL/assets/108085853/42d88026-9660-43f2-b520-b42a072eff75)
