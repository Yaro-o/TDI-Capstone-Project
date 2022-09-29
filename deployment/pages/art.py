from dash import dcc, html,register_page
import dash_bootstrap_components as dbc
from assets.texts import *
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, path='/art', name='State-of-the-Art Predictive Models', order=6)
padd_ = 20

df_p = pd.read_csv('Data/art.csv', usecols=['ts', 'y', 'silverkite', 'silverkite_mean_train', 'silverkite_mean_test', 'silverkite_std_train', 'silverkite_std_test', 
    'prophet', 'prophet_mean_train', 'prophet_mean_test', 'prophet_std_train', 'prophet_std_test'])


mean_train = np.round(df_p['prophet_mean_train'].mean(),1)
mean_test = np.round(df_p['prophet_mean_test'].mean(),1)
std_train = np.round(df_p['prophet_std_train'].mean(),1)
std_test = np.round(df_p['prophet_std_test'].mean(),1)

fig_art_1 = go.Figure()
l = df_p.shape[0]
fig_art_1.add_trace(go.Scatter(x=list(df_p.ts), y=df_p['y'], mode='lines+markers'))
for i in range(1,13,1):
    fig_art_1.add_trace(go.Scatter(x=list(df_p.iloc[l-(i+1)*7 : l-(i+1)*7+7].ts), y=df_p[l-(i+1)*7 : l-(i+1)*7+7]['prophet'], mode='lines+markers', 
        line=dict(color='Red',), name='CV'))

fig_art_1.update_layout(title="Prophet", 
    xaxis_title="Date", yaxis_title="Number of Injuries")

for j in range(1,13,1):
    x_temp = df_p['ts'].iloc[l-(j+1)*7]
    fig_art_1.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_art_1.add_annotation(x=x_temp, y=75, text="CV # " + str(13-j), showarrow=True, arrowhead=3)

fig_art_1.add_trace(go.Scatter(x=list(df_p.iloc[l-7 : l-1].ts), y=df_p[l-7 : l-1]['prophet'], mode='lines+markers', line=dict(color='Green',), name='Prediction'))
x_temp = df_p['ts'].iloc[l-7]
fig_art_1.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Green',), xref='x', yref='y', opacity=0.5)
fig_art_1.add_annotation(x=x_temp, y=75, text="Prediction", showarrow=True, arrowhead=3)
x_temp = df_p['ts'].iloc[l-10*7]
fig_art_1.add_annotation(text=f'''Scoring Method: Mean Absolute Error
<br>12-Fold Cross Validation Results:
<br>Mean Train Scores: {mean_train}, Standard Deviation of Train Scores: {std_train}
<br>Mean CV Scores: {mean_test}, Standard Deviation of CV Scores: {std_test}''', 
    x=x_temp, y=280, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_art_1.update_yaxes(range=[0,300])
fig_art_1.update_layout(showlegend=False, template='plotly_white')

mean_train = np.round(df_p['silverkite_mean_train'].mean(),1)
mean_test = np.round(df_p['silverkite_mean_test'].mean(),1)
std_train = np.round(df_p['silverkite_std_train'].mean(),1)
std_test = np.round(df_p['silverkite_std_test'].mean(),1)

fig_art_2 = go.Figure()
l = df_p.shape[0]
fig_art_2.add_trace(go.Scatter(x=list(df_p.ts), y=df_p['y'], mode='lines+markers'))
for i in range(1,13,1):
    fig_art_2.add_trace(go.Scatter(x=list(df_p.iloc[l-(i+1)*7 : l-(i+1)*7+7].ts), y=df_p[l-(i+1)*7 : l-(i+1)*7+7]['silverkite'], mode='lines+markers', 
        line=dict(color='Red',), name='CV'))

fig_art_2.update_layout(title="Prophet", 
    xaxis_title="Date", yaxis_title="Number of Injuries")

for j in range(1,13,1):
    x_temp = df_p['ts'].iloc[l-(j+1)*7]
    fig_art_2.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_art_2.add_annotation(x=x_temp, y=75, text="CV # " + str(13-j), showarrow=True, arrowhead=3)

fig_art_2.add_trace(go.Scatter(x=list(df_p.iloc[l-7 : l-1].ts), y=df_p[l-7 : l-1]['silverkite'], mode='lines+markers', line=dict(color='Green',), name='Prediction'))
x_temp = df_p['ts'].iloc[l-7]
fig_art_2.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Green',), xref='x', yref='y', opacity=0.5)
fig_art_2.add_annotation(x=x_temp, y=75, text="Prediction", showarrow=True, arrowhead=3)
x_temp = df_p['ts'].iloc[l-10*7]
fig_art_2.add_annotation(text=f'''Scoring Method: Mean Absolute Error
<br>12-Fold Cross Validation Results:
<br>Mean Train Scores: {mean_train}, Standard Deviation of Train Scores: {std_train}
<br>Mean CV Scores: {mean_test}, Standard Deviation of CV Scores: {std_test}''', 
    x=x_temp, y=280, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_art_2.update_yaxes(range=[0,300])
fig_art_2.update_layout(showlegend=False, template='plotly_white')

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("State-of-the-Art Predictive Models"),
                        html.P(text_art_1),
                        html.Div(text_art_2),
                        html.P(text_art_3),
                    ]), style={'padding': padd_}
            ),
        ),
        dbc.Row(
            [
                dbc.Col(
                        dcc.Tabs(value='1',
                            children = 
                            [
                                dcc.Tab(value='1', children = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_art_1, style={'height': '60vh'})]), 
                                    className="mt-4", color="info", outline=True), label="Meta's Prophet"),
                                dcc.Tab(value='2', children = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_art_2, style={'height': '60vh'})]), 
                                    className="mt-4", color="info", outline=True), label="LinkedIn's Silverkite"),
                            ]
                        ),
                    style={'padding': padd_, 'textAlign': 'center', "widht": '100%'}),
            ]
        ),
    ]
)