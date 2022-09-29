from dash import dcc, html, register_page
import dash_bootstrap_components as dbc
from assets.texts import *
import pandas as pd
import plotly.graph_objects as go

register_page(__name__, path='/ml', name='Machine Learning Predictive Models', order=5)
padd_ = 20

df_p = pd.read_csv('Data/art.csv', usecols=['ts', 'y', 'linreg', 'linreg_mean_train', 'linreg_mean_test', 'linreg_std_train', 'linreg_std_test', 
    'logreg', 'logreg_mean_train', 'logreg_mean_test', 'logreg_std_train', 'logreg_std_test',
    'xgb', 'xgb_mean_train', 'xgb_mean_test', 'xgb_std_train', 'xgb_std_test'])

# Linear Regression:
l = df_p.shape[0]
fig_ml_1 = go.Figure()
fig_ml_1.add_trace(go.Scatter(x=list(df_p.ts), y=df_p['y'], mode='lines+markers'))
for i in range(1,13,1):
    fig_ml_1.add_trace(go.Scatter(x=list(df_p.iloc[l-(i+1)*7 : l-(i+1)*7+7].ts), y=df_p[l-(i+1)*7 : l-(i+1)*7+7]['linreg'], mode='lines+markers', 
        line=dict(color='Red',), name='CV'))
fig_ml_1.update_layout(title="Linear Regression", 
    xaxis_title="Date", yaxis_title="Number of Injuries")
for j in range(1,13,1):
    x_temp = df_p['ts'].iloc[l-(j+1)*7]
    fig_ml_1.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_ml_1.add_annotation(x=x_temp, y=75, text="CV # " + str(13-j), showarrow=True, arrowhead=3)
