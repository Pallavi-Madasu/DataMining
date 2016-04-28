##Program to show OVERALL CRIME over the YEARS

CH <- read.csv("Chicago_crime_data_cleaned.csv")   ##Read the data
color <- c("red", "blue", "black", "green", "purple", "grey", "orange", "cyan", "brown", "aquamarine", "darkgoldenrod1", "lawngreen", "tan1", "gold", "yellow")
Lty <- rep(1,length(crime))
years <- c(2001:2016)

##Generating plots for overall crime in a year
png("overallCrime.jpg")  
plot(c(2001:2016), c(0,200000),bty='L', type = "n", xlab = "Years", ylab = "count", main = "Types of Crime in Chicago")
for (i in 1:length(years)){
  cdate <- CH$chicago.date
  cdate <- as.Date(cdate,"%m/%d/%Y")
  cyear <- format(cdate, "%Y")
  lines(table(cyear), type = "o", col=color[i])
}
legend("topleft", years, col = color, lty = Lty, legend = years)
dev.off()

