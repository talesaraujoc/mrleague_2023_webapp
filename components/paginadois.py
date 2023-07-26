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


# Pré Layout

card = dbc.Card(
    dbc.CardBody(
        [
            dbc.RadioItems(options=competicoes, value=competicoes[0], id='radio-01-liga-copa', inline=True, style={'margin-top':'40px', 'margin-left':'35px', 'padding-left':'60px'}),
            
            html.H4('Rodada:', style={'margin-top':'70px'}),
            dcc.Dropdown(id='dpd-01-rodada'),
            
            html.Hr(),
            
            html.H4('Critério:', style={'margin-top':'220px'}),
            dcc.Dropdown(options=lista_criterio, value=lista_criterio[0], id='dpd-02-criterios') 
        ]
    ),
style={'height':'100vh'})

# Layout
app.layout = html.Div([
    dbc.Row([
        dbc.Col([],sm=1),
        
        dbc.Col(card,sm=2),
        
        dbc.Col([
            dbc.Row(dcc.Graph(id='fig_c1'), style={'margin-bottom':'10px'}),
            dbc.Row(dcc.Graph(id='fig_c2'), style={'margin-bottom':'10px'}),
            dbc.Row(dcc.Graph(id='grafico-rodada-goleiro'))
        ], sm=9)
    ], style={'margin':'10px'})
])


# Callbacks
@app.callback(
    Output('dpd-01-rodada', 'options'),
    Input('radio-01-liga-copa', 'value')
)
def update_drop_um(selection):
    if selection == 'LIGA':
        return lista_rodadas_liga
    else:
        return lista_rodadas_copa

@app.callback(
    Output('dpd-01-rodada', 'value'),
    Input('dpd-01-rodada', 'options')
)
def set_rodada(available_options):
    return available_options[0]

@app.callback(
    Output('fig_c1', 'figure'),
    Input('radio-01-liga-copa', 'value'),
    Input('dpd-01-rodada', 'value'),
)
def update_grafico_01_c1(competicao, rodada):
    if competicao == 'LIGA':
        df_target = df_season.loc[df_season['COMPETIÇÃO']=='LIGA']
        df_target = df_target.loc[df_target['RODADA']==rodada]
        df_target = df_target.groupby('TIME').agg({'V':'sum', 'E':'sum', 'D':'sum'})/6
        df_target = df_target.reset_index()
        
        df_target_b = df_season.loc[df_season['COMPETIÇÃO']=='LIGA']
        df_target_b = df_target_b.loc[df_target_b['RODADA']==rodada]
        df_target_b = df_target_b.groupby('PLAYER').agg({'PTS':'sum'})
        df_target_b = df_target_b.reset_index()
        df_target_b = df_target_b.sort_values(by=['PTS'], ascending=False)
        
        fig = make_subplots(rows=1, cols=2, subplot_titles=('V/E/D', 'PTS'))
        
        fig.add_trace(go.Bar(x=df_target['TIME'], y=df_target['V'], marker=dict(color='#3ADE3E'), name='Vitórias'), row=1, col=1)
        fig.add_trace(go.Bar(x=df_target['TIME'], y=df_target['E'], marker=dict(color='#EAE5B4'), name='Empates'), row=1, col=1)
        fig.add_trace(go.Bar(x=df_target['TIME'], y=df_target['D'], marker=dict(color='#F52D2A'), name='Derrotas'), row=1, col=1)
        
        fig.add_trace(go.Bar(x=df_target_b['PLAYER'], y=df_target_b['PTS'], name="PTS", marker=dict(color='#000000')), row=1, col=2)
        
        return fig
    else:
        df_target = df_season.loc[df_season['COMPETIÇÃO']=='COPA']
        df_target = df_target.loc[df_target['RODADA']==rodada]
        df_target = df_target.groupby('TIME').agg({'V':'sum', 'E':'sum', 'D':'sum'})/6
        df_target = df_target.reset_index()

        df_target_b = df_season.loc[df_season['COMPETIÇÃO']=='COPA']
        df_target_b = df_target_b.loc[df_target_b['RODADA']==rodada]
        df_target_b = df_target_b.groupby('PLAYER').agg({'PTS':'sum'})
        df_target_b = df_target_b.reset_index()
        df_target_b = df_target_b.sort_values(by=['PTS'], ascending=False)
        
        fig = make_subplots(rows=1, cols=2, subplot_titles=('V/E/D', 'PTS'))
        
        fig.add_trace(go.Bar(x=df_target['TIME'], y=df_target['V'], marker=dict(color='#3ADE3E'), name='Vitórias'), row=1, col=1)
        fig.add_trace(go.Bar(x=df_target['TIME'], y=df_target['E'], marker=dict(color='#EAE5B4'), name='Empates'), row=1, col=1)
        fig.add_trace(go.Bar(x=df_target['TIME'], y=df_target['D'], marker=dict(color='#F52D2A'), name='Derrotas'), row=1, col=1)
        
        fig.add_trace(go.Bar(x=df_target_b['PLAYER'], y=df_target_b['PTS'], name="PTS", marker=dict(color='#000000')), row=1, col=2)
        
        return fig

