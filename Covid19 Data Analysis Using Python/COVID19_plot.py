import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import sys
sys.path.append("C:\\Users\\ithaca\\Documents\\Py4e\\Covid19 Data Analysis Using Python\\fig")
from figP import LD_line
print('modules are imported')

dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(dataset_url)
df = df[df.Confirmed > 0]

# Global spread of Covid19
fig = px.choropleth(df , locations = 'Country' , locationmode = 'country names', color='Confirmed', animation_frame='Date')
fig.update_layout(title_text = 'Globle Spread of COVID 19')
fig.show()

# Normalized daily increase of COVID 19 in the Netherlands
df_N = df[df.Country == 'Netherlands']
df_N['Daily New Cases'] = df_N.Confirmed.diff()
df_N['Daily New Deaths'] = df_N.Deaths.diff()

df_N['Daily New Cases'] = df_N['Daily New Cases']/df_N['Daily New Cases'].max()
df_N['Daily New Deaths'] = df_N['Daily New Deaths']/df_N['Daily New Deaths'].max()

ST_date = '2021-01-23'
AF_date = '2021-02-23'

fig = px.line(df_N, x = 'Date', y = ['Daily New Cases', 'Daily New Deaths'],
              title = 'Normalized daily increase of COVID 19 in the Netherlands')
LD_line(fig, df_N, ST_date, AF_date)
