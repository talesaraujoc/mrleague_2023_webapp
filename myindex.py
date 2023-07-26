from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from globals import *
from app import *
from components import sidebar, paginaum, paginadois



# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
                ], md=1),
        
        dbc.Col([content], md=11)
            ])
], fluid=True)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/paginaum": 
        return paginaum.layout

    if pathname == "/paginadois":
        return paginadois.layout
        

if __name__ == '__main__':
    app.run_server(debug=False)
    
  