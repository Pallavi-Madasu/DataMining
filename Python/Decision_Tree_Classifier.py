import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import cross_validation
from sklearn import ensemble
from sklearn.naive_bayes import GaussianNB

# Encode strings to integers
def encode_crimeType(df):
    df_new = df.copy()
    unique_crime_types = df_new["Crime Type"].unique()
    crime_type_int = {name: n for n, name in enumerate(unique_crime_types)}
    df_new["crime_type_int"] = df_new["Crime Type"].replace(crime_type_int)   
    return df_new

# Visualize Decision Tree
def drawDecisionTree(model,feature_names):
    with open("dt.dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f, feature_names = features, filled = True) 
        command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
        try:
            subprocess.check_call(command)
        except:
            exit("could not run dot, ie graphviz, to produce visualization, please run the command again separately")


df = pd.read_csv("~/Desktop/My DM/Baltimore/Baltimore.csv",low_memory=False)
#df_new = encode_crimeType(df)

features = ["Month of the Crime","Mean Temperature","Mean Dew Point","Mean Visibility","Max Humidity","Mean Wind Speed","Max Sea Level"]

X = df[features]
Y = df["Crime Type"]

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=200)

print '--Decision Tree--'
clf = tree.DecisionTreeClassifier(min_samples_split=25000, random_state=99)
clf = clf.fit(X, Y)
scores = cross_validation.cross_val_score(clf, X, Y, cv=5)
print 'Cross Validation : '+str(scores.mean())
clf1 = tree.DecisionTreeClassifier(min_samples_split=25000, random_state=99).fit(X_train, Y_train)
print 'Random Split : '+str(clf1.score(X_test, Y_test))

drawDecisionTree(clf,features)




