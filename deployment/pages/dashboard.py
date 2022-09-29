from dash import dcc, html, Input, Output, callback, dash_table
import dash
import dash_bootstrap_components as dbc
from df import df
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from assets.texts import *
import os

df_p = pd.read_csv(os.path.join('Data/art.csv'), usecols=['ts', 'y', 'linreg', 'linreg_mean_train', 'linreg_mean_test', 'linreg_std_train', 'linreg_std_test', 
    'logreg', 'logreg_mean_train', 'logreg_mean_test', 'logreg_std_train', 'logreg_std_test',
    'xgb', 'xgb_mean_train', 'xgb_mean_test', 'xgb_std_train', 'xgb_std_test'])

# XGBoost:
l = df_p.shape[0]
fig_dash_7 = go.Figure()
fig_dash_7.add_trace(go.Scatter(x=list(df_p.ts), y=df_p['y'], mode='lines+markers'))
for i in range(1,13,1):
    fig_dash_7.add_trace(go.Scatter(x=list(df_p.iloc[l-(i+1)*7 : l-(i+1)*7+7].ts), y=df_p[l-(i+1)*7 : l-(i+1)*7+7]['xgb'], mode='lines+markers', 
        line=dict(color='Red',), name='CV'))
fig_dash_7.update_layout(title="XGBoost", 
    xaxis_title="Date", yaxis_title="Number of Injuries")
for j in range(1,13,1):
    x_temp = df_p['ts'].iloc[l-(j+1)*7]
    fig_dash_7.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Orange',), xref='x', yref='y', opacity=0.5)
    fig_dash_7.add_annotation(x=x_temp, y=75, text="CV # " + str(13-j), showarrow=True, arrowhead=3)
fig_dash_7.add_trace(go.Scatter(x=list(df_p.iloc[l-7 : l-1].ts), y=df_p[l-7 : l-1]['xgb'], mode='lines+markers', line=dict(color='Green',), name='Prediction'))
x_temp = df_p['ts'].iloc[l-7]
fig_dash_7.add_shape(type='line', x0=x_temp, y0=0, x1=x_temp, y1=350, line=dict(color='Green',), xref='x', yref='y', opacity=0.5)
fig_dash_7.add_annotation(x=x_temp, y=75, text="Prediction", showarrow=True, arrowhead=3)
x_temp = df_p['ts'].iloc[l-10*7]
fig_dash_7.add_annotation(text=f'''Scoring Method: Mean Absolute Error
<br>12-Fold Cross Validation Results:
<br>Mean Train Scores: {df_p.xgb_mean_train.iloc[0]}, Standard Deviation of Train Scores: {df_p.xgb_std_train.iloc[0]}
<br>Mean CV Scores: {df_p.xgb_mean_test.iloc[0]}, Standard Deviation of CV Scores: {df_p.xgb_std_test.iloc[0]}''', 
    x=x_temp, y=280, showarrow=False, bordercolor="black", borderwidth=2, borderpad=6, bgcolor="white", opacity=1)
fig_dash_7.update_yaxes(range=[0,300])
fig_dash_7.update_layout(showlegend=False, template='plotly_white')

ml_result_data = {
    'Naïve': [np.nan, np.nan, 23.9, 14.0], '7-Day Rolling Average': [np.nan, np.nan, 18.8, 7.4], '21-Day Rolling Average': [np.nan, np.nan, 17.2, 6.3],
    'Naïve-seasonal': [np.nan, np.nan, 23.5, 6.6], 'Naïve-seasonal-28-Days': [np.nan, np.nan, 20.0, 5.8], 'Exponential Smoothing': [np.nan, np.nan, 18.1, 6.5],
    'Linear Regression': [18.1, 0.1, 17.8, 8.8], 'Logistic Regression': [25.3, 1.0, 18.4, 8.1], 'XGBoost': [17.2, 0.1, 15.8, 8.5],
    "Meta's Prophet": [13.8, 0.1, 26.3, 12.1], "LinkedIn's Silverkite": [16.8, 0.1, 18.0, 7.2],
    }
