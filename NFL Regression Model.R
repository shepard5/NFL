#Import however many excel sheets using this method on mac, haven't been able to troubleshoot otherwise

filepath_1<-file.choose()
file_1<-filepath_1

filepath_2<-file.choose()
file_2<-filepath_2


data<-read_excel(file_1)
data2<-read_execl(file_2)


#Look into step wise regression to find best model.


#Need to incorporate player injuries, division game, coming off bye week, home field advantage and others
