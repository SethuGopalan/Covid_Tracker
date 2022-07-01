
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

import dash_bootstrap_components as dbc

#data section
df = pd.read_csv('Worldwide country-level data.csv')
dff = df.dropna(axis=1, thresh=2)
data1 = dff['iso_alpha_3']
data2 = data1.dropna()
data3 = dff['deaths']
data4 = data3.dropna()

data5 = df[['iso_alpha_3', "date", "confirmed",
            "deaths", "recovered"]].drop_duplicates()
data6 = data5.dropna()


app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = dbc.Container([
# header section

    dbc.Row([
        dbc.Col(html.H3('Covid Data Dashboard',
                className='text-center text-info, mb-4'))
    ]),
    html.Br(),
# Dropdown
    dbc.Row([
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id="my_dropdown",
                    options=[{'label': i, 'value': i}
                             for i in data2.unique()],

                    value=["USA"],
                    multi=True,),
            ], width={'size': 5, 'offset': 0}),
        ], justify='center'),
        dbc.Row([
            dbc.Col([
                html.Div(id="div_text", style={'textAlign': 'center'})
            ]),
        ]),
        dbc.Row([
            dbc.Col([]),
        ]),

        html.Br(),
# Table view
        dbc.Row([
            dbc.Col([
                dash_table.DataTable(
                    data=data6.to_dict('records'),
                    columns=[{"id": i, "name": i, }
                             for i in data6.columns

                             ],
                    fixed_rows={'headers': True},
                    style_table={'maxhight': '100px', 'maxwidth': 3},
                    page_size=12,
                    style_header={
                        'backgroundColor': 'white', 'border': '4px solid white'},
                    style_data_conditional=[
                        {'if': {'column_id': 'iso_alpha_3'},
                         'backgroundColor': 'dodgerblue',
                         'color': 'white',
                         },
                        {'if': {'column_id': 'date'},
                         'backgroundColor': 'tomato',
                         'color': 'white',
                         },
                        {'if': {'column_id': 'confirmed'},
                         'backgroundColor': 'hotpink',
                         'color': 'white',
                         },
                        {'if': {'column_id': 'recovered'},
                         'backgroundColor': 'RebeccaPurple',
                         'color': 'white',
                         },
                        {'if': {'column_id': 'deaths'},
                         'backgroundColor': '#3D9970',
                         'color': 'white',
                         },
                    ],
                    style_cell={
                        'textAlign': 'center'
                    },


                ),
            ], width={'size': 5, 'offset': 1}),
            dbc.Col([

                dcc.Graph(id="graph1"),
            ], width={'size': 5, 'offset': 0}),


        ]),
    ], justify='center'),
    html.Br(),

    dbc.Row([

        dbc.Col([

            dcc.Graph(id="graph2"),



        ], width={'size': 5, 'offset': 0}),
        dbc.Col([

            dcc.Graph(id="graph3"),


        ], width={'size': 5, 'offset': 0})



    ], justify='center'),



], fluid=True)

# callback
@ app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Output("div_text", "children"),
    Input("my_dropdown", "value"))
# call back Function
def filter_scatter(country):

    dff = df[df['iso_alpha_3'].isin(country)]
    # df_data = df.pivot(dff, "date", 'deaths')
    fig1 = px.scatter_geo(dff, locations='iso_alpha_3',  color="iso_alpha_3", hover_name='iso_alpha_3', hover_data=['deaths', 'date', 'confirmed', 'recovered'], animation_group='iso_alpha_3'

                          )
    fig1.update_traces(marker=dict(size=20), showlegend=True,
                       selector=dict(type='scattergeo'), mode='lines+markers+text')
    fig2 = px.imshow(dff, labels=dict(
        x='{} is selected'.format(str(country)[1:-1]), y='{} Covid data range'.format(str(country)[1:-1])))
    html.Br(),
    fig3 = px.scatter(dff, x='date', y='deaths', color="iso_alpha_3",
                      hover_name='iso_alpha_3', hover_data=['deaths', 'date', 'confirmed', 'recovered'])

    return fig1, fig2, fig3, html.Div('{}selected'.format(str(country)[1:-1]))


if __name__ == "__main__":
    app.run_server(debug=True)
