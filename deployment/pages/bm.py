from dash import dcc, html, register_page
import dash_bootstrap_components as dbc
from assets.texts import *
import pandas as pd
from df import df
from datetime import timedelta
import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff

from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.graphics.gofplots import qqplot
from statsmodels.tsa.stattools import acf

register_page(__name__, path='/bm', name='Baseline Predictive Models', order=4)
padd_ = 20

df = df[['CRASH DATE', 'NUMBER OF PERSONS INJURED']]
df = df.resample(rule='D', on='CRASH DATE').sum().reset_index()
df.columns = ['Date', 'y']
df = df[(df['Date'] > '2020-04-01') & (df['Date'] < '2022-07-02')]
df.reset_index(inplace=True)
df.drop(columns=['index'], inplace=True)
df['test'] = 'train'
for i in range(12):
    df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7) + timedelta(days=(i*7))), 'test'] = ('test ' + str(i+1))

# Naïve:
df['naïve'] = 0
for i in range(12):
    df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7) + timedelta(days=(i*7))), 'naïve'] = df['y'][len(df) - 1 - 12*7 + i*7]
df['naïve_mae'] = np.absolute(df['naïve'] - df['y'])
mean = np.round(np.mean(df[df['test'] != 'train'].groupby('test')['naïve_mae'].mean()), decimals = 2)
std = np.round(np.std(df[df['test'] != 'train'].groupby('test')['naïve_mae'].mean()), decimals = 2)

df_temp = df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7))]
df_temp.reset_index(inplace=True)
fig_1 = go.Figure()
fig_1.add_trace(go.Scatter(x=list(df_temp.Date), y=df_temp['y'], mode='lines+markers'))
for i in range(12):
    fig_1.add_trace(go.Scatter(x=list(df_temp.iloc[i*7:i*7+7].Date), y=df_temp[i*7:i*7+7]['naïve'], mode='lines+markers', line=dict(color='Red',)))

fig_1.update_layout(title="Prediction (naïve) vs. Target", xaxis_title="Date", yaxis_title="Number of Injuries")

for i in range(12):
    x_temp = df_temp['Date'][i*7]
    fig_1.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_1.add_annotation(x=x_temp, y=75, text="CV # " + str(i+1), showarrow=True, arrowhead=3)

fig_1.add_annotation(text=f'mean cv Scores: {mean} <br> std cv Scores: {std}', 
                   x='2022-04-16', y=230, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_1.update_yaxes(range=[50,250])
fig_1.update_layout(showlegend=False, template='plotly_white')

# 7-Day Rolling Average:
df['y-r7'] = df['y'].rolling(7).mean()
for i in range(12):
    df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7) + timedelta(days=(i*7))), 'average-7'] = df['y-r7'][len(df) - 1 - 12*7 + i*7]
df['average-7-mae'] = np.absolute(df['average-7'] - df['y'])
mean = np.round(np.mean(df[df['test'] != 'train'].groupby('test')['average-7-mae'].mean()), decimals = 2)
std = np.round(np.std(df[df['test'] != 'train'].groupby('test')['average-7-mae'].mean()), decimals = 2)

df_temp = df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7))]
df_temp.reset_index(inplace=True)
fig_2 = go.Figure()
fig_2.add_trace(go.Scatter(x=list(df_temp.Date), y=df_temp['y'], mode='lines+markers', name='Target'))
for i in range(12):
    fig_2.add_trace(go.Scatter(x=list(df_temp.iloc[i*7:i*7+7].Date), y=df_temp[i*7:i*7+7]['average-7'], mode='lines+markers', line=dict(color='Red',)))
fig_2.update_layout(title="Prediction (Rolling Average, 7-Day) vs. Target", xaxis_title="Date", yaxis_title="Number of Injuries")
for i in range(12):
    x_temp = df_temp['Date'][i*7]
    fig_2.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_2.add_annotation(x=x_temp, y=75, text="cv # " + str(i+1), showarrow=True, arrowhead=3)
fig_2.add_annotation(text=f'mean cv Scores: {mean} <br> std cv Scores: {std}', 
                   x='2022-04-16', y=230, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6,
                   bgcolor="white", opacity=1)
fig_2.update_yaxes(range=[50,250])
fig_2.update_layout(showlegend=False, template='plotly_white')