ml_results = pd.DataFrame.from_dict(ml_result_data, orient='index', columns=['Mean Train', 'SD Train', 'Mean Test', 'SD Test'])
ml_results.reset_index(inplace=True)
ml_results.columns = ['Algorithm', 'Mean Train', 'SD Train', 'Mean Test', 'SD Test']
table_results = dbc.Card(dbc.CardBody(dash_table.DataTable(ml_results.to_dict('records'), [{"name": i, "id": i} for i in ml_results.columns],
                    style_table={'overflowX': 'auto'}, style_cell={'text-align': 'center', 'marginLeft': 'auto', 'marginRight': 'auto', 'fontSize': 12},
                    style_header={'backgroundColor': '#3C5C84', 'fontWeight': 'bold', 'color': 'white'},
                    style_data_conditional=[{'if': {'filter_query': '{Algorithm} = "XGBoost"'}, 'backgroundColor': '#8196AF', 'color': 'black', 'fontWeight': 'bold'}
    ])),
                    className="mt-1", color="info", outline=True)

mask = (df['LATITUDE'] > 40.48) & (df['LATITUDE'] < 40.95) & (df['LONGITUDE']< -73.65) & (df['LONGITUDE'] > -74.3)
df = df.loc[mask]

dash.register_page(__name__, path="/", name='Dashboard', order=0)

date_range= dcc.RadioItems(id='year', options=[{'label': '2019', 'value': '2019.html'}, {'label': '2020', 'value': '2020.html'},
                                                {'label': '2021', 'value': '2021.html'}, {'label': '2022', 'value': '2022.html'}],
                             value='2019.html', inline=True, inputStyle={"margin-right": "5px", "margin-left": "10px"})              

card_1 = html.Div([
    dbc.Card(
        dbc.CardBody(
            html.Div([
                dbc.Label('Filter Accidents by Year:', style={"font-weight": "bold"}),
                html.Div(date_range,
                    style={'margin-bottom': "10px"}
                ),
                dbc.Label('Filter Accidents by Severity:', style={"font-weight": "bold"}),
                dcc.RadioItems(id='sev', options=['All Accidents', 'Injuries', 'Fatalities'], value='All Accidents',
                               inline=True, inputStyle={"margin-right": "5px", "margin-left": "10px"}, className='mb-2'),
                dbc.Label('Filter Accidents by Mode:', style={"font-weight": "bold"}),
                dcc.RadioItems(id='typ', options=['All Accidents', 'Pedestrians', 'Cyclists'], value='All Accidents',
                               inline=True, inputStyle={"margin-right": "5px", "margin-left": "10px"}, className='mb-2'),
                dbc.Label('Filter Accidents by Borough:', style={"font-weight": "bold"}),
                html.Div(
                    dbc.Row(
                        [
                            dbc.Col(dcc.Dropdown(['All', 'Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island'], 'All', id='borough', clearable=False), 
                            width = {"size": 4, "offset": 4}),
                        ],
                    ),
                ),
            ], style={'textAlign': 'center'})
        ), class_name='card border-info mb-3'
    )
]
),

card_2 = dbc.Col(html.Div(
    dbc.Card(dbc.CardBody([dcc.Graph(id='fig_dash_1', style={'height': '45vh', 'width': '100%'})],
                          ), className="mt-1", color="info", outline=True)))

card_3 = html.Div(
    dbc.Card(dbc.CardBody([dcc.Graph(id='fig_dash_2', style={'height': '63.3vh', 'width': '100%'})],
                          ), color="info", outline=True))

