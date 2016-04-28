##Plotting Crime Evolution for Months

bal <- read.csv("Baltimore_Crime_Data.csv")
cdate <- bal$CrimeDate

##Converting to date data-type
cdate <- as.Date(cdate,"%m/%d/%Y")
df <- data.frame(date = cdate, year = as.numeric(format(cdate, format = "%Y")), month = as.numeric(format(cdate, format = "%m")), day = as.numeric(format(cdate, format = "%d")))
years <- c(2013,2014,2015)
color <- c("red", "black", "green")   #, "purple", "cyan" ,"blue", "brown")#,"aquamarine", "darkgoldenrod1", "lawngreen")
png("Baltimore_may.jpg")
plot(c(1,31),c(50,150), bty='L', type = "n", xlab = "Days", ylab = "count", main = "Crime Evolution in Baltimore in May, 2015")

##Plotting graphs for particular month over the years
for (i in 1:length(years)){
  day <- df$day[df$year==years[i] & df$month==5]
  print(table(day))
  lines(table(day), type = "o", col=color[i])
}
legend("bottomright", years, col = color, lty = rep(1,length(years)), legend = years)
dev.off()