# 21-Day Rolling Average:
df['y-r21'] = df['y'].rolling(21).mean()
for i in range(12):
    df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7) + timedelta(days=(i*7))), 'average-21'] = df['y-r21'][len(df) - 1 - 12*7 + i*7]
df['average-21-mae'] = np.absolute(df['average-21'] - df['y'])

mean = np.round(np.mean(df[df['test'] != 'train'].groupby('test')['average-21-mae'].mean()), decimals = 2)
std = np.round(np.std(df[df['test'] != 'train'].groupby('test')['average-21-mae'].mean()), decimals = 2)

df_temp = df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7))]
df_temp.reset_index(inplace=True)
fig_3 = go.Figure()
fig_3.add_trace(go.Scatter(x=list(df_temp.Date), y=df_temp['y'], mode='lines+markers', name='Target'))
for i in range(12):
    fig_3.add_trace(go.Scatter(x=list(df_temp.iloc[i*7:i*7+7].Date), y=df_temp[i*7:i*7+7]['average-21'], mode='lines+markers', line=dict(color='Red',)))
fig_3.update_layout(title="Prediction (Rolling Average, 21-Day) vs. Target", xaxis_title="Date", yaxis_title="Number of Injuries")
for i in range(12):
    x_temp = df_temp['Date'][i*7]
    fig_3.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_3.add_annotation(x=x_temp, y=75, text="cv # " + str(i+1), showarrow=True, arrowhead=3)
fig_3.add_annotation(text=f'mean cv Scores: {mean} <br> std cv Scores: {std}', 
                   x='2022-04-16', y=230, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6,
                   bgcolor="white", opacity=1)
fig_3.update_yaxes(range=[50,250])
fig_3.update_layout(showlegend=False, template='plotly_white')

# Seasonal Naive:
df['y-lag-7'] = df['y'].shift(7)
df['y-lag-7-mae'] = np.absolute(df['y-lag-7'] - df['y'])
mean = np.round(np.mean(df[df['test'] != 'train'].groupby('test')['y-lag-7-mae'].mean()), decimals = 2)
std = np.round(np.std(df[df['test'] != 'train'].groupby('test')['y-lag-7-mae'].mean()), decimals = 2)
df_temp = df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7))]
df_temp.reset_index(inplace=True)
fig_4= go.Figure()
fig_4.add_trace(go.Scatter(x=list(df_temp.Date), y=df_temp['y'], mode='lines+markers', name='Target'))
for i in range(12):
    fig_4.add_trace(go.Scatter(x=list(df_temp.iloc[i*7:i*7+7].Date), y=df_temp[i*7:i*7+7]['y-lag-7'], mode='lines+markers', line=dict(color='Red',)))
fig_4.update_layout(title="Prediction (Seasonal Naïve, 7-Day) vs. Target", xaxis_title="Date", yaxis_title="Number of Injuries")
for i in range(12):
    x_temp = df_temp['Date'][i*7]
    fig_4.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_4.add_annotation(x=x_temp, y=75, text="cv # " + str(i+1), showarrow=True, arrowhead=3)
fig_4.add_annotation(text=f'mean cv Scores: {mean} <br> std cv Scores: {std}', 
                   x='2022-04-16', y=230, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_4.update_yaxes(range=[50,250])
fig_4.update_layout(showlegend=False, template='plotly_white')

# Seasonal Naive - average of past four lags:
df['y-lag-7+14+21+28'] = (df['y'].shift(7) + df['y'].shift(14) + df['y'].shift(21) + df['y'].shift(28))/4
df['y-lag-7+14+21+28-mae'] = np.absolute(df['y-lag-7+14+21+28'] - df['y'])
mean = np.round(np.mean(df[df['test'] != 'train'].groupby('test')['y-lag-7+14+21+28-mae'].mean()), decimals = 2)
std = np.round(np.std(df[df['test'] != 'train'].groupby('test')['y-lag-7+14+21+28-mae'].mean()), decimals = 2)
df_temp = df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7))]
df_temp.reset_index(inplace=True)
fig_5 = go.Figure()
fig_5.add_trace(go.Scatter(x=list(df_temp.Date), y=df_temp['y'], mode='lines+markers', name='Target'))
for i in range(12):
    fig_5.add_trace(go.Scatter(x=list(df_temp.iloc[i*7:i*7+7].Date), y=df_temp[i*7:i*7+7]['y-lag-7+14+21+28'], mode='lines+markers', line=dict(color='Red',)))