card_4 = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4(id='acc', className="card-title")),
                    dbc.CardBody(html.H4('Accidents', className="card-title"))
                ], class_name='card border-info mb-3'
            ), width={"size": 3, "offset": 1}
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4(id='inj', className="card-title")),
                    dbc.CardBody(html.H4('Injuries', className="card-title"))
                ], class_name='card border-info mb-3'
            ), width={"size": 2, "offset": 1}            
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4(id='ftl', className="card-title")),
                    dbc.CardBody(html.H4('Fatalities', className="card-title"))
                ], class_name='card border-info mb-3'
            ), width={"size": 3, "offset": 1}            
        ),
    ]
)

card_5 = html.Div(
    dbc.Card(dbc.CardBody([dcc.Graph(id='fig_dash_3', style={'height': '45vh', 'width': '100%'})],
                          ), color="info", outline=True))

card_6 = dbc.Col(html.Div(
    dbc.Card(dbc.CardBody([dcc.Graph(id='fig_dash_4', style={'height': '45vh', 'width': '100%'})],
                          ), className="mt-1", color="info", outline=True)))

card_7 = dbc.Col(html.Div(
    dbc.Card(dbc.CardBody([dcc.Graph(id='fig_dash_5', style={'height': '45vh', 'width': '100%'})],
                          ), className="mt-1", color="info", outline=True)))

card_9 = dbc.Col(html.Div(
    dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_dash_7, style={'height': '65vh', 'width': '100%'})],
                          ), className="mt-1", color="info", outline=True)))

card_10 = dbc.Col(html.Div(
    dbc.Card(dbc.CardBody([
        html.H3('NYC Motor Vehicle Collisions Dashboard', style={'textAlign': 'center'}),
        html.P(text_dash_1, style={'textAlign': 'center'}),
        html.P(text_dash_2, style={'textAlign': 'center'})
    ],
    ), className="mb-3", color="info", outline=True)),
        width={"size": 8, "offset": 2},
    )

layout = html.Div(
    [
        dbc.Row(
                card_10
        ),        
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(card_1),
                        dbc.Row(card_5)
                    ],
                    width=4
                ),
                dbc.Col(
                    [
                        dbc.Row(card_4),
                        dbc.Row(card_3)
                    ],
                    width=8
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(card_2, width = 4),
                dbc.Col(card_6, width = 4),
                dbc.Col(card_7, width = 4),
            ], class_name='mt-3'
        ),
        dbc.Row(
            [
                dbc.Col(
                html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Iframe(id="geo_fig_output", src="assets/plots/fig_dash_2019.html", style={'height': '65vh', 'width': '100%'})
                            ]
                        ), color="info", outline=True))
                , width = 12),
            ], class_name='mt-3'
        ),        
        dbc.Row(
            [
                dbc.Col(card_9, width = 8),
                dbc.Col(table_results, width = 4),
            ], class_name='mt-3', align="center",
        ),           
    ]
)

@callback(
    Output('geo_fig_output', 'src'),
    Input('year', 'value'), prevent_initial_call=True)
def update_table(year):
    return f"assets/plots/fig_dash_{year}"

@callback(
    Output('fig_dash_1', 'figure'),
    Output('fig_dash_2', 'figure'),
    Output('fig_dash_3', 'figure'),
    Output('fig_dash_4', 'figure'),
    Output('fig_dash_5', 'figure'),
    Output('acc', 'children'),
    Output('inj', 'children'),
    Output('ftl', 'children'),
    Input('sev', 'value'),
    Input('typ', 'value'),
    Input('year', 'value'),
    Input('borough', 'value'))
