
'''algorithm to append two rating columns to the original player file'''
import pandas
import matplotlib.pyplot as plt
import numpy as np


def appendnrtg(df_lebron, df_rating):
              l = []
              k = []
              t = df_rating['Team']              
              # change names to abbs to match to player file
              t = t.str.replace('Atlanta Hawks','ATL').replace('Brooklyn Nets','BRK').replace('Boston Celtics','BOS').replace('Charlotte Hornets','CHA').replace('Chicago Bulls','CHI').replace('Cleveland Cavaliers','CLE').replace('Dallas Mavericks','DAL').replace('Denver Nuggets','DEN').replace('Detroit Pistons','DET').replace('Golden State Warriors','GSW').replace('Houston Rockets','HOU').replace('Indiana Pacers','IND').replace('Los Angeles Clippers','LAC').replace('Los Angeles Lakers','LAL').replace('Memphis Grizzlies','MEM').replace('Miami Heat','MIA').replace('Milwaukee Bucks','MIL').replace('Minnesota Timberwolves','MIN').replace('New Orleans Pelicans','NOP').replace('New York Knicks','NYK').replace('Oklahoma City Thunder','OKC').replace('Orlando Magic','ORL').replace('Philadelphia 76ers','PHI').replace('Phoenix Suns','PHO').replace('Portland Trail Blazers','POR').replace('Sacramento Kings','SAC').replace('San Antonio Spurs','SAS').replace('Toronto Raptors','TOR').replace('Utah Jazz','UTA').replace('Washington Wizards','WAS').replace('Seattle SuperSonics','SEA').replace('New Orleans Hornets','NOH').replace('New Jersey Nets','NJN').replace('Charlotte Bobcats','CHA').replace('New Orleans/Oklahoma City Hornets', 'NOK')
              
              nrtg = df_rating['NRtg']
              nrtga = df_rating['NRtg/A']          
              # loop through the opponents array and team array
              for opp in df_lebron['Opp']:
                            for team in t:
                                          
                                          if team == opp:
                                                        # find index of the team in the team array
                                                        i = list(t).index(team)                                                        
                                                        
                                                        # get values using the index
                                                        x = nrtg[i]
                                                        y = nrtga[i]
                                                        l.append(x)
                                                        k.append(y)
              
              df_lebron['nrtg'] = pandas.Series(l)              
              df_lebron['nrtga'] = pandas.Series(k)
              

