# Shepard5 NFL Model MAT 525 (Continued)
The goal of this project is to sufficiently predict all NFL teams' season win totals with sufficient accuracy. I'm assuming it's not possible to find a model that produces statistically significant insights beyond the bounds of the typical ~10% buffer sportsbooks provide using player and team sport related statistics. Anywho, I'm curious to see how close I can get.

As of 2021, sportsbooks' preseason lines have an MSE of 2.6 when compared to actual season results. The goal of this project is to produce an MSE that is confidently under the 2.6 benchmark for future seasons. 


#
Developing models for individual teams rather than using all available data to summarize into one singular model will improve predictability game outcomes. For example, QB-centric teams (KC, BAL, Bills, Rams) will find that QBR is a better predictor variable than teams with a more homogeneous offense (49ers, Patriots, Steelers, Titans). 

I ran a quick linear regression in R for QB-centric (QB heavy) (BUF,NYJ,CIN,BAL,JAX,KC,DEN,PHI,CHI,ARI) and QB-non-centric (QB light) (NE,CLE,PIT,HOU,TEN,LV,WSH,DET,SEA,49ers) teams. I also balanced it with sacks to account for influences of team defenses on win totals. While it is a small sample size, the results support intuition. 


![Inkednflregressionpic](https://github.com/shepard5/NFL/assets/108085853/dce8d5f4-d47c-49f2-bf61-e0a0b4cebda6)

#
Granted, this regression is optimized for this dataset, and may not fit other season data well.

#
While linear regression may be good at estimating team outcomes and eliminating human bias, football is a very complex sport where several unexpected variables may alter a team's win totals over the course of 18 weeks (trades, injuries, rookie variability, etc). Delving deeper into the data and exploring the near-endless landscape of potentially predictable variables would surely reveal easter eggs, but mastering other modeling techniques and building a model on theory would serve better for the sport of football.

I encourage you to take a look at my other projects, particularly my project building horse racing models where I plan on exploring other model building techniques. 



Neural Network Predictions vs Actual (Average MSE ~ 8.5) - Next generate synthetic data to train the network, or collect data from college games as well (12/8)  

![Capture](https://github.com/shepard5/NFL/assets/108085853/42d88026-9660-43f2-b520-b42a072eff75)

https://rpubs.com/Timboslice003/991908

Timmy Hernandez does a great job addressing the goals and approach to building such a model. For this particular variable, the main concern is minimizing MSE.
