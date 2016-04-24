import pandas as pd
import numpy as np
from sklearn import cross_validation
from sklearn import ensemble


df = pd.read_csv("~/Desktop/My DM/Baltimore/Baltimore.csv",low_memory=False)

features = ["Month of the Crime","Mean Temperature","Mean Dew Point","Mean Visibility","Max Humidity","Mean Wind Speed","Max Sea Level"]

X = df[features]
Y = df["Crime Type"]

print '--Training the calssifier--'
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=200)

# Using Gini
print '--Random Forest - Gini--'
clf_rf1 = ensemble.RandomForestClassifier(10,"gini").fit(X_train, Y_train)
print 'Random Split : '+str(clf_rf1.score(X_test, Y_test))

# Using Entropy
print '--Random Forest - Entropy--'
clf_rf2 = ensemble.RandomForestClassifier(10,"entropy").fit(X_train, Y_train)
print 'Random Split : '+str(clf_rf2.score(X_test, Y_test))



