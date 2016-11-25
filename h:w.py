'''create a new column for home/away'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import the dataframe
df = pd.read_csv('whole_data_lebron.csv')


ha = df['Unnamed: 5']

# transform @ to 0/1 for ease of analyzing
l = []
for x in ha:
    # @ means away
    if x == "@":
        l.append('0')
    else:
        l.append('1')

print(l)
l = pd.Series(l)


# create a new column in df
df['home/away'] = l
df.to_csv('whole_data_lebron1.csv')


#print(df['home/away'])