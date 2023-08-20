data<-read_excel("C:\\Users\\Sam\\Desktop\\NFL-main\\Functions\\NFL_Data.xlsx")

#data_clean<-data[-c(27,28,31,32), ]

data_clean<-data[data$QBR != 0]
y<-data_clean$`ATS Streak`
x<-data_clean$QBR
x_log<-log(data_clean$QBR)

model<-lm(x~y, data=data_clean)
summary(model)
