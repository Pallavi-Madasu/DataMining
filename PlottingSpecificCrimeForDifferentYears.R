##Program to plot trend of SPECIFIC CRIME over the YEARS

CH <- read.csv("Denver_data_cleaned.csv")  ##Read data
years <- c(2006,2007,2008,2009,2010,2011,2012,2013,2014,2015)
color <- c( "red", "blue", "black", "green", "purple", "grey", "orange", "cyan", "brown", "aquamarine")
Lty <- rep(1,length(years))

png("assualt_Denver.jpg")
plot(c(1,12), c(200,1500),bty='L', type = "n", xlab = "Months", ylab = "count", main = "Crime:Assault over the Years in Philadelphia")

##Select only dates of occurance of SPECIFIC crime TYPE
cdate <- philly$DISPATCH_DATE[philly$TEXT_GENERAL_CODE=="ASSAULT"]
cdate <- as.Date(cdate,"%m/%d/%Y")
df <- data.frame(date = cdate, year = as.numeric(format(cdate, format = "%Y")), month = as.numeric(format(cdate, format = "%m")), day = as.numeric(format(cdate, format = "%d")))

##Generate the PLOTS
for (i in 1:length(years)){
  month <- df$month[df$year==years[i]]
  lines(table(month), type = "o", col=color[i])
}
legend("topleft", years, col = color, lty = Lty, legend = years)
dev.off()