def update_table(sev, typ, year, borough):
    year = year.split('.')[0]
    df_temp = df[(df['CRASH DATE'] >= year+'-01-01') & (df['CRASH DATE'] <= year+'-12-31')]

    if sev == 'Injuries':
        df_temp = df_temp[df_temp['NUMBER OF PERSONS INJURED']>0]
    elif sev == 'Fatalities':
        df_temp = df_temp[df_temp['NUMBER OF PERSONS KILLED']>0]
    if typ == 'Pedestrians':
        df_temp = df_temp[(df_temp['NUMBER OF PEDESTRIANS INJURED']>0) | (df_temp['NUMBER OF PEDESTRIANS KILLED']>0)]
    elif typ == 'Cyclists':
        df_temp = df_temp[(df_temp['NUMBER OF CYCLIST INJURED']>0) | (df_temp['NUMBER OF CYCLIST KILLED']>0)]
    if borough == 'Manhattan':
        df_temp = df_temp[df_temp['BOROUGH'] == 'MANHATTAN']
    elif borough == 'Brooklyn':
        df_temp = df_temp[df_temp['BOROUGH'] == 'BROOKLYN']
    elif borough == 'Queens':
        df_temp = df_temp[df_temp['BOROUGH'] == 'QUEENS']
    elif borough == 'Bronx':
        df_temp = df_temp[df_temp['BOROUGH'] == 'BRONX']
    elif borough == 'Staten Island':
        df_temp = df_temp[df_temp['BOROUGH'] == 'STATEN ISLAND']

    fig_dash_1 = px.histogram(df_temp, x='Hour', template='plotly_white', nbins=24, color_discrete_sequence=['#D98880'],
        title='Number of Accidents by Hour')
    fig_dash_1.update_layout(margin={"r": 0, "l": 0, "b": 0}, bargap=0.3)
    
    df_temp['d_#'] = df_temp['CRASH DATE'].dt.dayofweek
    df_temp.sort_values('d_#', inplace=True, ascending=True)

    fig_dash_4 = px.histogram(df_temp, x='Day', template='plotly_white', nbins=7, color_discrete_sequence=['#D98880'],
        title='Number of Accidents by Day')
    fig_dash_4.update_layout(margin={"r": 0, "l": 0, "b": 0}, bargap=0.3)

    df_temp['m_#'] = df_temp['CRASH DATE'].dt.month
    df_temp.sort_values('m_#', inplace=True, ascending=True)
    fig_dash_5 = px.histogram(df_temp, x='Month', template='plotly_white', nbins=12, color_discrete_sequence=['#D98880'],
        title='Number of Accidents by Month')
    fig_dash_5.update_layout(margin={"r": 0, "l": 0, "b": 0}, bargap=0.3)    

    fig_dash_2 = px.scatter_mapbox(lat=df_temp["LATITUDE"], lon=df_temp["LONGITUDE"], color=df_temp['BOROUGH'], 
        color_discrete_map={'BROOKLYN':'rgb(47,21,23)', 'QUEENS':'rgb(100,41,39)', 'MANHATTAN':'rgb(146,71,37)', 'BRONX':'rgb(178,115,45)', 'STATEN ISLAND':'rgb(214,193,76)'},
        )
    fig_dash_2.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="left", x=0))
    fig_dash_2.update_layout(mapbox={"style": "carto-positron",
                    "zoom": 9, "center": {"lon": -73.95, "lat": 40.7}})
    fig_dash_2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    temp_2 = pd.DataFrame(df_temp['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()).iloc[:10].reset_index()
    fig_dash_3 = px.pie(temp_2,values='CONTRIBUTING FACTOR VEHICLE 1', names='index', color_discrete_sequence=px.colors.sequential.solar, 
        title='Contributing Factor of the Accident')
    fig_dash_3.update_layout(margin={"r": 0, "l": 0, "b": 0})
    
    acc = '{0:,}'.format(int(df_temp['Count'].sum()))
    inj = '{0:,}'.format(int(df_temp['NUMBER OF PERSONS INJURED'].sum()))
    ftl = '{0:,}'.format(int(df_temp['NUMBER OF PERSONS KILLED'].sum()))

    return fig_dash_1, fig_dash_2, fig_dash_3, fig_dash_4, fig_dash_5, acc, inj, ftl    