import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

from globals import *


layout = dbc.Col([
                html.H3("MR League", className="text-primary"),
                html.P("Web APP", className="text-info"),
                html.Hr(),
                
        # Seção Nav ======================
                html.Hr(),
                
                dbc.Nav([dbc.NavLink("Menu Geral", href="/paginaum", active="exact")], vertical=True, pills=True, id='nav_button_1', style={"margin-bottom":"50px"}),
                
                dbc.Nav([dbc.NavLink("Rodadas", href="/paginadois", active="exact")], vertical=True, pills=True, id='nav_button_2'),
    

                ], id='sidebar_completa')
