from dash import dcc, html, Input, Output, callback, register_page, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np
import dash_gif_component as gif

from assets.texts import *
from df import df, df_streets

register_page(__name__, path='/esda', name='Exploratory Spatial Data Analysis', order=3)
padd_ = 20

mar_l_r = "2%"
mar_l_r_2 = "0.25%"

df = df[['CRASH DATE', 'LATITUDE', 'LONGITUDE', 'NUMBER OF PERSONS INJURED', 'Hour', 'Count', 'PHYSICALID']]

df.sort_values('Hour', inplace=True)
mask = (df['LATITUDE'] > 40.48) & (df['LATITUDE'] < 40.95) & (df['LONGITUDE']
                                                              < -73.65) & (df['LONGITUDE'] > -74.3) & (df['CRASH DATE'] > '2020-07-01')
df = df.loc[mask]

fig_1 = go.Figure(go.Scattermapbox(lat=df["LATITUDE"], lon=df["LONGITUDE"], mode='markers',
                                   marker=go.scattermapbox.Marker(size=4, color='red', opacity=0.01)))
fig_1.update_layout(mapbox={"style": "carto-positron",
                    "zoom": 9, "center": {"lon": -73.95, "lat": 40.7}})
fig_1.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

tab_map_1 = dbc.Card(dbc.CardBody([html.Iframe(src="assets/plots/fig_esda_3.html", style={
    'height': '65vh', 'width': '100%'})]), className="mt-4", color="info", outline=True)
tab_map_2 = dbc.Card(dbc.CardBody([html.Div(
    html.Iframe(src="assets/plots/fig_esda_4.html", style={
    'height': '65vh', 'width': '100%'})
)
    ]), className="mt-4", color="info", outline=True)