fig_5.update_layout(title="Prediction (Seasonal Naïve, 28-Day) vs. Target", xaxis_title="Date", yaxis_title="Number of Injuries")
for i in range(12):
    x_temp = df_temp['Date'][i*7]
    fig_5.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_5.add_annotation(x=x_temp, y=75, text="cv # " + str(i+1), showarrow=True, arrowhead=3)
fig_5.add_annotation(text=f'mean cv Scores: {mean} <br> std cv Scores: {std}', 
                   x='2022-04-16', y=230, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_5.update_yaxes(range=[50,250])
fig_5.update_layout(showlegend=False, template='plotly_white')

# Exponential Smoothing:
df['triple-ex']=0
for i in range(12):
    test_size = (84) - i*7
    df_train = df.iloc[:len(df) - test_size].copy()
    df_test = df.iloc[len(df) - test_size:].copy()
    model = ExponentialSmoothing(df_train['y'], trend='add', seasonal='add', seasonal_periods=7)
    results = model.fit()
    predictions = results.forecast(steps=test_size)
    df.loc[len(df) - test_size:, 'triple-ex'] = predictions

df['triple-ex-mae'] = np.absolute(df['triple-ex'] - df['y'])
mean = np.round(np.mean(df[df['test'] != 'train'].groupby('test')['triple-ex-mae'].mean()), decimals = 2)
std = np.round(np.std(df[df['test'] != 'train'].groupby('test')['triple-ex-mae'].mean()), decimals = 2)

df_temp = df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=12*7))]
df_temp.reset_index(inplace=True)
fig_6 = go.Figure()
fig_6.add_trace(go.Scatter(x=list(df_temp.Date), y=df_temp['y'], mode='lines+markers', name='Target'))
for i in range(12):
    fig_6.add_trace(go.Scatter(x=list(df_temp.iloc[i*7:i*7+7].Date), y=df_temp[i*7:i*7+7]['triple-ex'], mode='lines+markers', line=dict(color='Red',)))
fig_6.update_layout(title="Prediction (Exponential Smoothing) vs. Target", xaxis_title="Date", yaxis_title="Number of Injuries")
for i in range(12):
    x_temp = df_temp['Date'][i*7]
    fig_6.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_6.add_annotation(x=x_temp, y=75, text="cv # " + str(i+1), showarrow=True, arrowhead=3)
fig_6.add_annotation(text=f'mean cv Scores: {mean} <br> std cv Scores: {std}', 
                   x='2022-04-16', y=230, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_6.update_yaxes(range=[50,250])
fig_6.update_layout(showlegend=False, template='plotly_white')

# Residuals Analysis:
df['test_'] = 'train'
for i in range(104):
    df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=104*7) + timedelta(days=(i*7))), 'test_'] = ('test ' + str(i+1))
for i in range(104):
    df.loc[df['Date'] > (df['Date'][len(df)-1] - timedelta(days=104*7) + timedelta(days=(i*7))), 'average-21'] = df['y-r21'][len(df) - 1 - 104*7 + i*7]
df['best-residual'] = df['average-21'] - df['y']
fig_7 = ff.create_distplot([df[df['test_'] != 'train']['best-residual']], ['Residuals'], bin_size=1, curve_type='kde')
fig_7.update_layout(title_text='Histogram Plot of Residuals with a Best-Fit Normal Distribution', showlegend=False, template='plotly_white')

fig_8 = go.Figure()
qqplot_data = qqplot(df[df['test_'] != 'train']['best-residual'], line='s').gca().lines
fig_8.add_trace({'type': 'scatter','x': qqplot_data[0].get_xdata(),'y': qqplot_data[0].get_ydata(), 'mode': 'markers','marker': {'color': '#19d3f3'}})
fig_8.add_trace({'type': 'scatter','x': qqplot_data[1].get_xdata(),'y': qqplot_data[1].get_ydata(), 'mode': 'lines','line': {'color': '#636efa'}})
fig_8.update_layout({'title': 'Quantile-Quantile Plot','xaxis': {'title': 'Theoritical Quantities','zeroline': False},'yaxis': {'title': 'Residuals'}})
fig_8.update_layout(showlegend=False, template='plotly_white')

