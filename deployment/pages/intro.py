from dash import dcc, html
import dash
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.graph_objects as go
from assets.texts import *
from df import df

dash.register_page(__name__, path="/intro", name='Problem Statement', order=1)
padd_ = 20

df = df[['CRASH DATE', 'NUMBER OF PERSONS INJURED', 'Count']]

df = df.resample(rule='D', on='CRASH DATE').sum()
df = df[['Count', 'NUMBER OF PERSONS INJURED']].reset_index()
df.columns = ['Date', 'Accidents', 'Injuries']

df['MA30_A'] = df['Accidents'].rolling(window=30).mean()
df['MA7_A'] = df['Accidents'].rolling(window=7).mean()
df['MA30_I'] = df['Injuries'].rolling(window=30).mean()
df['MA7_I'] = df['Injuries'].rolling(window=7).mean()

fig_1 = go.Figure()
fig_1.add_trace(go.Scatter(x=df.Date, y=df.Accidents,
                         legendgroup="Accidents", legendgrouptitle_text="Daily Accidents Count", name="Daily Accidents Count",
                         mode="markers", marker=dict(color="Black", size=3)))
fig_1.add_trace(go.Scatter(x=df.Date, y=df.MA7_A,
                         legendgroup="Accidents", name="7-Day Moving Average", mode="lines",
                         line=dict(color="Crimson", width=2)))
fig_1.add_trace(go.Scatter(x=df.Date, y=df.MA30_A,
                         legendgroup="Accidents", name="30-Day Moving Average", mode="lines",
                         line=dict(color="Blue", width=2)))
fig_1.add_trace(go.Scatter(x=df.Date, y=df.Injuries,
                         legendgroup="Injuries", legendgrouptitle_text="Daily Injuries Count", name="Daily Injuries Count",
                         mode="markers", marker=dict(color="#BA4A00", size=3)))
fig_1.add_trace(go.Scatter(x=df.Date, y=df.MA7_I,
                         legendgroup="Injuries", name="7-Day Moving Average", mode="lines",
                         line=dict(color="Crimson", width=2)))
fig_1.add_trace(go.Scatter(x=df.Date, y=df.MA30_I,
                         legendgroup="Injuries", name="30-Day Moving Average", mode="lines",
                         line=dict(color="Blue", width=2)))
fig_1.update_layout(template="plotly_white",
                  title="Number of Daily Accidents and Injuries")
fig_1.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
fig_1.update_layout(
    yaxis_range=[0, 1200], xaxis_title="Date", yaxis_title="Count", height=700)

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("Problem Statement"),
                        html.P(text_intro_1),
                        html.P(text_intro_2),
                        dbc.Col(html.Div(
                            dbc.Card(dbc.CardBody([html.Img(src='assets/project_flow.jpg', style={'height': '100%', 'width': '100%'})],
                                        ), className="mt-4", color="white", outline=False)
                                            ), width={"size": 6, "offset": 3}),
                        html.P(text_intro_3, className="mt-4"),
                        html.Div(b_intro_1),
                    ]
                ), style={'padding': padd_}
            )
        ), 
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        dbc.Col(html.Div(
                            dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_1, style={'height': '100%', 'width': '100%'})],
                                        ), color="info", outline=True)
                                            ), width={"size": 12, "offset": 0}),
                    ]
                ), style={'padding': padd_}
            )
        ),         
    ]
)
