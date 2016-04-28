##Program to plot Crime Trends Over the MONTHS for different YEARS

CH <- read.csv("Chicago_cleaned.csv") #Read data for particular city
color <- c("yellow", "red", "blue", "black", "green", "purple", "grey", "orange", "cyan", "brown", "aquamarine", "darkgoldenrod1", "lawngreen", "tan1", "gold")
years <- c(2001, 2002, 2003, 2004, 2005, 2006,2007,2008,2009,2010,2011,2012,2013,2014,2015)
Lty <- rep(1,length(years))

#Generate Plot
png("9_11_chicago.jpg")

cdate <- CH$chicago.date
cdate <- as.Date(cdate,"%m/%d/%Y")    #Convert to Date type
df <- data.frame(date = cdate, year = as.numeric(format(cdate, format = "%Y")), month = as.numeric(format(cdate, format = "%m")), day = as.numeric(format(cdate, format = "%d")))
plot(c(1,length(years)), c(0,2000),bty='L', type = "n", xlab = "Years", ylab = "count", main = "Crime in September over the Years")
for (i in 1:length(years)){
month <- df$month[df$year==years[i]]    ## For every year get a count of crime for different months
lines(table(month), type = "o", col=color[i])
}
legend("bottom", years, col = color, lty = Lty, legend = years)
dev.off()

