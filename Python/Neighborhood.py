import pandas as pd
import numpy as np
import argparse
import math

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def separate (path, lat, lon, lat_lim, lon_lim):
    
    #print "pd.read_csv(path,dtype=pd.DataFrame)"
    df_city = pd.read_csv(path,dtype=pd.DataFrame)

    exec("df_city."+lat+".fillna(0,inplace=True)")
    exec("df_city."+lon+".fillna(0,inplace=True)")
    
    exec("df_X_temp = df_city."+lat)
    exec("df_Y_temp = df_city."+lon)

    df_X = df_X_temp[df_X_temp.notnull()]
    df_Y = df_Y_temp[df_Y_temp.notnull()]

    min_lon = np.float64(pd.Series.min(df_Y[(abs(np.float64(df_Y)) > 1.0) & (abs(np.float64(df_Y)) < lon_lim)]))
    max_lon = np.float64(pd.Series.max(df_Y[(abs(np.float64(df_Y)) > 1.0) & (abs(np.float64(df_Y)) < lon_lim)]))

##    print min_lon
##    print max_lon
    
    min_lat = np.float64(pd.Series.min(df_X[(abs(np.float64(df_X)) > 1.0) & (abs(np.float64(df_X)) > lat_lim)]))
    max_lat = np.float64(pd.Series.max(df_X[(abs(np.float64(df_X)) > 1.0) & (abs(np.float64(df_X)) > lat_lim)]))

##    print min_lat
##    print max_lat
    
    step_lat = (max_lat - min_lat)/10
    step_lon = (max_lon - min_lon)/10

##    print step_lat
##    print step_lon
    
    lat_seg = [i for i in np.arange(min_lat,max_lat+(step_lat/2),step_lat)]
    lon_seg = [j for j in np.arange(min_lon,max_lon+(step_lon/2),step_lon)]
    
    crime_per_neighborhood = [[0 for i in range(len(lat_seg)-1)] for j in range(len(lon_seg)-1)]

    print lat_seg
    print lon_seg
    print len(df_X)
    total = 0

##    print df_X
##    print df_Y
    
    for i in df_X.index.values:
    #for i in range(10):
        flag = 0
        for j in range(len(lat_seg)-1):
            #print str(df_X[i]) + str(lat_seg[j]) + str(lat_seg[j+1])
            if (((isclose(np.float64(df_X[i]), lat_seg[j], rel_tol = 1e-5)) or (abs(np.float64(df_X[i])) > abs(lat_seg[j]))) and (isclose(np.float64(df_X[i]), lat_seg[j+1], rel_tol = 1e-5) or (abs(np.float64(df_X[i])) < abs(lat_seg[j+1])))):
                #print "Lat Okay"
                for k in range(len(lon_seg)-1):
                    #print str(df_Y[i]) + str(lon_seg[k]) + str(lon_seg[k+1])
                    if (((isclose(np.float64(df_Y[i]), lon_seg[k], rel_tol = 1e-5)) or (abs(np.float64(df_Y[i])) > abs(lon_seg[k]))) and (isclose(np.float64(df_Y[i]), lon_seg[k+1], rel_tol = 1e-5) or (abs(np.float64(df_Y[i])) < abs(lon_seg[k+1])))):
                        crime_per_neighborhood[j][k] += 1
                        total += 1
                        flag = 1
                        break;
                break;
            
##        if flag == 0:
##            print "skipped = " + str(i)
##            print "lat = " + str(df_X[i])
##            print "lon = " + str(df_Y[i])
##            print lat_seg
##            print lon_seg
##            print "\n"

    print total
    
    for i in range(len(lat_seg)-1):
        print crime_per_neighborhood[i]
        
    return

def combined (path, coord, lat_lim, lon_lim):
    
    df_city = pd.read_csv(path,dtype=pd.DataFrame)

    exec("df_city."+coord+".fillna('(0, 0)',inplace=True)")
    
    exec("df_X_temp = np.asarray([0.0 for i in range(len(df_city."+coord+"))])")
    exec("df_Y_temp = np.asarray([0.0 for i in range(len(df_city."+coord+"))])")
    
    for i in range(len(df_X_temp)):
        exec("df_X_temp[i] = np.float64(df_city."+coord+"[i].split(', ')[0].split('(')[1])")
        exec("df_Y_temp[i] = np.float64(df_city."+coord+"[i].split(', ')[1].split(')')[0])")

    df_X_temp = pd.core.series.Series(df_X_temp)
    df_Y_temp = pd.core.series.Series(df_Y_temp)

    df_X = df_X_temp[df_X_temp.notnull()]
    df_Y = df_Y_temp[df_Y_temp.notnull()]

