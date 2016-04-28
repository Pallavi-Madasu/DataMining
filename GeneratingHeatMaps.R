##Plotting heatmaps for various cities individually
library(ggmap)
library(ggplot2)

##For Philadelphia
philly <- read.csv("Philadelphia_Data_Consolidated.csv")
head(philly)
phillyPT<- data.frame()
LAT <- round(as.numeric(philly$POINT_Y),2)
LONG <- round(as.numeric(philly$POINT_X),2)
phillyPT <- data.frame(LONG, LAT)

##Generating the count of Crime for each Neighborhood
locationCrimes <- as.data.frame(table(phillyPT$LONG, phillyPT$LAT))
names(locationCrimes) <- c('long', 'lat', 'Frequency')
locationCrimes$long <- as.numeric(as.character(locationCrimes$long))
locationCrimes$lat <- as.numeric(as.character(locationCrimes$lat))
locationCrimes <- subset(locationCrimes, Frequency >0)
head(locationCrimes)

##Generating map for the city
philMap <- get_map(location = 'philadelphia', zoom = 11)

##plotting heatmaps and bubble maps 
ggmap(philMap) + geom_tile(data = locationCrimes, aes(x = long, y = lat, alpha = Frequency),fill = 'red') + theme(axis.title.y = element_blank(), axis.title.x = element_blank()) + ggtitle("Auto Theft")
ggmap(philMap)+geom_point(data = locationCrimes, aes(x=long, y = lat, size=Frequency), color="blue")


##San Francisco
sf <- read.csv("SFO_Data_Consolidated.csv")
head(sf)
sf$LAT <- round(as.numeric(sf$Y),2)
sf$LONG <- round(as.numeric(sf$X),2)
sfPT<- data.frame(sf$LONG, sf$LAT)
locationCrimes <- as.data.frame(table(sfPT$sf.LONG, sfPT$sf.LAT))
names(locationCrimes) <- c('long', 'lat', 'Frequency')
locationCrimes$long <- as.numeric(as.character(locationCrimes$long))
locationCrimes$lat <- as.numeric(as.character(locationCrimes$lat))
locationCrimes <- subset(locationCrimes, Frequency >0)
head(locationCrimes)
sfMap <- get_map(location = 'san francisco', zoom = 12)
ggmap(sfMap)
ggmap(sfMap) + geom_tile(data = locationCrimes, aes(x = long, y = lat, alpha = Frequency),fill = 'red') + theme(axis.title.y = element_blank(), axis.title.x = element_blank())
ggmap(sfMap)+geom_point(data = locationCrimes, aes(x=long, y = lat, size=Frequency), color="blue")


##Denver
den <- read.csv("Denver_data_cleaned.csv")
head(den)
den$LAT <- round(as.numeric(den$test_d.GEO_LAT),2)
den$LONG <- round(as.numeric(den$test_d.GEO_LON),2)
denPT <- data.frame(den$LONG, den$LAT)
locationCrimes <- as.data.frame(table(denPT$den.LONG, denPT$den.LAT))
names(locationCrimes) <- c('long', 'lat', 'Frequency')
locationCrimes$long <- as.numeric(as.character(locationCrimes$long))
locationCrimes$lat <- as.numeric(as.character(locationCrimes$lat))
locationCrimes <- subset(locationCrimes, Frequency >0)
head(locationCrimes)
denverMap <- get_map(location = 'denver', zoom = 12)
ggmap(denverMap)
ggmap(denverMap) + geom_tile(data = locationCrimes, aes(x = long, y = lat, alpha = Frequency),fill = 'red') + theme(axis.title.y = element_blank(), axis.title.x = element_blank())

##Baltimore
bal <- read.csv("Baltimore_Crime_Data.csv")
head(bal)
color <- c("red", "blue", "black", "green", "purple", "grey", "orange", "cyan", "brown", "aquamarine", "darkgoldenrod1", "lawngreen", "tan1", "gold")
years <- c(2011,2012,2013,2014,2015)
Lty <- rep(1,length(years))
png("baltimore_2011_Aug_Sept.jpg")
plot(c(1,31), c(0,300),bty='L', type = "n", xlab = "Days", ylab = "count", main = "Crime variation in August and September in 2014")
cdate <- bal$CrimeDate#[CH$test_d.OFFENSE_CATEGORY_ID=="ARSON"]
cdate <- as.Date(cdate,"%m/%d/%y")
df <- data.frame(date = cdate, year = as.numeric(format(cdate, format = "%Y")), month = as.numeric(format(cdate, format = "%m")), day = as.numeric(format(cdate, format = "%d")))
for (i in 8:9){
  day <- df$day[df$year==2014 & df$month==8]
  lines(table(day), type = "o", col=color[i])
}
legend("topleft", years, col = c("red","blue"), lty = c(1,2), legend = c("August","September"))
dev.off()


##Atlanta
atlanta <- read.csv("Atlanta_Data_Consolidated.csv")
head(atlanta)
cdate <- atlanta$Report.Date #[atlanta$Neigborhood=="Downtown"]
cdate <- as.Date(cdate,"%m/%d/%Y")
df <- data.frame(date = cdate, year = as.numeric(format(cdate, format = "%Y")), month = as.numeric(format(cdate, format = "%m")), day = as.numeric(format(cdate, format = "%d")))
years <- c(2011,2012,2013,2014,2015)
color <- c("red", "black", "green", "purple", "cyan")
png("Atlanta_DT_crime_evolution_febraury.jpg")
plot(c(1,31), c(0,170),bty='L', type = "n", xlab = "Month", ylab = "count", main = "Crime Evolution in Atlanta over the Years in Febraury")
for (i in 1:length(years)){
  day <- df$day[df$year==years[i] & df$month==2]
  print(table(day))
  lines(table(day), type = "o", col=color[i])
}
legend("topleft", years, col = color, lty = rep(1,length(years)), legend = years)
dev.off()

