import pandas
import matplotlib.pyplot as plt
import numpy as np


df1 = pandas.read_csv('lebron15-16.csv')
# remove the games lebron did not play
new_df1 = (df1[df1['GS'] == '1'])
df2 = pandas.read_csv('lebron16.csv')
# the '1' is an int for the second csv... took me a while to realize
new_df2 = (df2[df2['GS'] == 1])
new_df = new_df1.append(new_df2, ignore_index=True)



l = []
for i in range(0, len(new_df)):
    
    assists = int((new_df.iloc[i]['AST']))
    blocks = int((new_df.iloc[i]['BLK']))
    turnovers = int((new_df.iloc[i]['TOV']))
    points = int((new_df.iloc[i]['PTS']))
    rebounds = int((new_df.iloc[i]['TRB']))
    steals = int((new_df.iloc[i]['STL']))
    
    # calculate the Fanduel points.
    total_points = assists*1.5+blocks*2+points+rebounds*1.2+steals*2-turnovers
    l.append(total_points)


# simple graph.  I did not draw a regression line because with this much fluctuation it won't be very useful; we need more information on why his performance fluctuates.

plt.plot(l)
plt.show()



    
