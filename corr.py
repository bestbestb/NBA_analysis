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
df_corr['nrtg'] = df['nrtg']
df_corr['nrtga'] = df['nrtga']
df_corr['fanduel_points'] = df['fanduel_points']
df_corr['home/away'] = df['home/away']

#print(df_corr)
#print(df_corr.corr())


'''
nrtg     nrtga  fanduel_points  home/away
nrtg            1.000000  0.995377        0.037819  -0.001136
nrtga           0.995377  1.000000        0.039224  -0.001805
fanduel_points  0.037819  0.039224        1.000000  -0.016659
home/away      -0.001136 -0.001805       -0.016659   1.000000

table result shows theres no correlation between nrtg and fanduel points/home and away...

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

#plt.plot(l)
#plt.boxplot(l)
plt.plot(l)
plt.show()
'''
came up with scales based on the plots $ min/max/median
'''

k = []

for f in fanduel:
    
    if f > 40:
        x = 'A'
        
    if f <= 40:
        x = 'E'
            
    k.append(x)
#print(k)
k = pd.Series(k)
df_corr['fanduel_points'] = k

df_corr = df_corr[['nrtg', 'nrtga', 'home/away', 'fanduel_points']]
print(df_corr)

array = df_corr.values
#print(array)  
        
X = array[:,0:3]
Y = array[:,3]

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

