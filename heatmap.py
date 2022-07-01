import dash_bootstrap_components as dbc
from ast import Eq
from distutils.log import debug
from ensurepip import bootstrap
from msilib.schema import Component
from multiprocessing.sharedctypes import Value
from operator import index, length_hint
from tabnanny import check
from matplotlib.pyplot import legend
from numpy import equal, isin
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from dash import Dash, html, dcc
import dash
from dash import Input, Output, dash_table
import numpy as np
import pandas as pd

# app = dash.Dash()
# df = pd.read_csv('Worldwide country-level data.csv')
# # df = px.data.gapminder()
# table=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# # dff = df.drop_duplicates()
# # c_data = df['iso_alpha_3']
# # # country=c_data.dropna()
# # d_data = df["date"]
# # d_date = d_data.dropna()
# # da_data = df['deaths']
# # deaths_data = da_data.dropna()
# # table=pd.pivot_table(df,values='lifeExp',index=['lifeExp'])

# # df = df.pivot_table('country', 'lifeExp', 'lifeExp'),
# fig = px.imshow(df)
# fig.show()


# if __name__ == "__main__":
#     app.run_server(debug=True)
import plotly.express as px
data = [[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
fig = px.imshow(data,
                labels=dict(x="Day of Week", y="Time of Day",
                            color="Productivity"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                y=['Morning', 'Afternoon', 'Evening']
                )
fig.update_xaxes(side="top")
fig.show()
