
from numpy import equal, isin
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from dash import Dash, html, dcc
import dash
from dash import Input, Output, dash_table
import numpy as np
import pandas as pd
import dash_bootstrap_components as dbc

# data input

df = px.data.gapminder()
dff = df.dropna(axis=1, thresh=2)

Table_value = df[['country', 'continent', 'year', 'lifeExp', 'gdpPercap']]


app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = dbc.Container([
    # Header section

    dbc.Row([
        dbc.Col([html.H1("Global GDP and LifeExp data up to Year 2007", className='text-center text-info, mb-4',

                         ),


                 ]),


    ]),
    html.Br(),
    html.Br(),
    # slider
    dbc.Row([

        dbc.Col([
            dcc.Slider(
                id="my_slider",
                min=dff['year'].min(),
                max=dff['year'].max(),
                value=dff['year'].min(),
                marks={str(year): str(year)
                       for year in dff['year'].unique()},



            ),


        ], width={'size': 6, 'offset': 0}),
        # dropdrown

        dbc.Col([
            dcc.Dropdown(
                id="my_dropdown",
                options=[{'label': i, 'value': i}
                         for i in df['continent'].unique()],

                value=["Asia"],
                multi=True,),
        ], width={'size': 6, 'offset': 0}),

    ], justify='around'),
    html.Br(),

    dbc.Row([
        html.Div(id="mytext", style={'textAlign': 'center'}),

    ], justify='center'),

    html.Br(),
    html.Br(),
    html.Br(),
    # graph1
    dbc.Row([

            dbc.Col([dcc.Graph(id="graph1"),
                     ], width={'size': 5, 'offset': 0}),

            # graph2
            dbc.Col([dcc.Graph(id="graph2"),

                     ], width={'size': 5, 'offset': 0}),

            dbc.Col([dcc.Graph(id="graph3"),

                     ], width={'size': 5, 'offset': 0}),


            ], justify='around'),
    html.Br(),
    html.Br(),

    # Table View
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                data=Table_value.to_dict('records'),
                columns=[{"id": i, "name": i, }
                         for i in Table_value.columns

                         ],
                fixed_rows={'headers': True},
                style_table={'maxhight': '100px', 'maxwidth': 3},
                page_size=5,
                style_header={
                    'backgroundColor': 'white', 'border': '4px solid white'},
                style_data_conditional=[
                    {'if': {'column_id': 'country'},
                     'backgroundColor': 'dodgerblue',
                     'color': 'white',
                     },
                    {'if': {'column_id': 'continent'},
                     'backgroundColor': 'tomato',
                     'color': 'white',
                     },
                    {'if': {'column_id': 'year'},
                     'backgroundColor': 'hotpink',
                     'color': 'white',
                     },
                    {'if': {'column_id': 'lifeExp'},
                     'backgroundColor': 'RebeccaPurple',
                     'color': 'white',
                     },
                    {'if': {'column_id': 'gdpPercap'},
                     'backgroundColor': '#3D9970',
                     'color': 'white',
                     },
                ],
                style_cell={
                    'textAlign': 'center'
                },


            ),
        ], width={'size': 10, 'offset': 1}),

    ]),


], fluid=True)
# callback


@ app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Output('mytext', 'children'),
    Input("my_slider", "value"),
    Input("my_dropdown", "value"))
# callback function
def update_Graph(slider_value, drop_value):

    d_value = df.loc[(df['year'] == slider_value)
                     & df['continent'].isin(drop_value)]
    # print(d_value)
    fig1 = px.scatter(d_value, x="gdpPercap", y="lifeExp",
                      color='country',  size="pop", size_max=65)
    fig1.update_xaxes(showline=True, linewidth=2,
                      linecolor='black')
    fig1.update_yaxes(showline=True, linewidth=2, linecolor='black')

    fig2 = px.imshow(d_value, aspect='auto', labels=dict(x='{}is selected'.format(str(drop_value)[1:-1]), y=' Year{} is Selected '.format(slider_value), color='{}'.format(str(drop_value)[1:-1])),
                     )
    theta = dff.columns
    fig3 = px.line_polar(dff,  theta=theta,  color=theta,
                         line_shape='linear', line_close=True, markers=True)
    fig3.update_traces(fill='toself')

    return fig1, fig2, fig3, html.Div("Selected Year is {} and selected Continent is{}".format(slider_value, (str(drop_value)[1:-1]))),


if __name__ == "__main__":
    app.run_server(debug=True)
