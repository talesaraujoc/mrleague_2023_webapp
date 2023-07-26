from dash import dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

import pandas as pd
import numpy as np

import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from globals import *
from app import app




# Pré-layout ===========================

card_total_partidas = dbc.Card(
    [
        dbc.CardImg(src="/assets/image_1.png", top=True, style={'max-width':'58px','max-height':'58px', 'padding-left':'20px', 'padding-top':'20px'}),
        dbc.CardBody(
            [
                html.H5("Partidas", className="card-title"),
                html.H2(n_partidas_totais)
            ]
        ),
    ],
    style={"width": "18rem"},
)

card_total_gols = dbc.Card(
    [
        dbc.CardImg(src="/assets/bola_simbolo_card.png", top=True, style={'max-width':'45px','max-height':'45px', 'padding-left':'20px', 'padding-top':'20px'}),
        dbc.CardBody(
            [
                html.H5("Gols", className="card-title"),
                html.H2(n_gols_temporada)
            ]
        ),
    ],
    style={"width": "18rem"},
)

card_lider_atual = dbc.Card(
    [
        dbc.CardImg(src="/assets/trofeu.png", top=True, style={'max-width':'45px','max-height':'45px', 'padding-left':'20px', 'padding-top':'20px'}),
        dbc.CardBody(
            [
                html.H5("1° geral", className="card-title"),
                html.H2(lider_geral)
                
            ]
        ),
    ],
    style={"width": "18rem"},
)

card_n_rodadas = dbc.Card(
    [
        dbc.CardImg(src="/assets/n_rodadas.png", top=True, style={'max-width':'45px','max-height':'45px', 'padding-left':'20px', 'padding-top':'20px'}),
        dbc.CardBody(
            [
                html.H5("N° de rodadas|Liga", className="card-title"),
                html.H2(n_rodadas_liga)
            ]
        ),
    ],
    style={"width": "18rem"},
)

card_n_copas = dbc.Card(
    [
        dbc.CardImg(src="/assets/n_rodadas.png", top=True, style={'max-width':'45px','max-height':'45px', 'padding-left':'20px', 'padding-top':'20px'}),
        dbc.CardBody(
            [
                html.H5("N° de rodadas|Copa", className="card-title"),
                html.H2(n_rodadas_copa)
            ]
        ),
    ],
    style={"width": "18rem"},
)

fig_corrida_geral = px.bar(df_corrida_geral, x='PLAYER', y='PTS', title='PONTUAÇÃO GERAL')
#fig_corrida_geral.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

fig_top_cinco_artilheiros = px.bar(df_top_cinco_artilheiros, x='PLAYER', y='GOL', title='TOP 5 - ARTILHEIRO')
fig_top_cinco_ass = px.bar(df_top_cinco_assistencia, x='PLAYER', y='ASS', title='TOP 5 - ASSISTS')
fig_gks = px.bar(df_goleiros_gs, x='PLAYER', y=['GS','STG', 'DD'], barmode="group", title='GKs - GS / STG / DDs')

# Layout ===============================
layout = dbc.Container(
    dbc.Row([
        
        dbc.Col([
            dbc.Row([html.H3("TEMPORADA 2023", style={'padding':'20px'})]),
            dbc.Row([
                dbc.Col([], sm=1),
                dbc.Col(dbc.Card(card_total_partidas, color="primary", style={"opacity": 0.9}), sm=2),
                dbc.Col(dbc.Card(card_total_gols, color='secondary', style={"opacity": 0.9}), sm=2),
                dbc.Col(dbc.Card(card_lider_atual, color='success', style={"opacity": 0.9}), sm=2),
                dbc.Col(dbc.Card(card_n_rodadas, color='warning', style={"opacity": 0.9}), sm=2),
                dbc.Col(dbc.Card(card_n_copas, color='#64A9DE', style={"opacity": 0.9}), sm=2),
                dbc.Col([], sm=1)
                ], style={'padding-bottom':'20px'}),
            dbc.Row([dcc.Graph(figure=fig_corrida_geral)], style={}),
            dbc.Row([dbc.Col([dcc.Graph(figure=fig_top_cinco_artilheiros)], sm=4), dbc.Col([dcc.Graph(figure=fig_top_cinco_ass)], sm=4), dbc.Col([dcc.Graph(figure=fig_gks)], sm=4)], style={'margin-top':'15px'})
                ], sm=12)
    ], style={'margin':'10px'}),
    fluid=True, style={'height': '100%'})