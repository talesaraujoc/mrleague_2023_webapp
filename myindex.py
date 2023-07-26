from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from globals import *
from app import *
from components import sidebar, pag_1, pag_2



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
    if pathname == "/" or pathname == "/pag_1": 
        return pag_1.layout

    if pathname == "/pag_2":
        return pag_2.layout
        

if __name__ == '__main__':
    app.run_server(debug=True)
    
  