tabs_map = dcc.Tabs(value='1',
                        children =
                        [
                            dcc.Tab(value='1', children = tab_map_1, label="Number of Accident Per Road Segment"),
                            dcc.Tab(value='2', children = tab_map_2, label="Average Number of Accident Per 100 ft.")
                        ]
                    )

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("Exploratory Spatial Data Analysis"),
                        html.P(text_esda_1),
                    ]), style={'padding': padd_},
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        dbc.Col(html.Div(
                            dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_1, style={'height': '100%', 'width': '100%'})],
                                                  ), color="info", outline=True)
                        ), width={"size": 8, "offset": 2}),
                    ]
                ), style={'padding': padd_},
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.P(text_esda_2),
                        html.P(text_esda_3),
                        html.P(text_esda_4),
                    ]), style={'padding': padd_},
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        dbc.Col(html.Div(
                            dbc.Card(dbc.CardBody([html.Iframe(src="assets/plots/fig_2.html", style={'height': '60vh', 'width': '100%'})],
                                                  ), color="info", outline=True)
                        ), width={"size": 8, "offset": 2}),
                    ]
                )
            ), style={'padding': padd_},
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardHeader("Insights:", style={'textAlign': 'center', 'fontWeight': 'bold'}),
                        dbc.CardBody(
                            [html.Div(b_esda_1, className="card-text")], style={'textAlign': 'center'}),
                    ],
                    color="info", inverse=True
                ), width={"size": 8, "offset": 2}, style={'padding': padd_},
                ),
            ]
        ),
        dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            children=[
                                html.H4("Spatial Autocorrelation using Moran's I"),
                                html.P(text_esda_12),
                                html.P(text_esda_13),
                            ]), style={'padding': padd_},
                    ),
                    dbc.Col(
                        html.Div(
                            style={"margin-left": mar_l_r,
                                "margin-top": mar_l_r, "margin-right": mar_l_r},
                            children=[
                                html.H6("A Visualization of Spatial Autocorrelation, borrowed from Radil, 2011", style={'textAlign': 'center'}),
                                html.Img(src=r'assets/img/moran_ex.png', style={'height': '100%', 'width': '100%'}),
                            ]), style={'padding': padd_},
                    ),                    
                ], align="center",
        ), 
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.P(text_esda_14),
                    ]
                ), style={'padding': padd_},
            )
        ),          
        dbc.Row(
            [
                dbc.Col(html.Div(
                            dbc.Card(dbc.CardBody([html.Img(src=r'assets/img/Moran_Scatter.jpg', style={'height': '100%', 'width': '100%'})],
                                                  ), color="info", outline=True), style={'width':'28vw'}
                        ), style={'padding': padd_},
                    ),
                dbc.Col(html.Div(
                            dbc.Card(dbc.CardBody([html.Iframe(src="assets/plots/fig_5.html", style={'height': '45vh', 'width': '100%'})],
                                                  ), color="info", outline=True), style={'width':'65vw'}
                        ), style={'padding': padd_},
                    )
            ], align="center", 
        ),  
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardHeader("Insights:", style={'textAlign': 'center', 'fontWeight': 'bold'}),
                        dbc.CardBody(
                            [html.Div(b_esda_6, className="card-text")], style={'textAlign': 'center'}),
                    ],
                    color="info", inverse=True
                ), width={"size": 8, "offset": 2}, style={'padding': padd_},
                ),
            ]
        ),              
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("NYC Street Centerline (CSCL) Database"),
                        html.P(text_esda_5),
                        dash_table.DataTable(id='street_df_page', columns=[{"name": i, "id": i} for i in df_streets.columns], page_current=0,
                                             page_size=5, page_action='custom', style_table={'overflowX': 'auto'}, style_cell={'text-align': 'center',
                                                                    'marginLeft': 'auto', 'marginRight': 'auto', 'fontSize': 12},
                                             style_header={
                                                 'backgroundColor': '#E5E8E8', 'fontWeight': 'bold'},
                                             ),
                        html.P(text_esda_6),
                        html.P(text_esda_7),
                    ]), style={'padding': padd_},
            )
        ),
        dbc.Row(
            [
                dbc.Col(tabs_map, style={'padding': padd_},),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardHeader("Insights:", style={'textAlign': 'center', 'fontWeight': 'bold'}),
                        dbc.CardBody(
                            [html.Div(b_esda_2, className="card-text")], style={'textAlign': 'center'}),
                    ],
                    color="info", inverse=True
                ), width={"size": 8, "offset": 2}, style={'padding': padd_},
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        children=[
                            html.H4(
                                "Using DBSCAN to Identify Accident Hot Spots"),
                            html.P(text_esda_8),
                            html.Div(b_esda_3),
                            html.P(text_esda_9),
                            html.Div(b_esda_4),
                        ]), style={'padding': padd_},
                ),
                dbc.Col(
                    html.Div(

                        children=[
                            html.H6(
                                'Visualization of how DBSCAN Algorithm works, borrowed from digitalvidya.com'),
                            gif.GifPlayer(gif='assets/dbscan.gif',
                                          still='assets/dbscan_still.png'),
                        ]), style={'padding': padd_, 'width': '100%', 'verticalAlign': 'middle', 'textAlign': 'center'}, 
                )
            ], align="center"
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.P(text_esda_10),
                        html.P(text_esda_11),
                        dbc.Label("""Epsilon, Maximum Radius of Neighbors in ft. (A one way street is ~50ft. and a two way street is ~100ft.
                        To capture a massive intersection with all its connecting roads, you need a radius of ~2000-300ft.):"""),
                        dcc.RadioItems(id='eps', options=[
                                       100, 125, 150, 175, 200, 225, 250, 275, 300], value=200, inline=True, inputStyle={"margin-left": "20px"}),
                        dbc.Label(
                            'Minimum Points, Minimum Number of Datapoints Within the Neighborhood for Clusters:'),
                        dcc.RadioItems(id='min_p', options=[
                                       50, 75, 100, 125, 150], value=100, inline=True, inputStyle={"margin-left": "20px"}),
                    ]
                ), style={'padding': padd_},
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        dbc.Col(html.Div(
                            dbc.Card(dbc.CardBody([dcc.Graph(id='fig_call_1', style={'height': '65vh', 'width': '100%'})],
                                                  ), className="mt-1", color="info", outline=True)
                            ), width={"size": 12, "offset": 0}),
                ]
                ), style={'padding': padd_},
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Tabs(value='1',
                                children =
                        [
                            dcc.Tab(value='1', children = dbc.Card(dbc.CardBody([html.Img(src=r'assets/img/intersection_1.png', style={'height': '60vh'})]), 
                                    color="info", outline=True),
                                    label="Bruckner Blvd. at Hunts Pt."),
                            dcc.Tab(value='2', children = dbc.Card(dbc.CardBody([html.Img(src=r'assets/img/intersection_2.png', style={'height': '60vh'})]), 
                                    color="info", outline=True),
                                    label="Belt Pkwy. at Erskine St."),
                            dcc.Tab(value='3', children = dbc.Card(dbc.CardBody([html.Img(src=r'assets/img/intersection_3.png', style={'height': '60vh'})]), 
                                    color="info", outline=True),
                                    label="Atlantic Ave. at Pennsylvanie Ave."),
                            dcc.Tab(value='4', children = dbc.Card(dbc.CardBody([html.Img(src=r'assets/img/intersection_4.png', style={'height': '60vh'})]), 
                                    color="info", outline=True),
                                    label="Pennsylvanie Ave. at Jamaica Ave."),
                            dcc.Tab(value='5', children = dbc.Card(dbc.CardBody([html.Img(src=r'assets/img/intersection_5.png', style={'height': '60vh'})]), 
                                    color="info", outline=True),
                                    label="Columbia St. at Atlatic Ave."),
                        ]
                    ), style={'padding': padd_, 'textAlign': 'center',}),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardHeader("Insights:", style={'textAlign': 'center', 'fontWeight': 'bold'}),
                        dbc.CardBody(
                            [html.Div(b_esda_5, className="card-text")], style={'textAlign': 'center'}),
                    ],
                    color="info", inverse=True
                ), width={"size": 8, "offset": 2}, style={'padding': padd_},
                ),
            ]
        ),        
    ]
)


