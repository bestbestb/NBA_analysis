import pandas as pd
import numpy as np
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
# import the dataframe
df = pd.read_csv('whole_data_lebron.csv')

# make a new df for correlation analysis
df_corr = pd.DataFrame()
df_corr['ORtg_diff'] = df['ORtg_diff']
df_corr['DRtg_diff'] = df['DRtg_diff']
df_corr['NRtg_diff'] = df['NRtg_diff']
df_corr['NRtg/A_diff'] = df['NRtg/A_diff']
df_corr['nrtg'] = df['nrtg']
df_corr['nrtga'] = df['nrtga']
df_corr['home/away'] = df['home/away']
df_corr['fanduel_points'] = df['fanduel_points']

#print(df_corr)
print(df_corr.corr())


'''
                ORtg_diff  DRtg_diff  NRtg_diff  NRtg/A_diff      nrtg  \
ORtg_diff        1.000000  -0.358948   0.808316     0.813511 -0.533085   
DRtg_diff       -0.358948   1.000000  -0.839655    -0.831279  0.559600   
NRtg_diff        0.808316  -0.839655   1.000000     0.997738 -0.663275   
NRtg/A_diff      0.813511  -0.831279   0.997738     1.000000 -0.657180   
nrtg            -0.533085   0.559600  -0.663275    -0.657180  1.000000   
nrtga           -0.536307   0.541136  -0.653501    -0.653294  0.995377   
home/away        0.009218   0.025027  -0.010421    -0.009989 -0.001136   
fanduel_points  -0.004483  -0.120200   0.073169     0.079327  0.037819   

                   nrtga  home/away  fanduel_points  
ORtg_diff      -0.536307   0.009218       -0.004483  
DRtg_diff       0.541136   0.025027       -0.120200  
NRtg_diff      -0.653501  -0.010421        0.073169  
NRtg/A_diff    -0.653294  -0.009989        0.079327  
nrtg            0.995377  -0.001136        0.037819  
nrtga           1.000000  -0.001805        0.039224  
home/away      -0.001805   1.000000       -0.016659  
fanduel_points  0.039224  -0.016659        1.000000  


table result shows theres a weak correlation between fanduel points and DRtg_diff  

'''


'''trying ML'''

fanduel = df_corr['fanduel_points']
min_f = min(fanduel)
max_f = max(fanduel)
l = fanduel.tolist()
#create levels for fanduel points
fanduel_level = []
# min = 14.1
print(min_f)
#ma = 90.1
print(max_f)
# mean = 47.3
print(np.median(l))
m = np.median(l)
#plt.plot(l)
#plt.boxplot(l)
plt.plot(l)
plt.show()
'''
came up with scales based on the plots $ min/max/median
'''

k = []

for f in fanduel:
    # testing if the result will be greater or smaller than m
    if f > m:
        x = 'A'
      
    if f <= m:
        x = 'E'
            
    k.append(x)
#print(k)
k = pd.Series(k)
df_corr['fanduel_points'] = k

df_corr = df_corr[['ORtg_diff', 'DRtg_diff', 'NRtg_diff', 'NRtg/A_diff', 'nrtg', 'nrtga', 'home/away', 'fanduel_points']]
print(df_corr)

array = df_corr.values
#print(array)  
        
X = array[:,0:7]
Y = array[:,7]

validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = cross_validation.train_test_split(X, Y, test_size=validation_size, random_state=seed)

num_folds = 10
num_instances = len(X_train)
seed = 7
scoring = 'accuracy'


# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for (name, model) in models:
	kfold = cross_validation.KFold(n=num_instances, n_folds=num_folds, random_state=seed)
	cv_results = cross_validation.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

'''
LDA: 0.510901 (0.035752)
KNN: 0.448631 (0.029267)
CART: 0.429975 (0.061766)
NB: 0.510901 (0.035752)
SVM: 0.504989 (0.039934)
...no correlation shown
'''

# what now?
# - predict the amount of minutes a player spends on the floor
# - over/under
# - A high O/U should be at least 206 points, and can sometimes go all the way up to 225 points. These totals are often times set when the Kings or Warriors are involved, because these are the two teams that play at the fastest pace in the NBA.
# - points spreads: whether the game will be close or not. A large point spread is usually an indication that you shouldn't pay up for superstars on either team, i.e they will be put to bench to save energy. maye target substitue players like Spurs behemoth center Boban Marjanovic.
# For cash games, you need 5x the salary (so a $9,000 player would need 45 points to reach "value"), but in tournaments you should be looking for players that could potentially hit 6x or even 7x.
# correlation between players eg. perfect pair
# WOWY analysis: player's usage rates when certain units are on the court. 
# contrarian

# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))


'''
# after  changing the measure to 40 we get 0.73 correction rate

[1265 rows x 8 columns]
LR: 0.758853 (0.036470)
LDA: 0.751922 (0.036351)
KNN: 0.757833 (0.032732)
CART: 0.714473 (0.035367)
NB: 0.758853 (0.036470)
SVM: 0.766783 (0.032390)
0.758893280632
[[174  14]
 [ 47  18]]
             precision    recall  f1-score   support

          A       0.79      0.93      0.85       188
          E       0.56      0.28      0.37        65

avg / total       0.73      0.76      0.73       253


but after changing to 47.3 we only get 0.54 correction rate

LR: 0.567181 (0.042787)
LDA: 0.577014 (0.043821)
KNN: 0.576053 (0.029609)
CART: 0.567103 (0.043981)
NB: 0.508921 (0.064217)
SVM: 0.581062 (0.037172)
0.541501976285
[[61 60]
 [56 76]]
             precision    recall  f1-score   support

          A       0.52      0.50      0.51       121
          E       0.56      0.58      0.57       132

avg / total       0.54      0.54      0.54       253
'''