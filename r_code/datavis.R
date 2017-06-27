library(ggplot2)
library(corrgram)

mycsv <- read.csv('/home/nozes/labs/datavis-article/mycsv.csv', sep = ';', header=TRUE)
colnames(mycsv)
typeof(mycsv)


xoxo <-mycsv[,2:8]


m <- as.matrix(xoxo)
colnames(m)
rownames(m) <- colnames(m)
m

heatmap(as.matrix(m))






library(corrgram)


corrgram(mycsv, order=TRUE, lower.panel=panel.shade,
         upper.panel=panel.pie, text.panel=panel.txt) 