@callback(
    Output('street_df_page', 'data'),
    Input('street_df_page', "page_current"),
    Input('street_df_page', "page_size"))
def update_table(page_current, page_size):
    return df_streets.iloc[page_current*page_size:(page_current + 1)*page_size].to_dict('records')


@callback(Output('fig_call_1', 'figure'),
          Input('eps', 'value'), Input('min_p', 'value'))
def update_figure(eps, min_p):

    df_points = df[['LATITUDE', 'LONGITUDE']]
    df_temp = df_points[['LATITUDE', 'LONGITUDE']].copy()
    kms_per_radian = 6371.0088
    feet_to_km = 0.0003048
    epsilon = (eps*feet_to_km) / kms_per_radian
    db = DBSCAN(eps=epsilon, min_samples=min_p, algorithm='ball_tree',
                metric='haversine', n_jobs=-1).fit(np.radians(df_temp))

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    df_temp['cluster'] = ["cluster-{}".format(x) for x in labels]
    df_temp = df_temp.round(decimals=4)
    df_temp['t'] = df_temp['LATITUDE'].astype(
        str)+df_temp['LONGITUDE'].astype(str)
    df_temp['count'] = df_temp['t'].map(df_temp['t'].value_counts())
    df_temp.drop(columns='t', inplace=True)

    df_plot = (df_temp[df_temp['cluster'] != 'cluster--1'])
    fig_call_1 = px.scatter_mapbox(df_plot, lat='LATITUDE',
                              lon='LONGITUDE', zoom=9, color='cluster')
    fig_call_1.update_traces(marker=dict(size=10))
    fig_call_1.update_layout(showlegend=False, mapbox_style='carto-darkmatter',
                        mapbox_zoom=9, margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig_call_1.add_annotation(text=f'Number of Clusters: {len(set(labels)) - (1 if -1 in labels else 0)}', xref="x domain", yref="y domain", x=0.02, y=0.98, showarrow=False,
                         bordercolor="black", borderwidth=1, borderpad=4, bgcolor="white")

    return fig_call_1
