from ast import Eq
from distutils.log import debug
from msilib.schema import Component
from multiprocessing.sharedctypes import Value
from operator import index, length_hint
from tabnanny import check
from matplotlib.pyplot import legend
from numpy import NaN, equal, isin
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from dash import Dash, html, dcc
import dash
from dash import Input, Output
import numpy as np
import pandas as pd
from pytz import country_names

# df = pd.read_csv('Worldwide country-level data.csv')
df = px.data.gapminder()
# dff=df.replace('',np.nan)
# df= df.dropna(inplace=True)
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# c_data=df['iso_alpha_3']
# country=c_data.dropna()
# d_data=df["date"]
# d_date=d_data.dropna()
# da_data=df['deaths']
# deaths_data=da_data.dropna()

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
#            "iso_alpha_3"]]
print(df)
