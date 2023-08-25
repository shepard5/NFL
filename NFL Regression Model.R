#Import however many excel sheets using this method on mac, haven't been able to troubleshoot otherwise
library(MASS)
library(readxl)
library(ggplot2)

#Select spreadsheets in file view

filepath_2022<-file.choose()
file_2022<-filepath_2022

filepath_2021<-file.choose()
file_2021<-filepath_2021

filepath_2019<-file.choose()
file_2019<-filepath_2019

filepath_2018<-file.choose()
file_2018<-filepath_2018

#Import 2022 Wins Column

filepath_2022Ws<-file.choose()
file_2022Ws<-filepath_2022Ws
Wins_2022_df<-read_excel(file_2022Ws)
Wins2022 <- Wins_2022_df[["0"]]

filepath_2021Ws<-file.choose()
file_2021Ws<-filepath_2021Ws
Wins_2021_df<-read_excel(file_2021Ws)
Wins2021 <- Wins_2021_df[['0']]

filepath_2019Ws<-file.choose()
file_2019Ws<-filepath_2019Ws
Wins_2019_df<-read_excel(file_2019Ws)
Wins2019 <- Wins_2019_df[['0']]

filepath_2018Ws<-file.choose()
file_2018Ws<-filepath_2018Ws
Wins_2018_df<-read_excel(file_2018Ws)
Wins2018 <- Wins_2018_df[["0"]]

#Create team data frames for use in R

data2022<-read_excel(file_2022)
data2021<-read_excel(file_2021)
data2019<-read_excel(file_2019)
data2018<-read_excel(file_2018)

data2018$year <- 2018
data2019$year <- 2019
data2021$year <- 2021
data2022$year <- 2022

#Modeling Wins with variables in team data

model_2022<-lm(Wins2022~data2022$`ESPN Quarterback Rating`+data2022$Sacks)
model_2021<-lm(Wins2021~data2021$`ESPN Quarterback Rating`+data2021$Sacks)
model_2019<-lm(Wins2019~data2019$`ESPN Quarterback Rating`+data2019$Sacks)
model_2018<-lm(Wins2018~data2018$`ESPN Quarterback Rating`+data2018$Sacks)

#QB Heavy All 4 Years

#For regression, try to have similar win totals for qb heavy and qb light

QB_Light_IDs<-c(17,23,10,13,28,8,25,32,5,26)
QB_Heavy_IDs<-c(2,4,30,12,21,3,22,31,7,15,6,7)

QB_Light_Wins<-Wins_2022_df$`0`[QB_Light_IDs] #Avg 8.5 Wins per team
QB_Heavy_Wins<-Wins_2022_df$`0`[QB_Heavy_IDs] #Avg 9.33 Wins per team

#Tinkering with different variables

qb_light_model<-lm(QB_Light_Wins~data2022$`Quarterback Rating`[QB_Light_IDs]+data2022$Sacks[QB_Light_IDs]+data2022$`Turnover Ratio`[QB_Light_IDs]+data2022$`Possession Time Seconds`[QB_Light_IDs])
qb_heavy_model<-lm(QB_Heavy_Wins~data2022$`Quarterback Rating`[QB_Heavy_IDs]+data2022$Sacks[QB_Heavy_IDs]+data2022$`Turnover Ratio`[QB_Heavy_IDs]+data2022$`Possession Time Seconds`[QB_Heavy_IDs])

#Checking for multicollinearity
combined_df_heavy<-data.frame(data2022$`Quarterback Rating`[QB_Heavy_IDs],data2022$Sacks[QB_Heavy_IDs],data2022$`Turnover Ratio`[QB_Heavy_IDs],data2022$`Possession Time Seconds`[QB_Heavy_IDs])
combined_df_light<-data.frame(data2022$`Quarterback Rating`[QB_Light_IDs],data2022$Sacks[QB_Light_IDs],data2022$`Turnover Ratio`[QB_Light_IDs],data2022$`Possession Time Seconds`[QB_Light_IDs])

cor_matrix<-cor(combined_df,use = "complete.obs", method = "pearson")

##Collinearity doesn't seem to be a major issue with these variables - all at or below 0.5. What is concerning is for the QB light data set, QBR and defensive sacks appear to be
#correlated far higher than expectations.

#Will have to make sure QB light and heavy teams analysis isn't also a QB bad and good analysis. Maybe will have to look at passing attempts 
#and/or number of plays with meaningful/beyond-expectation contributions by quarterbacks 

summary(qb_light_model)
summary(qb_heavy_model)


#Running model using Miami Dolphins Data - Using ESPN Quarterback Rating



#Expected total wins is 10.68 assuming all 
#2022 conditions remains the same. Using Quarterback Rating, 10.38. Might have to look into Miami - looking like they
#could break 9.5 wins. Update: Jalen Ramsey is out - look into importing injury data. 


summary(model_2022)
summary(model_2021)
summary(model_2019)
summary(model_2018)


#8/24 Logistic regression of match-ups among teams with high predictability

#High Predictability Candidates: 49ers,DAL,MIA,MIN,NYG,PHI,SEA,PIT








#Sample regression using combined data

combined_data <- rbind(data2018, data2019, data2021, data2022)
model <- lm(combined_data$`Red Zone Efficiency Percentage`~combined_data$`First Downs Per Game`)
summary(model)


## Plotting data with regression line

ggplot(combined_data, aes(x=combined_data$`ESPN Quarterback Rating`, y=combined_data$`Red Zone Efficiency Percentage`)) +
  geom_point(aes(color=as.factor(year)), alpha=0.6) +  # Different colors for each year
  geom_abline(intercept = coef(model)[1], slope = coef(model)[2], color="black", size=1.2) +
  labs(title="Scatter plot with Regression Line", x="X-axis label", y="Y-axis label") +
  theme_minimal() 


#Look into step wise regression to find best model
library(MASS)

#Need to incorporate player injuries, division game, coming off bye week, home field advantage and others
model<-lm(data$Wins~data$`Turnover Ratio`)
model.residuals <- resid