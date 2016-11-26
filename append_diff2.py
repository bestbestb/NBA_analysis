'''algorithm to append difference between rating columns to the original player file'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('whole_data_lebron.csv')
df_diff = pd.read_csv('diff_data_lebron.csv')

# Assumption: if offense of both teams are high and defense of both teams are low, then lebron has a higher chance of a good performance

# again, ortg_diff is the diff between CLE and opponent team's ortg
df['ORtg_diff'] = df_diff['ORtg_diff']
df['DRtg_diff'] = df_diff['DRtg_diff']
df['NRtg_diff'] = df_diff['NRtg_diff']
df['NRtg/A_diff'] = df_diff['NRtg/A_diff']

df.to_csv('whole_data_lebron.csv')



