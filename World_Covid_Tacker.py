from ast import Eq
from distutils.log import debug
from msilib.schema import Component
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


app = dash.Dash()

app.layout = html.Div(id='parent', children=[

    html.H1(id='H1', children='Covid Data Tracker World wide'),
    dcc.Graph(id="graph"),
    dcc.Dropdown(
        id="my_dropdown",
        options=[{'label': i, 'value': i}for i in df["iso_alpha_3"].unique()],
        value="USA",
        multi=True,

    ),
    html.Div(id='my-dropdown'),
    html.Br(),

])


@app.callback(
    Output("my-dropdown", "children"),
    Input("my_dropdown", "value")
)
def update_dropdown(update_value):
    df = pd.read_csv('Worldwide country-level data.csv')
    # dff = df.loc[df['country']==(update_value)]
    df[df['iso_alpha_3'].isin(update_value)]

    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="iso_alpha_3", hover_data=['population', 'confirmed', 'deaths', 'recovered', ],
                            color_discrete_sequence=["fuchsia"], zoom=1, height=700, width=800)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20})
    fig.show()


if __name__ == "__main__":
    app.run_server(debug=True)
