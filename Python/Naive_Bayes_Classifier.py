from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
from sklearn import cross_validation

print '---------- Naive Bayes -----------'

df = pd.read_csv("~/Desktop/My DM/Baltimore/Baltimore.csv",low_memory=False)

features = ["Month of the Crime","Mean Temperature","Mean Dew Point","Mean Visibility","Max Humidity","Mean Wind Speed","Max Sea Level"]

x = df[features]
y = df["Crime Type"]

print 'Partial Fit - training classifier'
clf_pf = GaussianNB()
clf_pf.partial_fit(x, y, np.unique(y))

print '--Cross Validation--'
scores = cross_validation.cross_val_score(clf_pf, x, y, cv=5)
print scores.mean()

print '--Random Split--'
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(x, y, test_size=0.2, random_state=0)
clf1 = GaussianNB().fit(X_train, Y_train)
print clf1.score(X_test, Y_test)

# Test file
df_test = pd.read_csv("~/Desktop/My DM/Baltimore/Test_Baltimore.csv",low_memory=False)
xt = df_test[features]
print 'Partial Fit Predicted - '+str(clf_pf.predict(xt))
print 'Predict Probability - '+str(clf_pf.predict_proba(xt))