def create_auto_corr_plot(series):
    corr_array = acf(series.dropna(), alpha=0.05)
    lower_y = corr_array[1][:,0] - corr_array[0]
    upper_y = corr_array[1][:,1] - corr_array[0]
    fig = go.Figure()
    [fig.add_scatter(x=(x,x), y=(0,corr_array[0][x]), mode='lines',line_color='#3f3f3f') 
     for x in range(len(corr_array[0]))]
    fig.add_scatter(x=np.arange(len(corr_array[0])), y=corr_array[0], mode='markers', marker_color='#1f77b4', marker_size=8)
    fig.add_scatter(x=np.arange(len(corr_array[0])), y=upper_y, mode='lines', line_color='rgba(255,255,255,0)')
    fig.add_scatter(x=np.arange(len(corr_array[0])), y=lower_y, mode='lines',fillcolor='rgba(32, 146, 230,0.3)',
        fill='tonexty', line_color='rgba(255,255,255,0)')
    fig.update_traces(showlegend=False)
    fig.update_xaxes(range=[-1,30])
    fig.update_yaxes(zerolinecolor='#000000')  
    title='Autocorrelation (ACF)' + ' for ' + series.name
    fig.update_layout(title=title)
    return fig

fig_9 = create_auto_corr_plot(df[df['test_'] != 'train']['best-residual'])
fig_9.update_layout(showlegend=False, template='plotly_white')

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("Baseline Predictive Models"),
                        html.P(text_bm_1),
                        html.P(text_bm_3),
                    ]), style={'padding': padd_},
            ),
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Tabs(value='1',
                        children =
                                [
                                    dcc.Tab(value='1', children = dbc.Card(dbc.CardBody([html.P(text_bm_2, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_1, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="Naïve"),
                                    dcc.Tab(value='2', children = dbc.Card(dbc.CardBody([html.P(text_bm_4, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_2, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="7-Day Rolling Average"),
                                    dcc.Tab(value='3', children = dbc.Card(dbc.CardBody([html.P(text_bm_5, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_3, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="21-Day Rolling Average"),   
                                    dcc.Tab(value='4', children = dbc.Card(dbc.CardBody([html.P(text_bm_6, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_4, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="Naïve-seasonal"),
                                    dcc.Tab(value='5', children = dbc.Card(dbc.CardBody([html.P(text_bm_7, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_5, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="Naïve-seasonal-28-Days"),
                                    dcc.Tab(value='6', children = dbc.Card(dbc.CardBody([html.P(text_bm_8, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_6, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="Exponential Smoothing"),
                                ]
                    ),
                    style={'textAlign': 'center', "widht": '100%', 'padding': padd_}),
            ]
        ),  
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.P(text_bm_9),
                    ]), style={'padding': padd_},

            ),
        ),    
        dbc.Row(
            [
                dbc.Col(
                        dcc.Tabs(value='1',
                        children =
                                [
                                    dcc.Tab(value='1', children = dbc.Card(dbc.CardBody([html.P(text_bm_10, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_7, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="Distribution of Residuals"),
                                    dcc.Tab(value='2', children = dbc.Card(dbc.CardBody([html.P(text_bm_11, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_8, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="Quantile-Quantile Plot"),
                                    dcc.Tab(value='3', children = dbc.Card(dbc.CardBody([html.P(text_bm_12, style={'textAlign': 'left'}),
                                        dcc.Graph(figure=fig_9, style={'height': '60vh'})]), 
                                            className="mt-4", color="info", outline=True), label="Autocorrelation Plot"),
                                ]
                        ),
                    style={'textAlign': 'center', "widht": '100%', 'padding': padd_}),
            ], 
        ),  
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardHeader("Insights:", style={'textAlign': 'center', 'fontWeight': 'bold'}),
                        dbc.CardBody(
                            [html.Div(b_bm_1, className="card-text")], style={'textAlign': 'center'}),
                    ],
                    color="info", inverse=True
                ), width={"size": 8, "offset": 2}, style={'padding': padd_},
                ),
            ]
        ),                                 
    ]
)