@app.callback(
    Output('fig_c2', 'figure'),
    Input('radio-01-liga-copa', 'value'),
    Input('dpd-01-rodada', 'value'),
    Input('dpd-02-criterios', 'value')
)
def update_grafico_02_c2(competicao, rodada, criterios):
    if competicao == 'LIGA':
        df_scouts_individuais_por_rodada = df_liga.loc[df_liga['RODADA']==rodada]
        df_scouts_individuais_por_rodada = df_scouts_individuais_por_rodada.groupby('PLAYER').agg({'GOL':'sum', 'ASS':'sum', 'STG':'sum', 'GC':'sum', 'AMA':'sum', 'AZUL':'sum', 'VER':'sum', 'PP':'sum', 'FALTA':'sum'})
        df_scouts_individuais_por_rodada = df_scouts_individuais_por_rodada.reset_index()
        df_gol = df_scouts_individuais_por_rodada.sort_values(by=['GOL'], ascending=False)
        df_ass = df_scouts_individuais_por_rodada.sort_values(by=['ASS'], ascending=False)
        df_outros = df_scouts_individuais_por_rodada.sort_values(by=[criterios], ascending=False)

        fig = make_subplots(rows=1, cols=3, subplot_titles=('GOLS', 'ASSISTS', criterios))
        
        fig.add_trace(go.Bar(x=df_gol['PLAYER'], y=df_gol['GOL'], showlegend=False, marker=dict(color='#4FDAE8')), row=1, col=1)
        fig.add_trace(go.Bar(x=df_ass['PLAYER'], y=df_ass['ASS'], showlegend=False, marker=dict(color='#5589DB')), row=1, col=2)
        fig.add_trace(go.Bar(x= df_outros['PLAYER'], y= df_outros[criterios], showlegend=False, marker=dict(color='#9054E8')), row=1, col=3)
        
        return fig
    
    else:
        df_scouts_individuais_por_rodada = df_copa.loc[df_liga['RODADA']==rodada]
        df_scouts_individuais_por_rodada = df_scouts_individuais_por_rodada.groupby('PLAYER').agg({'GOL':'sum', 'ASS':'sum', 'STG':'sum', 'AMA':'sum', 'AZUL':'sum', 'VER':'sum', 'FALTA':'sum'})
        df_scouts_individuais_por_rodada = df_scouts_individuais_por_rodada.reset_index()
        df_gol = df_scouts_individuais_por_rodada.sort_values(by=['GOL'], ascending=False)
        df_ass = df_scouts_individuais_por_rodada.sort_values(by=['ASS'], ascending=False)
        df_outros = df_scouts_individuais_por_rodada.sort_values(by=[criterios], ascending=False)

        fig = make_subplots(rows=1, cols=3, subplot_titles=('GOLS', 'ASSISTS', criterios))
        
        fig.add_trace(go.Bar(x=df_gol['PLAYER'], y=df_gol['GOL'], showlegend=False, marker=dict(color='#4FDAE8')), row=1, col=1)
        fig.add_trace(go.Bar(x=df_ass['PLAYER'], y=df_ass['ASS'], showlegend=False, marker=dict(color='#5589DB')), row=1, col=2)
        fig.add_trace(go.Bar(x= df_outros['PLAYER'], y= df_outros[criterios], showlegend=False, marker=dict(color='#9054E8')), row=1, col=3)
        
        
        return fig
    
@app.callback(
    Output('grafico-rodada-goleiro','figure'),
    Input('radio-01-liga-copa', 'value'),
    Input('dpd-01-rodada', 'value'),
)

def update_figure(competicao, rodada):
    df_rodada_x = df_season.loc[df_season['COMPETIÇÃO']==competicao]
    df_rodada_x = df_rodada_x.loc[df_rodada_x['RODADA']==rodada]
    df_rodada_gks = df_rodada_x.loc[df_rodada_x['POSIÇÃO']=='GK']
    df_rodada_gks = df_rodada_gks.groupby('PLAYER').agg({'V':'sum', 'E':'sum', 'D':'sum', 'GOL':'sum', 'ASS':'sum', 'STG':'sum', 'GC':'sum', 'AMA':'sum', 'AZUL':'sum', 'VER':'sum', 'PP':'sum', 'GS':'sum', 'DD':'sum', 'DP':'sum','FALTA':'sum', 'PTS':'sum'}).reset_index()
    df_rodada_gks = df_rodada_gks.sort_values(by='PTS',ascending=False)
    
    fig_gk = px.bar(df_rodada_gks, x='PLAYER', y=['V', 'E', 'D', 'GS', 'STG','DD'], barmode="group")
    


    return fig_gk
        