# GRAF - čas v odvisnosti od števila točk 

library(ggplot2)
library(plotly)

cas <- read.table("cas.txt")
stevilo_tock <- c(4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 50, 60, 70, 100, 150, 200, 250)

tabela <- data.frame(t(setNames(cas, stevilo_tock)))
colnames(tabela) <- c("casi")
plot.new()
ggplot(tabela) + geom_line(data = tabela, aes(x = stevilo_tock, y = tabela$casi), col = "Violet") + 
  geom_point(data = tabela, aes(x = stevilo_tock, y = tabela$casi), col = "Blue") + 
  xlab("Stevilo tock") + ylab("Cas")