fig_ml_1.add_trace(go.Scatter(x=list(df_p.iloc[l-7 : l-1].ts), y=df_p[l-7 : l-1]['linreg'], mode='lines+markers', line=dict(color='Green',), name='Prediction'))
x_temp = df_p['ts'].iloc[l-7]
fig_ml_1.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Green',), xref='x', yref='y', opacity=0.5)
fig_ml_1.add_annotation(x=x_temp, y=75, text="Prediction", showarrow=True, arrowhead=3)
x_temp = df_p['ts'].iloc[l-10*7]
fig_ml_1.add_annotation(text=f'''Scoring Method: Mean Absolute Error
<br>12-Fold Cross Validation Results:
<br>Mean Train Scores: {df_p.linreg_mean_train.iloc[0]}, Standard Deviation of Train Scores: {df_p.linreg_std_train.iloc[0]}
<br>Mean CV Scores: {df_p.linreg_mean_test.iloc[0]}, Standard Deviation of CV Scores: {df_p.linreg_std_test.iloc[0]}''', 
    x=x_temp, y=280, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_ml_1.update_yaxes(range=[0,300])
fig_ml_1.update_layout(showlegend=False, template='plotly_white')

# Logistic Regression:
l = df_p.shape[0]
fig_ml_2 = go.Figure()
fig_ml_2.add_trace(go.Scatter(x=list(df_p.ts), y=df_p['y'], mode='lines+markers'))
for i in range(1,13,1):
    fig_ml_2.add_trace(go.Scatter(x=list(df_p.iloc[l-(i+1)*7 : l-(i+1)*7+7].ts), y=df_p[l-(i+1)*7 : l-(i+1)*7+7]['logreg'], mode='lines+markers', 
        line=dict(color='Red',), name='CV'))
fig_ml_2.update_layout(title="Logistic Regression", 
    xaxis_title="Date", yaxis_title="Number of Injuries")
for j in range(1,13,1):
    x_temp = df_p['ts'].iloc[l-(j+1)*7]
    fig_ml_2.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_ml_2.add_annotation(x=x_temp, y=75, text="CV # " + str(13-j), showarrow=True, arrowhead=3)
fig_ml_2.add_trace(go.Scatter(x=list(df_p.iloc[l-7 : l-1].ts), y=df_p[l-7 : l-1]['logreg'], mode='lines+markers', line=dict(color='Green',), name='Prediction'))
x_temp = df_p['ts'].iloc[l-7]
fig_ml_2.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Green',), xref='x', yref='y', opacity=0.5)
fig_ml_2.add_annotation(x=x_temp, y=75, text="Prediction", showarrow=True, arrowhead=3)
x_temp = df_p['ts'].iloc[l-10*7]
fig_ml_2.add_annotation(text=f'''Scoring Method: Mean Absolute Error
<br>12-Fold Cross Validation Results:
<br>Mean Train Scores: {df_p.logreg_mean_train.iloc[0]}, Standard Deviation of Train Scores: {df_p.logreg_std_train.iloc[0]}
<br>Mean CV Scores: {df_p.logreg_mean_test.iloc[0]}, Standard Deviation of CV Scores: {df_p.logreg_std_test.iloc[0]}''', 
    x=x_temp, y=280, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_ml_2.update_yaxes(range=[0,300])
fig_ml_2.update_layout(showlegend=False, template='plotly_white')

# XGBoost:
l = df_p.shape[0]
fig_ml_3 = go.Figure()
fig_ml_3.add_trace(go.Scatter(x=list(df_p.ts), y=df_p['y'], mode='lines+markers'))
for i in range(1,13,1):
    fig_ml_3.add_trace(go.Scatter(x=list(df_p.iloc[l-(i+1)*7 : l-(i+1)*7+7].ts), y=df_p[l-(i+1)*7 : l-(i+1)*7+7]['xgb'], mode='lines+markers', 
        line=dict(color='Red',), name='CV'))
fig_ml_3.update_layout(title="XGBoost", 
    xaxis_title="Date", yaxis_title="Number of Injuries")
for j in range(1,13,1):
    x_temp = df_p['ts'].iloc[l-(j+1)*7]
    fig_ml_3.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_ml_3.add_annotation(x=x_temp, y=75, text="CV # " + str(13-j), showarrow=True, arrowhead=3)
fig_ml_3.add_trace(go.Scatter(x=list(df_p.iloc[l-7 : l-1].ts), y=df_p[l-7 : l-1]['xgb'], mode='lines+markers', line=dict(color='Green',), name='Prediction'))
x_temp = df_p['ts'].iloc[l-7]
fig_ml_3.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Green',), xref='x', yref='y', opacity=0.5)
fig_ml_3.add_annotation(x=x_temp, y=75, text="Prediction", showarrow=True, arrowhead=3)
x_temp = df_p['ts'].iloc[l-10*7]
fig_ml_3.add_annotation(text=f'''Scoring Method: Mean Absolute Error
<br>12-Fold Cross Validation Results:
<br>Mean Train Scores: {df_p.xgb_mean_train.iloc[0]}, Standard Deviation of Train Scores: {df_p.xgb_std_train.iloc[0]}
<br>Mean CV Scores: {df_p.xgb_mean_test.iloc[0]}, Standard Deviation of CV Scores: {df_p.xgb_std_test.iloc[0]}''', 
    x=x_temp, y=280, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_ml_3.update_yaxes(range=[0,300])
fig_ml_3.update_layout(showlegend=False, template='plotly_white')

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("Machine Learning Predictive Models"),
                        html.P(text_ml_1),
                        html.P(text_ml_5),
                        html.Div(text_ml_6),
                        html.Div(text_ml_7),
                    ]), style={'padding': padd_}
            ),
        ),
        dbc.Row(
            [
                dbc.Col(
                        dcc.Tabs(value='1',
                            children =
                            [
                                dcc.Tab(value='1', children = dbc.Card(dbc.CardBody([html.P(text_ml_2, style={'textAlign': 'left'}),
                                    dcc.Graph(figure=fig_ml_1, style={'height': '60vh'})]), 
                                        className="mt-4", color="info", outline=True), label="Linear Regression"),
                                dcc.Tab(value='2', children = dbc.Card(dbc.CardBody([html.P(text_ml_3, style={'textAlign': 'left'}),
                                    dcc.Graph(figure=fig_ml_2, style={'height': '60vh'})]), 
                                        className="mt-4", color="info", outline=True), label="Logistic Regression"),
                                dcc.Tab(value='3', children = dbc.Card(dbc.CardBody([html.P(text_ml_4, style={'textAlign': 'left'}),
                                    dcc.Graph(figure=fig_ml_3, style={'height': '60vh'})]), 
                                        className="mt-4", color="info", outline=True), label="XGBoost"),
                            ]
                        ),
                        style={'padding': padd_, 'textAlign': 'center', "widht": '100%'}
                        ),
            ]
        ),
    ]
)