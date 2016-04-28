GeneratingHeatMaps.R
PlottingCrimeForParticularMonthOverYears.R
PlottingCrimeOverMonthsForDifferentYears.R
PlottingOverallCrimeForDifferentYears.R
PlottingSpecificCrimeForDifferentYears.R
PlottingTypesOfCrimeOverTheYears.R
R##Program to show EVOLUTION of VARIOUS TYPES of CRIME over the YEARS

CH <- read.csv("Chicago_crime_data_cleaned.csv")   ##Read the data
crime <- levels(CH$crime)      ##Get the unique crime types for the particular city
color <- c("red", "blue", "black", "green", "purple", "grey", "orange", "cyan", "brown", "aquamarine", "darkgoldenrod1", "lawngreen", "tan1", "gold", "yellow")
Lty <- rep(1,length(crime))

##Generating plots for various crime types
png("types.jpg")  
plot(c(2001:2016), c(0,200000),bty='L', type = "n", xlab = "Years", ylab = "count", main = "Types of Crime in Chicago")
for (i in 1:length(crime)){
  cdate <- CH$chicago.date[CH$crime==crime[i]]
  cdate <- as.Date(cdate,"%m/%d/%Y")
  cyear <- format(cdate, "%Y")
  lines(table(cyear), type = "o", col=color[i])
}
legend("topleft", c(2001:2016), col = color, lty = Lty, legend = crime)
dev.off()

