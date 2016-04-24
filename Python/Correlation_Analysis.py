import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr,pearsonr

df = pd.read_csv("~/Desktop/My DM/Baltimore/Baltimore_Crimes_Weather.csv")
#df = pd.read_csv("~/Desktop/My DM/Louisville/Louisville_Crimes_Weather.csv")

df_new = df.copy()

def plotGraph(x,y,xlabel,ylabel,path):
    fig = plt.figure()
    plt.scatter(x,y)
    fig.suptitle('Baltimore Correlation')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(path)
    plt.show()


# Correlation with month of the crime
unique_crime_months = df_new.crime_month.unique()
crime_month_int = {name: n for n, name in enumerate(unique_crime_months)}
df_new["crime_month_int"] = df_new.crime_month.replace(crime_month_int)
crime_month_cc = np.corrcoef(df_new.ncrimes,df_new.crime_month_int)[0,1]
print 'Crime Month Correlation: '+str(crime_month_cc) # 0.286
print 'Spearman Correlation' +str(spearmanr(df.ncrimes, df.crime_month)) # 0.322
print 'Pearson Correlation' +str(pearsonr(df.ncrimes, df.crime_month)) # 0.317

# Correlation with events
unique_events = df_new.events.unique()
events_int = {name: n for n, name in enumerate(unique_events)}
df_new["events_int"] = df_new.events.replace(events_int)
events_cc = np.corrcoef(df_new.ncrimes,df_new.events_int)[0,1]
print 'Events Correlation: '+str(events_cc) # 0.018
print 'Spearman Correlation' +str(spearmanr(df_new.ncrimes, df_new.events)) # 0.027
print 'Pearson Correlation' +str(pearsonr(df_new.ncrimes, df_new.events_int)) # 0.018

# Correlation with weather parameters
print '--Correlation Coefficient---'
max_temp_cc = np.corrcoef(df.ncrimes,df.max_temp)[0,1]
mean_temp_cc = np.corrcoef(df.ncrimes,df.mean_temp)[0,1]
min_temp_cc = np.corrcoef(df.ncrimes,df.min_temp)[0,1]
max_dp_cc = np.corrcoef(df.ncrimes,df.max_dp)[0,1]
mean_dp_cc = np.corrcoef(df.ncrimes,df.mean_dp)[0,1]
min_dp_cc = np.corrcoef(df.ncrimes,df.min_dp)[0,1]
max_humidity_cc = np.corrcoef(df.ncrimes,df.max_humidity)[0,1]
mean_humidity_cc = np.corrcoef(df.ncrimes,df.mean_humidity)[0,1]
min_humidity_cc = np.corrcoef(df.ncrimes,df.min_humidity)[0,1]
max_sl_cc = np.corrcoef(df.ncrimes,df.max_sl)[0,1]
mean_sl_cc = np.corrcoef(df.ncrimes,df.mean_sl)[0,1]
min_sl_cc = np.corrcoef(df.ncrimes,df.min_sl)[0,1]
max_visibility_cc = np.corrcoef(df.ncrimes,df.max_visibility)[0,1]
mean_visibility_cc = np.corrcoef(df.ncrimes,df.mean_visibility)[0,1]
min_visibility_cc = np.corrcoef(df.ncrimes,df.min_visibility)[0,1]
max_ws_cc = np.corrcoef(df.ncrimes,df.max_ws)[0,1]
mean_ws_cc = np.corrcoef(df.ncrimes,df.mean_ws)[0,1]
cloud_cover_cc = np.corrcoef(df.ncrimes,df.cloud_cover)[0,1]
wind_dir_deg_cc = np.corrcoef(df.ncrimes,df.wind_dir_deg)[0,1]

print 'Max Temp : '+str(max_temp_cc)
print 'Mean Temp : '+str(mean_temp_cc)
print 'Min Temp : '+str(min_temp_cc)
print 'Max Dew Point : '+str(max_dp_cc)
print 'Mean Dew Point : '+str(mean_dp_cc)
print 'Min Dew Pont : '+str(min_dp_cc)
print 'Max Humidity : '+str(max_humidity_cc)
print 'Mean Humidity : '+str(mean_humidity_cc)
print 'Min Humidity : '+str(min_humidity_cc)
print 'Max Sea Level : '+str(max_sl_cc)
print 'Mean Sea Level : '+str(mean_sl_cc)
print 'Min Sea Level : '+str(min_sl_cc)
print 'Max Visibility : '+str(max_visibility_cc)
print 'Mean Visibility : '+str(mean_visibility_cc)
print 'Min Visibility : '+str(min_visibility_cc)
print 'Max Wind Speed : '+str(max_ws_cc)
print 'Mean Wind Speed : '+str(mean_ws_cc)
print 'Cloud Cover : '+str(cloud_cover_cc)
print 'Wind Dir Degrees : '+str(wind_dir_deg_cc)

plotGraph(df.mean_temp,df.ncrimes,"Temperature","Number of Crimes","~/Desktop/crimes_weather.jpg")


## Most correlated attributes are
## Positive - 1) Mean Temp, Mean Dew Point, Month of the Crime, Mean Visibility, Max Humidity
## Negative - 1) Max Sea Level, Mean Wind Speed
## Ignore Rest


##Crime Month Correlation: 0.286266339651
##Spearman CorrelationSpearmanrResult(correlation=0.32209553002975028, pvalue=9.828889809074348e-47)
##Pearson Correlation(0.31739438164050665, 2.3299714375143918e-45)
##
##Events Correlation: 0.0180833913807
##Spearman CorrelationSpearmanrResult(correlation=-0.02725295930582889, pvalue=0.23706642214512832)
##Pearson Correlation(0.018083391380715925, 0.43277373156359489)

##Max Temp : 0.549936010416
##Mean Temp : 0.554048510731
##Min Temp : 0.538827337739
##Max Dew Point : 0.508789902893
##Mean Dew Point : 0.518135442212
##Min Dew Pont : 0.518142084607
##Max Humidity : 0.173148187366
##Mean Humidity : 0.105972523862
##Min Humidity : 0.0353543136498
##Max Sea Level : -0.228658847869
##Mean Sea Level : -0.11122010022
##Min Sea Level : -0.00202921513927
##Max Visibility : 0.0206638886793
##Mean Visibility : 0.125512601325
##Min Visibility : 0.0581748703093
##Max Wind Speed : -0.152727423301
##Mean Wind Speed : -0.202719857906
##Cloud Cover : -0.039172692968
##Wind Dir Degrees : -0.0190502166256






