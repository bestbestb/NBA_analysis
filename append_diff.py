'''algorithm to append difference between rating columns to the original player file'''
import pandas
import matplotlib.pyplot as plt
import numpy as np


def appenddiff(df_lebron, df_rating):
              l = []
              k = []
              j = []
              h = []
              t = df_rating['Team']              
              # change names to abbs to match to player file
              t = t.str.replace('Atlanta Hawks','ATL').replace('Brooklyn Nets','BRK').replace('Boston Celtics','BOS').replace('Charlotte Hornets','CHA').replace('Chicago Bulls','CHI').replace('Cleveland Cavaliers','CLE').replace('Dallas Mavericks','DAL').replace('Denver Nuggets','DEN').replace('Detroit Pistons','DET').replace('Golden State Warriors','GSW').replace('Houston Rockets','HOU').replace('Indiana Pacers','IND').replace('Los Angeles Clippers','LAC').replace('Los Angeles Lakers','LAL').replace('Memphis Grizzlies','MEM').replace('Miami Heat','MIA').replace('Milwaukee Bucks','MIL').replace('Minnesota Timberwolves','MIN').replace('New Orleans Pelicans','NOP').replace('New York Knicks','NYK').replace('Oklahoma City Thunder','OKC').replace('Orlando Magic','ORL').replace('Philadelphia 76ers','PHI').replace('Phoenix Suns','PHO').replace('Portland Trail Blazers','POR').replace('Sacramento Kings','SAC').replace('San Antonio Spurs','SAS').replace('Toronto Raptors','TOR').replace('Utah Jazz','UTA').replace('Washington Wizards','WAS').replace('Seattle SuperSonics','SEA').replace('New Orleans Hornets','NOH').replace('New Jersey Nets','NJN').replace('Charlotte Bobcats','CHA').replace('New Orleans/Oklahoma City Hornets', 'NOK')
              
              ortg = df_rating['ORtg']
              drtga = df_rating['DRtg']
              nrtg = df_rating['NRtg']
              nrtga = df_rating['NRtg/A']
              # find index of CLE
              i_CLE = list(t).index('CLE')
              # get the ratings of CLE
              x1 = ortg[i_CLE]
              y1 = drtga[i_CLE]
              a1 = nrtg[i_CLE]
              b1 = nrtga[i_CLE]
              
              
              # loop through the opponents array and team array
              for opp in df_lebron['Opp']:
                            for team in t:
                                          
                                          if team == opp:
                                                        # find index of the team in the team array
                                                        i = list(t).index(team)                                                        
                                                        
                                                        # get values using the index
                                                        x2 = ortg[i]
                                                        y2 = drtga[i]
                                                        a2 = nrtg[i]
                                                        b2 = nrtga[i]
                                                        
                                                        # get the difference
                                                        x = x1 - x2
                                                        y = y1 - y2
                                                        a = a1 - a2
                                                        b = b1 - b2
                                                        
                                                        l.append(x)
                                                        k.append(y)
                                                        j.append(a)
                                                        h.append(b)
                                                        
              
              df_lebron['ORtg_diff'] = pandas.Series(l)              
              df_lebron['DRtg_diff'] = pandas.Series(k)
              df_lebron['NRtg_diff'] = pandas.Series(j)
              df_lebron['NRtg/A_diff'] = pandas.Series(h)
              
import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

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



#append columns for each lebron df
appenddiff(df16, df_rating_16)
# draft pick starts in may, so games of 1516 will use rating of 2015
appenddiff(df1516, df_rating_15)
appenddiff(df15, df_rating_15)
appenddiff(df1415, df_rating_14)
appenddiff(df14, df_rating_14)
appenddiff(df1314, df_rating_13)
appenddiff(df13, df_rating_13)
appenddiff(df1213, df_rating_12)
appenddiff(df12, df_rating_12)
appenddiff(df1112, df_rating_11)
appenddiff(df11, df_rating_11)
appenddiff(df1011, df_rating_10)
appenddiff(df10, df_rating_10)
appenddiff(df0910, df_rating_09)
appenddiff(df09, df_rating_09)
appenddiff(df0809, df_rating_08)
appenddiff(df08, df_rating_08)
appenddiff(df0708, df_rating_07)
appenddiff(df07, df_rating_07)
appenddiff(df0607, df_rating_06)
appenddiff(df06, df_rating_06)
appenddiff(df0506, df_rating_05)

appenddiff(df0405, df_rating_04)

appenddiff(df0304, df_rating_03)

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

new_df.to_csv('diff_data_lebron.csv')