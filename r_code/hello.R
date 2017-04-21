setwd("~/labs/envirocar/r_code")

duration = read.csv("../data_integration/duration.csv")  # read csv file 
duration_as_list = duration[,1]

hist(duration_as_list)
hist(duration_as_list[duration_as_list < 100]) 
