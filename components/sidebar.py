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
                html.H1("736 - Finanças", className="text-primary"),
                html.P("Web APP", className="text-info"),
                html.Hr(),
                
        # Seção Nav ======================
                html.Hr(),
                
                dbc.Nav([
                        dbc.NavLink("Menu Geral", href="/pag_1", active="exact"), 
                         
                        dbc.NavLink("Rodadas", href="/pag_2", active="exact")
                        ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom":"50px"}),
    

                ], id='sidebar_completa')