##    print df_X
##    print df_Y
    
    min_lon = np.float64(df_Y[pd.Series.idxmin(abs(df_Y[(abs(np.float64(df_Y)) > 1.0) & (abs(np.float64(df_Y)) < lon_lim)]))])
    max_lon = np.float64(df_Y[pd.Series.idxmax(abs(df_Y[(abs(np.float64(df_Y)) > 1.0) & (abs(np.float64(df_Y)) < lon_lim)]))])

    print min_lon
    print max_lon
    
    min_lat = np.float64(df_X[pd.Series.idxmin(abs(df_X[(abs(np.float64(df_X)) > 1.0) & (abs(np.float64(df_X)) > lat_lim)]))])
    max_lat = np.float64(df_X[pd.Series.idxmax(abs(df_X[(abs(np.float64(df_X)) > 1.0) & (abs(np.float64(df_X)) > lat_lim)]))])

    print min_lat
    print max_lat
    
    step_lat = (max_lat - min_lat)/10
    step_lon = (max_lon - min_lon)/10

##    print step_lat
##    print step_lon
    
    lat_seg = [i for i in np.arange(min_lat,max_lat+(step_lat/2),step_lat)]
    lon_seg = [j for j in np.arange(min_lon,max_lon+(step_lon/2),step_lon)]
    
    crime_per_neighborhood = [[0 for i in range(len(lon_seg)-1)] for j in range(len(lat_seg)-1)]

    print lat_seg
    print lon_seg
    print len(df_X)
    total = 0
##
##    print df_X
##    print df_Y
    
    for i in df_X.index.values:
    #for i in range(10):
        flag = 0
        for j in range(len(lat_seg)-1):
            #print str(df_X[i]) + str(lat_seg[j]) + str(lat_seg[j+1])
            if (((isclose(np.float64(df_X[i]), lat_seg[j], rel_tol = 1e-5)) or (abs(np.float64(df_X[i])) > abs(lat_seg[j]))) and (isclose(np.float64(df_X[i]), lat_seg[j+1], rel_tol = 1e-5) or (abs(np.float64(df_X[i])) < abs(lat_seg[j+1])))):
                #print "Lat Okay"
                for k in range(len(lon_seg)-1):
                    #print str(df_Y[i]) + str(lon_seg[k]) + str(lon_seg[k+1])
                    if (((isclose(np.float64(df_Y[i]), lon_seg[k], rel_tol = 1e-5)) or (abs(np.float64(df_Y[i])) > abs(lon_seg[k]))) and (isclose(np.float64(df_Y[i]), lon_seg[k+1], rel_tol = 1e-5) or (abs(np.float64(df_Y[i])) < abs(lon_seg[k+1])))):
                        crime_per_neighborhood[j][k] += 1
                        total += 1
                        flag = 1
                        break;
                break;
            
##        if flag == 0:
##            print "skipped = " + str(i)
##            print "lat = " + str(df_X[i])
##            print "lon = " + str(df_Y[i])
##            print lat_seg
##            print lon_seg
##            print "\n"

    print total
    
    for i in range(len(lat_seg)-1):
        print crime_per_neighborhood[i]

def zipcode (path, zipcode):
    
    df_city = pd.read_csv(path,dtype=pd.DataFrame)

    exec("df_city."+zipcode+".fillna('0',inplace=True)")
    
    exec("df_zip_temp = df_city."+zipcode)

    df_zip_temp = df_zip_temp[(df_zip_temp != '0') & (df_zip_temp != '`')]
    df_zip = pd.Series.unique(df_zip_temp)

    crime_per_neighborhood = pd.Series([[0 for i in range(2)] for j in range(len(df_zip))])
    
    for i in range(len(df_zip)):
        crime_per_neighborhood[i][0] = df_zip[i]
        crime_per_neighborhood[i][1] = 0

    for i in df_zip_temp.index.values:
        crime_per_neighborhood[int(np.where(df_zip == df_zip_temp[i])[0])][1] += 1

    for i in range(len(df_zip)):
        print crime_per_neighborhood[i]
    
                            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DCrime per neighborhood Analysis')
    parser.add_argument('--path', type=str,
                            help="CSV file name",
                            required=True)
    parser.add_argument('--loc', type=str,
                            help="Location attribute name",
                            default="",
                            required=False)
    parser.add_argument('--X', type=str,
                            help="Latitude attribute name",
                            default="",
                            required=False)
    parser.add_argument("--Y", type=str, 
                            help="Longitude attribute name",
                            default="", 
                            required=False)
    parser.add_argument("--zip", type=str, 
                            help="Zipcode attribute name",
                            default="", 
                            required=False)
    args = parser.parse_args()

    if 'Baltimore' in args.path:
        lat_lim = 41.0
    elif 'SFO' in args.path:
        lat_lim = 90.0
    elif 'Chicago' in args.path:
        lat_lim = 39.0
    else:
        lat_lim = 20.0

    if 'Baltimore' in args.path:
        lon_lim = 70.0
    elif 'SFO' in args.path:
        lon_lim = 121.0
    elif 'Chicago' in args.path:
        lon_lim = 90.0
    else:
        lon_lim = 130.0
        
    if (args.loc == "") and ((args.X == "") or (args.Y == "")) and (args.zip == ""):
        print "Either both X and Y coordinates or combined coordinates or zipcode required"

    elif (args.X != "") and (args.Y != ""):
        separate(args.path,args.X,args.Y,lat_lim,lon_lim)
        
    elif (args.zip != ""):
        zipcode(args.path,args.zip)
        
    else:
        combined(args.path,args.loc,lat_lim,lon_lim)  

