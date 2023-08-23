# Shepard5 NFL Model
The goal of this repo is to identify favorable week to week nfl spreads such that in the long term a sportsbettor will return a positive rate of return.
Machine learning may be a good course of action using prior seasons as testing samples. 
As of right now the script will utilize team momentum as the primary predictor variable. Teams that have two or more consecutive wins or losses against the spread will be considered as candidates week to week; determining whether the spread has adjusted sufficiently based on new information (game outcomes) may be considered as well.
Focus is now on creating pipelines that provide useful data and selecting the best model using step regression.

#
8/23 - Exploring developing models for individual teams rather than using all available data to summarize into one singular model. QB-centric teams (KC, BAL, Bills, Rams) will find that QBR is a better predictor variable than teams with a more homogeneous offense (49ers, Patriots, Steelers, Titans). 
![Capture](https://github.com/shepard5/NFL/assets/108085853/c1721095-68b1-42e9-88bc-9459e8ee0471)
![Capture_light](https://github.com/shepard5/NFL/assets/108085853/935b3811-8490-44df-9321-9b2547e33b71)
