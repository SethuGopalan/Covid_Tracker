from ast import Eq
from distutils.log import debug
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
from dash import Input, Output
import numpy as np
import pandas as pd
from pytz import country_names

df = pd.read_csv('Worldwide country-level data.csv')
dff = df.dropna(axis=1, thresh=2)
data1 = dff['iso_alpha_3']
data2 = data1.dropna()
data3 = dff['deaths']
data4 = data3.dropna()
data5 = df['id']


app = dash.Dash()

app.layout = html.Div(id='parent', children=[

    html.Div(
        dcc.Dropdown(
            id="my_dropdown",
            options=[{'label': i, 'value': i}
                     for i in data2.unique()],
            # options=["IND", "USA", "CAN"],

            value=["USA"],
            multi=True,


        ), style={'width': '50%'}


    ),


    html.Div(id='dropdown'),
    dcc.Graph(id="graph1"),
    dcc.Graph(id="graph2"),
    dcc.Graph(id="graph3")

])


@app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Input("my_dropdown", "value"))
def filter_scatter(country):

    dff = df[df['iso_alpha_3'].isin(country)]
    fig1 = px.scatter_geo(dff, locations='iso_alpha_3', color="iso_alpha_3", hover_name='iso_alpha_3', hover_data=['deaths', 'date', 'confirmed', 'recovered'], animation_group='iso_alpha_3'

                          )
    fig2 = px.imshow(dff, labels=dict(x="data", y="Value"), )
    html.Br(),
    fig3 = px.scatter(dff, x='date', y='deaths', color="iso_alpha_3",
                      hover_name='iso_alpha_3', hover_data=['deaths', 'date', 'confirmed', 'recovered'])
    return fig1, fig2, fig3


if __name__ == "__main__":
    app.run_server(debug=True)
