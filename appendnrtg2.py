
import pandas
import matplotlib.pyplot as plt
import numpy as np
'''append two rating columns to the original lebron csv files'''
# read in the lebron files
df0304 = pandas.read_csv('lebron03-04.csv')
df0405 = pandas.read_csv('lebron04-05.csv')
df0506 = pandas.read_csv('lebron05-06.csv')
df06 = pandas.read_csv('lebron06.csv')
df0607 = pandas.read_csv('lebron06-07.csv')
df07 = pandas.read_csv('lebron07.csv')
df0708 = pandas.read_csv('lebron07-08.csv')
df08 = pandas.read_csv('lebron08.csv')
df0809 = pandas.read_csv('lebron08-09.csv')
df09 = pandas.read_csv('lebron09.csv')
df0910 = pandas.read_csv('lebron09-10.csv')
df10 = pandas.read_csv('lebron10.csv')
df1011 = pandas.read_csv('lebron10-11.csv')
df11 = pandas.read_csv('lebron11.csv')
df1112 = pandas.read_csv('lebron11-12.csv')
df12 = pandas.read_csv('lebron12.csv')
df1213 = pandas.read_csv('lebron12-13.csv')
df13 = pandas.read_csv('lebron13.csv')
df1314 = pandas.read_csv('lebron13-14.csv')
df14 = pandas.read_csv('lebron14.csv')
df1415 = pandas.read_csv('lebron14-15.csv')
df15 = pandas.read_csv('lebron15.csv')
df1516 = pandas.read_csv('lebron15-16.csv')
df16 = pandas.read_csv('lebron16.csv')

# read in the rating files
df_rating_16 = pandas.read_csv('team_rating_1617.csv')
df_rating_15 = pandas.read_csv('team_rating_1516.csv')
df_rating_14 = pandas.read_csv('team_rating_1415.csv')
df_rating_13 = pandas.read_csv('team_rating_1314.csv')
df_rating_12 = pandas.read_csv('team_rating_1213.csv')
df_rating_11 = pandas.read_csv('team_rating_1112.csv')
df_rating_10 = pandas.read_csv('team_rating_1011.csv')
df_rating_09 = pandas.read_csv('team_rating_0910.csv')
df_rating_08 = pandas.read_csv('team_rating_0809.csv')
df_rating_07 = pandas.read_csv('team_rating_0708.csv')
df_rating_06 = pandas.read_csv('team_rating_0607.csv')
df_rating_05 = pandas.read_csv('team_rating_0506.csv')
df_rating_04 = pandas.read_csv('team_rating_0405.csv')
df_rating_03 = pandas.read_csv('team_rating_0304.csv')
df_rating_02 = pandas.read_csv('team_rating_0203.csv')

# import the function
from appendnrtg import appendnrtg

#append columns for each lebron df
appendnrtg(df16, df_rating_16)
# draft pick starts in may, so games of 1516 will use rating of 2015
appendnrtg(df1516, df_rating_15)
appendnrtg(df15, df_rating_15)
appendnrtg(df1415, df_rating_14)
appendnrtg(df14, df_rating_14)
appendnrtg(df1314, df_rating_13)
appendnrtg(df13, df_rating_13)
appendnrtg(df1213, df_rating_12)
appendnrtg(df12, df_rating_12)
appendnrtg(df1112, df_rating_11)
appendnrtg(df11, df_rating_11)
appendnrtg(df1011, df_rating_10)
appendnrtg(df10, df_rating_10)
appendnrtg(df0910, df_rating_09)
appendnrtg(df09, df_rating_09)
appendnrtg(df0809, df_rating_08)
appendnrtg(df08, df_rating_08)
appendnrtg(df0708, df_rating_07)
appendnrtg(df07, df_rating_07)
appendnrtg(df0607, df_rating_06)
appendnrtg(df06, df_rating_06)
appendnrtg(df0506, df_rating_05)

appendnrtg(df0405, df_rating_04)

appendnrtg(df0304, df_rating_03)



# df0304.to_csv('lebron03-04.csv')
print (df1516)
#print (df0304['Opp])

