import pandas
import matplotlib.pyplot as plt
import numpy as np

# read all the csv files for different years for lebron
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

'''turn each object of the gs column into str type
def turn_gs_str(dataframe):
    dataframe['GS']:
'''        
    
# make a list of all the dataframes with strings in GS column
df_list_1 = [df1213, df1314, df1415, df1516]

# remove the games lebron did not play
def trans_df(da):
    da.applymap(str)
    da = (da[(da['GS']) == '1'])
    return da

df1213 = trans_df(df1213)
df1314 = trans_df(df1314)
df1415 = trans_df(df1415)
df1516 = trans_df(df1516)
    


    

frames = [df0304, df0405, df0506, df06, df0607, df07, df0708, df08, df0304, df0809, df09, df0910, df10, df1011, df11, df1112, df12, df1213, df13, df1314, df14, df1415, df15, df1516, df16]

new_df = pandas.concat(frames, ignore_index=True)

new_df.to_csv('whole_data_lebron.csv')

l = []
for i in range(0, len(new_df)):
    AST = new_df.iloc[i]['AST']
   
    #AST = AST[np.logical_not(np.isnan(AST))]

    assists = float(AST)
    blocks = float((new_df.iloc[i]['BLK']))
    turnovers = float((new_df.iloc[i]['TOV']))
    points = float((new_df.iloc[i]['PTS']))
    rebounds = float((new_df.iloc[i]['TRB']))
    steals = float((new_df.iloc[i]['STL']))
    
    # calculate the Fanduel points.
    total_points = assists*1.5+blocks*2+points+rebounds*1.2+steals*2-turnovers
    l.append(total_points)


# simple graph.  I did not draw a regression line because with this much fluctuation it won't be very useful; we need more information on why his performance fluctuates.

plt.plot(l)
plt.show()



    
