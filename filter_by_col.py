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
from pytz import country_names

df = pd.read_csv('Worldwide country-level data.csv')
dff = df.dropna()
# data = dff[['date', 'confirmed', 'deaths', 'recovered', 'tests', 'vaccines',
#            'people_vaccinated', 'people_fully_vaccinated', 'hosp', 'icu', 'vent',
#            'school_closing', 'workplace_closing', 'cancel_events',
#            'gatherings_restrictions', 'transport_closing', 'population',
#            'stay_home_restrictions', 'internal_movement_restrictions',
#            'international_movement_restrictions', 'information_campaigns',
#            'testing_policy', 'contact_tracing', 'facial_coverings',
#            'vaccination_policy', 'elderly_people_protection',
#            'government_response_index', 'stringency_index',
#            'containment_health_index', 'economic_support_index',
#            'administrative_area_level', 'administrative_area_level_1',
#            'administrative_area_level_2', 'administrative_area_level_3',
#            "iso_alpha_3",
#            ]].drop_duplicates()

app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id="my_dropdown",
                options=[{'label': i, 'value': i}for i in dff],
                value=['confirmed'],
                multi=True
            )
        ], width={'size': 10, 'offset': 0}),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Col([
            dcc.Graph(id='graph')
        ], width={'size': 10, 'offset': 0})

    ])
])


@app.callback(
    Output('graph', 'figure'),
    Input("my_dropdown", 'value')

)
def update_graph(input_value):
    data = df.isin(input_value)
    df_data = df.pivot(data)

    fig = px.inshow(data,'deaths')
    #  hover_name='iso_alpha_3', hover_data=['deaths', 'date', 'confirmed', 'recovered'], log_x=True, size_max=65)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
