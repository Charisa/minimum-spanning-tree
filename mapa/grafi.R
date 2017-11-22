require(dplyr)
require(ggplot2)

#graf za vsote kvadratov cen likov odvisnih od stevila tock

tocke <- read.table("rezultati_tocke.txt")
tocke <- as.data.frame(t(tocke))
colnames(tocke) <- c("krog", "kvadrat", "pravokotnik", "elipsa", "trikotnik")
tocke["st_tock"] <- c(4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 50)
#graf
plot.new()
ggplot(data=tocke) + geom_point(data=tocke, aes(x=tocke$st_tock, y=tocke$krog), colour="darkorchid")+
  geom_line(data=tocke, aes(x=tocke$st_tock, y=tocke$krog), colour="darkorchid", size=1.5) + 
  geom_point(data=tocke, aes(x=tocke$st_tock, y=tocke$kvadrat), colour="deeppink")+
  geom_line(data=tocke, aes(x=tocke$st_tock, y=tocke$kvadrat), colour="deeppink", size=1.5) +
  geom_point(data=tocke, aes(x=tocke$st_tock, y=tocke$pravokotnik), colour="goldenrod1")+
  geom_line(data=tocke, aes(x=tocke$st_tock, y=tocke$pravokotnik), colour="goldenrod1", size=1.5) +
  geom_point(data=tocke, aes(x=tocke$st_tock, y=tocke$elipsa), colour="darkcyan")+
  geom_line(data=tocke, aes(x=tocke$st_tock, y=tocke$elipsa), colour="darkcyan", size=1.5) +
  geom_point(data=tocke, aes(x=tocke$st_tock, y=tocke$trikotnik), colour="darkolivegreen3")+
  geom_line(data=tocke, aes(x=tocke$st_tock, y=tocke$trikotnik), colour="darkolivegreen3", size=1.5) + 
  labs(x="Stevilo tock", y="Vsota")
legend("topright", legend = c("krog", "kvadrat", "pravokotnik", "elipsa", "trikotnik"), col = c("darkorchid", "deeppink", "goldenrod1", "darkcyan", "darkolivegreen3"), lty=c(1, 1, 1, 1, 1))

#graf za vsote kvadratov cen likov (brez pravokotnika) odvisnih od polmerov

polmeri <- read.table("rezultati_polmer.txt")
polmeri <- as.data.frame(t(polmeri))
colnames(polmeri) <- c("krog", "kvadrat", "elipsa", "trikotnik")
polmeri["polmer"] <- c(1, 1.5, 2, 5, 10)
#graf
plot.new()
ggplot(data=polmeri) + geom_point(data=polmeri, aes(x=polmeri$polmer, y=polmeri$krog), colour="darkorchid")+
  geom_line(data=polmeri, aes(x=polmeri$polmer, y=polmeri$krog), colour="darkorchid", size=1.5) + 
  geom_point(data=polmeri, aes(x=polmeri$polmer, y=polmeri$kvadrat), colour="deeppink")+
  geom_line(data=polmeri, aes(x=polmeri$polmer, y=polmeri$kvadrat), colour="deeppink", size=1.5) +
  geom_point(data=polmeri, aes(x=polmeri$polmer, y=polmeri$elipsa), colour="darkcyan")+
  geom_line(data=polmeri, aes(x=polmeri$polmer, y=polmeri$elipsa), colour="darkcyan", size=1.5) +
  geom_point(data=polmeri, aes(x=polmeri$polmer, y=polmeri$trikotnik), colour="darkolivegreen3")+
  geom_line(data=polmeri, aes(x=polmeri$polmer, y=polmeri$trikotnik), colour="darkolivegreen3", size=1.5)+ 
  labs(x="Polmer", y="Vsota")
legend("topleft", legend = c("krog", "kvadrat", "elipsa", "trikotnik"), col = c("darkorchid", "deeppink", "darkcyan", "darkolivegreen3"), lty=c(1, 1, 1, 1))
