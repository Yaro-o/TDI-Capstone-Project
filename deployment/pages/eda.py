from dash import dcc, html, Input, Output, callback, register_page, dash_table
import plotly.express as px
import numpy as np
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

import pandas as pd
import numpy as np
from assets.texts import *
from df import df, df_weather_temp

register_page(__name__, path='/eda', name='Exploratory Data Analysis', order=2)
padd_ = 20

number_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6:
                'June', 7: 'July', 8: 'Auguat', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

df = df[['CRASH DATE', 'NUMBER OF PERSONS INJURED', 'Count']]

df_h = df.resample(rule='H', on='CRASH DATE').sum()
df_h = df_h[['Count', 'NUMBER OF PERSONS INJURED']].reset_index()
df_h.columns = ['Date', 'Accidents', 'Injuries']

df_d = df.resample(rule='D', on='CRASH DATE').sum()
df_d = df_d[['Count', 'NUMBER OF PERSONS INJURED']].reset_index()
df_d.columns = ['Date', 'Accidents', 'Injuries']

df_2 = df_d.copy()
df_2 = df_2[(df_2['Date'] < '2020-01-01') | (df_2['Date'] > '2020-07-01')]
df_2['Period'] = ''
df_2.loc[df_2['Date'] < '2020-01-01', 'Period'] = 'Pre-Covid'
df_2.loc[df_2['Date'] > '2020-07-01', 'Period'] = 'Post-Covid'
df_2['Day_'] = df_2['Date'].dt.dayofweek
df_2['Day'] = df_2['Date'].dt.day_name()
df_2 = df_2.groupby(["Day", "Period", "Day_"])[
    "Accidents"].mean().reset_index()
df_2.sort_values('Day_', inplace=True)
fig_1 = px.line(df_2, x="Day", y="Accidents",
                template='plotly_white', color="Period", markers=True)
fig_1.update_layout(yaxis_range=[0, 700])
fig_1.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

df_3 = df_2.copy()
df_3['Accidents_Normalized'] = 0
df_3.Accidents_Normalized = df_3.groupby(
    'Period').Accidents.transform(lambda x: (x/x.max()))
fig_2 = px.line(df_3, x="Day", y="Accidents_Normalized",
                template='plotly_white', color="Period", markers=True)
fig_2.update_layout(yaxis_range=[0, 1.2])
fig_2.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

df_2_i = df_d.copy()
df_2_i = df_2_i[(df_2_i['Date'] < '2020-01-01') |
                (df_2_i['Date'] > '2020-07-01')]
df_2_i['Period'] = ''
df_2_i.loc[df_2_i['Date'] < '2020-01-01', 'Period'] = 'Pre-Covid'
df_2_i.loc[df_2_i['Date'] > '2020-07-01', 'Period'] = 'Post-Covid'
df_2_i['Day_'] = df_2_i['Date'].dt.dayofweek
df_2_i['Day'] = df_2_i['Date'].dt.day_name()
df_2_i = df_2_i.groupby(["Day", "Period", "Day_"])[
    "Injuries"].mean().reset_index()
df_2_i.sort_values('Day_', inplace=True)
fig_3 = px.line(df_2_i, x="Day", y="Injuries",
                template='plotly_white', color="Period", markers=True)
fig_3.update_layout(yaxis_range=[0, 200])
fig_3.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

df_3_i = df_2_i.copy()
df_3_i['Injuries_Normalized'] = 0
df_3_i.Injuries_Normalized = df_3_i.groupby(
    'Period').Injuries.transform(lambda x: (x/x.max()))

fig_4 = px.line(df_3_i, x="Day", y="Injuries_Normalized",
                template='plotly_white', color="Period", markers=True)
fig_4.update_layout(yaxis_range=[0, 1.2])
fig_4.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

# DataFrame manipulation for hourly:
df_2h = df_h.copy()
df_2h = df_2h[(df_2h['Date'] < '2020-01-01') | (df_2h['Date'] > '2020-07-01')]
df_2h['Period'] = ''
df_2h.loc[df_2h['Date'] < '2020-01-01', 'Period'] = 'Pre-Covid'
df_2h.loc[df_2h['Date'] > '2020-07-01', 'Period'] = 'Post-Covid'
df_2h['Hour'] = df_2h['Date'].dt.hour
df_2h = df_2h.groupby(["Hour", "Period"])[
    ["Accidents", "Injuries"]].mean().reset_index()
df_2h.sort_values('Hour', inplace=True)
df_2h['Accidents_Normalized'] = 0
df_2h['Injuries_Normalized'] = 0
df_2h.Accidents_Normalized = df_2h.groupby(
    'Period').Accidents.transform(lambda x: (x/x.max()))
df_2h.Injuries_Normalized = df_2h.groupby(
    'Period').Injuries.transform(lambda x: (x/x.max()))

df_3h = df_h.copy()
df_3h = df_3h[(df_3h['Date'] < '2020-01-01') | (df_3h['Date'] > '2020-07-01')]
df_3h['Period'] = ''
df_3h.loc[df_3h['Date'] < '2020-01-01', 'Period'] = 'Pre-Covid'
df_3h.loc[df_3h['Date'] > '2020-07-01', 'Period'] = 'Post-Covid'
df_3h['Hour'] = df_3h['Date'].dt.hour
df_3h['Day_'] = df_3h['Date'].dt.dayofweek
df_3h['Day'] = df_3h['Date'].dt.day_name()
df_3h = df_3h.groupby(["Hour", "Day", "Day_", "Period"])[
    ["Accidents", "Injuries"]].mean().reset_index()
df_3h.sort_values(['Hour', "Day_"], inplace=True, ascending=[True, True])

fig_16 = px.scatter(df_3h, x="Hour", y="Day", template='plotly_white', color="Accidents", facet_col='Period',
                    size="Accidents", title="Accidents Daily Seasonality by Week", size_max=10)
fig_17 = px.scatter(df_3h, x="Hour", y="Day", template='plotly_white', color="Injuries", facet_col='Period',
                    size="Injuries", title="Injuries Daily Seasonality by Week", size_max=10)


fig_11 = px.line(df_2h, x="Hour", y="Accidents",
                 template='plotly_white', color="Period", markers=True)
fig_11.update_layout(yaxis_range=[0, 50])
fig_11.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

fig_12 = px.line(df_2h, x="Hour", y="Accidents_Normalized",
                 template='plotly_white', color="Period", markers=True)
fig_12.update_layout(yaxis_range=[0, 1.2])
fig_12.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

fig_13 = px.line(df_2h, x="Hour", y="Injuries",
                 template='plotly_white', color="Period", markers=True)
fig_13.update_layout(yaxis_range=[0, 12])
fig_13.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

fig_14 = px.line(df_2h, x="Hour", y="Injuries_Normalized",
                 template='plotly_white', color="Period", markers=True)
fig_14.update_layout(yaxis_range=[0, 1.2])
fig_14.update_layout(legend=dict(
    orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

fig_15 = px.scatter(df_3h, x="Hour", y="Day", template='plotly_white', color="Accidents", facet_col='Period',
                    size="Accidents", title="Accidents Daily Seasonality by Week", size_max=12)

# DataFrame manipulation for yearly:
df_y = df.resample(rule='M', on='CRASH DATE').sum()
df_y = df_y[['Count', 'NUMBER OF PERSONS INJURED']].reset_index()
df_y.columns = ['Date', 'Accidents', 'Injuries']
df_y = df_y[df_y['Date'] < "2022-07-01"]
df_y = df_y[df_y['Date'] > "2013-12-31"]
df_y['Month_'] = df_y['Date'].dt.month
df_y['Year'] = df_y['Date'].dt.year
df_y['Month'] = df_y['Date'].dt.month_name()
df_y = df_y.groupby(["Month", "Month_", 'Year'])[
    ["Accidents", "Injuries"]].mean().reset_index()
df_y.sort_values(['Month_', 'Year'], inplace=True, ascending=[True, True])
days_in_month = pd.DataFrame(data={'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                                   'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31},
                             index=['Number of Days']).T.reset_index()
df_y = df_y.merge(days_in_month, how='left', left_on='Month', right_on='index')
df_y['Accidents_Normalized'] = df_y['Accidents']/df_y['Number of Days']
df_y['Injuries_Normalized'] = df_y['Injuries']/df_y['Number of Days']

fig_18 = px.line(df_y, x="Month", y="Accidents", template='plotly_white',
                 color="Year", markers=True, title="Accidents Yearly Seasonality")
fig_19 = px.line(df_y, x="Month", y="Injuries", template='plotly_white',
                 color="Year", markers=True, title="Injuries Yearly Seasonality")

fig_20 = px.line(df_y, x="Month", y="Accidents_Normalized", template='plotly_white',
                 color="Year", markers=True, title="Accidents Yearly Seasonality")
fig_21 = px.line(df_y, x="Month", y="Injuries_Normalized", template='plotly_white',
                 color="Year", markers=True, title="Injuries Yearly Seasonality")

# Holidays:
df_holidays = df_d.copy()
holiday = pd.read_csv('Data/Holidays.csv')
holiday['holiday'] = 1
holiday['Date'] = pd.to_datetime(holiday['Date'])
df_holidays = df_holidays.merge(holiday, on='Date', how='left')
df_holidays = df_holidays[(df_holidays['Date'] < '2020-01-01')
                          | (df_holidays['Date'] > '2020-07-01')]
df_holidays['Period'] = ''
df_holidays.loc[df_holidays['Date'] < '2020-01-01', 'Period'] = 'Pre-Covid'
df_holidays.loc[df_holidays['Date'] > '2020-07-01', 'Period'] = 'Post-Covid'
df_holidays['Accident'] = ' '
df_holidays['Injury'] = ' '
df_holidays['Day Type'] = '0'
df_holidays['Day_'] = df_holidays['Date'].dt.dayofweek
df_holidays.loc[df_holidays['Day_'] == 6, 'Day Type'] = 'Sunday'
df_holidays.loc[df_holidays['Day_'] == 5, 'Day Type'] = 'Saturday'
df_holidays.loc[df_holidays['holiday'] == 1, 'Day Type'] = 'Holiday'
df_holidays.loc[df_holidays['Day Type'] == '0', 'Day Type'] = 'Weekday'
df_holidays.sort_values('Day Type', inplace=True, ascending=False)

fig_22 = px.strip(df_holidays[df_holidays['Period'] == 'Pre-Covid'],
                  x="Day Type", y="Accidents", color='Day Type', template='plotly_white')
fig_22.update_traces(jitter=1, marker=dict(
    size=15, line=dict(width=1, color='black')))
fig_22.update_layout(showlegend=False)

fig_23 = px.strip(df_holidays[df_holidays['Period'] == 'Post-Covid'],
                  x="Day Type", y="Accidents", color='Day Type', template='plotly_white')
fig_23.update_traces(jitter=1, marker=dict(
    size=15, line=dict(width=1, color='black')))
fig_23.update_layout(showlegend=False)

fig_24 = px.strip(df_holidays[df_holidays['Period'] == 'Pre-Covid'],
                  x="Day Type", y="Injuries", color='Day Type', template='plotly_white')
fig_24.update_traces(jitter=1, marker=dict(
    size=15, line=dict(width=1, color='black')))
fig_24.update_layout(showlegend=False)

fig_25 = px.strip(df_holidays[df_holidays['Period'] == 'Post-Covid'],
                  x="Day Type", y="Injuries", color='Day Type', template='plotly_white')
fig_25.update_traces(jitter=1, marker=dict(
    size=15, line=dict(width=1, color='black')))
fig_25.update_layout(showlegend=False)

# Weather
df_weather = df_d.copy()
df_weather = df_weather[(df_weather['Date'] < '2020-01-01')
                        | (df_weather['Date'] > '2020-07-01')]
df_weather['Period'] = ''
df_weather.loc[df_weather['Date'] < '2020-01-01', 'Period'] = 'Pre-Covid'
df_weather.loc[df_weather['Date'] > '2020-07-01', 'Period'] = 'Post-Covid'

df_w_2 = df_weather_temp.copy()
df_weather_temp = df_weather_temp[['datetime', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'windspeed', 'cloudcover', 'visibility', 'solarradiation',
                                   'solarenergy', 'uvindex', 'moonphase']]
df_weather_temp['datetime'] = pd.to_datetime(df_weather_temp['datetime'])
df_weather = df_weather.merge(
    df_weather_temp, how="left", left_on='Date', right_on='datetime')
df_weather.columns = ['Date', 'Accidents', 'Injuries', 'Period', 'datetime', 'Temperature', 'Feelslike', 'Dew Point', 'Humidity', 'Precipitation',
                      'Windspeed', 'Cloudcover', 'Visibility', 'Solar Radation', 'Solar Energy', 'UV Index', 'Moonphase']

w_b_m_5 = dbc.Card(dbc.CardBody([dcc.Graph(id='fig_26', style={
                   'height': '45vh'})]), color="info", outline=True)
w_b_m_6 = dbc.Card(dbc.CardBody([dcc.Graph(id='fig_27', style={
                   'height': '45vh'})]), color="info", outline=True)
df_w_p = df_weather[df_weather['Period'] ==
                    'Pre-Covid'].drop(columns=['Date', 'Period', 'datetime'])
corr_p = df_w_p.corr().reset_index()
df_w_a = df_weather[df_weather['Period'] ==
                    'Post-Covid'].drop(columns=['Date', 'Period', 'datetime'])
corr_a = df_w_a.corr().reset_index()
x_values = ["Accidents - Pre-Covid"]*14+["Accidents - Post-Covid"] * \
    14+["Injuries - Pre-Covid"]*14+["Injuries - Post-Covid"]*14
y_values = list(corr_p['index'])*4
color_values = list(corr_p.Accidents) + list(corr_a.Accidents) + \
    list(corr_p.Injuries) + list(corr_a.Injuries)
color_values = np.round(color_values, 2)
size_values = np.absolute(color_values)
fig_28 = px.scatter(x=x_values, y=y_values, template='plotly_white',
                    color=color_values, size=size_values,
                    size_max=25, range_color=[-1, 1], color_continuous_scale=px.colors.sequential.Viridis, labels={'x': ' ', 'y': ' ', 'color': 'Correlation Factor'})
fig_28.update_yaxes(type='category')
fig_28.update_layout(margin=dict(l=5, r=5, t=5, b=5))

w_b_m_7 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_28, style={'height': '60%', 'width': '100%', 'textAlign': 'center'})],
                                style={'textAlign': 'center'}), color="info", outline=True)

# MTA Dataset:
df_mta = df_d.copy()
df_mta = df_mta[df_mta['Date'] > "2020-07-01"]
df_mta_temp = pd.read_csv('Data/MTA_Daily_Ridership_Data__Beginning_2020.csv')
df_mta_temp = df_mta_temp[['Date', 'Subways: Total Estimated Ridership', 'Buses: Total Estimated Ridership',
                           'LIRR: Total Estimated Ridership', 'Metro-North: Total Estimated Ridership',
                           'Bridges and Tunnels: Total Traffic']]
df_mta_temp.columns = ['Date', 'Subway Passengers', 'Bus Passengers',
                       'LIRR Passenger', 'Metro North Passengers', 'Bridges and Tunnels Traffic']
df_mta_temp['Date'] = pd.to_datetime(df_mta_temp['Date'], format='%m/%d/%Y')
df_mta = df_mta.merge(df_mta_temp, how="left", on='Date')

w_b_m_8 = dbc.Card(dbc.CardBody([dcc.Graph(id='fig_29', style={
                   'height': '45vh'})]), color="info", outline=True)
w_b_m_9 = dbc.Card(dbc.CardBody([dcc.Graph(id='fig_30', style={
                   'height': '45vh'})]), color="info", outline=True)

corr_mta = df_mta.corr().reset_index()
x_values = ["Accidents"]*7+["Injuries"]*7
y_values = list(corr_mta['index'])*2
color_values = list(corr_mta.Accidents) + list(corr_mta.Injuries)
color_values = np.round(color_values, 2)
size_values = np.absolute(color_values)
fig_31 = px.scatter(x=x_values, y=y_values, template='plotly_white',
                    color=color_values, size=size_values,
                    size_max=25, range_color=[-1, 1], color_continuous_scale=px.colors.sequential.Viridis, labels={'x': ' ', 'y': ' ', 'color': 'Correlation Factor'})
fig_31.update_yaxes(type='category')
fig_31.update_layout(margin=dict(l=5, r=5, t=5, b=5))

w_b_m_10 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_31, style={'height': '60%', 'width': '100%', 'textAlign': 'center'})],
                                 style={'textAlign': 'center'}), color="info", outline=True)

# Tabs for the Weekly Seasonality:
tab_accidents_1 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_1, style={
                           'height': '45vh'})]), className="mt-4", color="info", outline=True)
tab_accidents_2 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_2, style={
                           'height': '45vh'})]), className="mt-4", color="info", outline=True)
tabs_accidents = dcc.Tabs(value='1',
                            children =
                                [
                                    dcc.Tab(value='1', children = tab_accidents_1, label="Accidents - Weekly Seasonality"),
                                    dcc.Tab(value='2', children = tab_accidents_2, label="Accidents - Weekly Seasonality - Normalized")
                                ]
                            )

tab_injuries_1 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_3, style={
                          'height': '45vh'})]), className="mt-4", color="info", outline=True)
tab_injuries_2 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_4, style={
                          'height': '45vh'})]), className="mt-4", color="info", outline=True)
tabs_injuries = dcc.Tabs(value='1',
                            children =
                            [
                                dcc.Tab(value='1', children = tab_injuries_1, label="Injuries - Weekly Seasonality"),
                                dcc.Tab(value='2', children = tab_injuries_2, label="Injuries - Weekly Seasonality - Normalized")
                            ]
                        )

# Tabs for the Daily Seasonality:
tab_accidents_daily_1 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_11, style={
                                 'height': '45vh'})]), className="mt-4", color="info", outline=True)
tab_accidents_daily_2 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_12, style={
                                 'height': '45vh'})]), className="mt-4", color="info", outline=True)
tabs_accidents_daily = dcc.Tabs(value='1',
                                    children =
                                    [
                                        dcc.Tab(value='1', children = tab_accidents_daily_1, label="Accidents - Daily Seasonality"),
                                        dcc.Tab(value='2', children = tab_accidents_daily_2, label="Accidents - Daily Seasonality - Normalized")
                                    ]
                                )

tab_injuries_daily_1 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_13, style={
                                'height': '45vh'})]), className="mt-4", color="info", outline=True)
tab_injuries_daily_2 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_14, style={
                                'height': '45vh'})]), className="mt-4", color="info", outline=True)
tabs_injuries_daily = dcc.Tabs(value='1',
                                    children =
                                    [
                                        dcc.Tab(value='1', children = tab_injuries_daily_1, label="Injuries - Daily Seasonality"),
                                        dcc.Tab(value='2', children = tab_injuries_daily_2, label="Injuries - Daily Seasonality - Normalized")
                                    ]
                                )

# Tabs for the Yearly Seasonality:
tab_accidents_yearly_1 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_18, style={
                                  'height': '45vh'})]), className="mt-4", color="info", outline=True)
tab_accidents_yearly_2 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_20, style={
                                  'height': '45vh'})]), className="mt-4", color="info", outline=True)
tabs_accidents_yearly = dcc.Tabs(value='1',
                                    children =
                                    [
                                        dcc.Tab(value='1', children = tab_accidents_yearly_1, label="Accidents - Yearly Seasonality"),
                                        dcc.Tab(value='2', children = tab_accidents_yearly_2, label="Accidents - Yearly Seasonality - Normalized")
                                    ]
                                )

tab_injuries_yearly_1 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_19, style={
                                 'height': '45vh'})]), className="mt-4", color="info", outline=True)
tab_injuries_yearly_2 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_21, style={
                                 'height': '45vh'})]), className="mt-4", color="info", outline=True)
tabs_injuries_yearly = dcc.Tabs(value='1',
                                    children =
                                    [
                                        dcc.Tab(value='1', children = tab_injuries_yearly_1, label="Injuries - Yearly Seasonality"),
                                        dcc.Tab(value='2', children = tab_injuries_yearly_2, label="Injuries - Yearly Seasonality - Normalized")
                                    ]
                                )

# Tabs for the holidays:
tab_accidents_holidays_1 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_22, style={
                                    'height': '45vh'})]), className="mt-4", color="info", outline=True)
tab_accidents_holidays_2 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_23, style={
                                    'height': '45vh'})]), className="mt-4", color="info", outline=True)
tabs_accidents_holidays = dcc.Tabs(value='1',
                                        children =
                                        [
                                            dcc.Tab(value='1', children = tab_accidents_holidays_1, label="Accidents - Pre-Covid"),
                                            dcc.Tab(value='2', children = tab_accidents_holidays_2, label="Accidents - Post-Covid")
                                        ]
                                    )

tab_injuries_holidays_1 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_24, style={
                                   'height': '45vh'})]), className="mt-4", color="info", outline=True)
tab_injuries_holidays_2 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_25, style={
                                   'height': '45vh'})]), className="mt-4", color="info", outline=True)
tabs_injuries_holidays = dcc.Tabs(value='1',
                                        children =
                                        [
                                            dcc.Tab(value='1', children = tab_injuries_holidays_1, label="Injuries - Pre-Covid"),
                                            dcc.Tab(value='2', children = tab_injuries_holidays_2, label="Injuries - Pre-Covid")
                                        ]
                                    )

# Weekly Sesonality by Month Figures:
df_4 = df_d.copy()
df_4['Month_'] = df_4['Date'].dt.month
df_4['Month'] = df_4['Date'].dt.month_name()
df_4['Day_'] = df_4['Date'].dt.dayofweek
df_4['Day'] = df_4['Date'].dt.day_name()
df_4 = df_4[(df_4['Date'] < '2020-01-01') | (df_4['Date'] > '2020-07-01')]
df_4['Period'] = ''
df_4.loc[df_4['Date'] < '2020-01-01', 'Period'] = 'Pre-Covid'
df_4.loc[df_4['Date'] > '2020-07-01', 'Period'] = 'Post-Covid'
df_4 = df_4.groupby(["Day", "Day_", "Month", "Month_", "Period"])[
    ["Accidents", "Injuries"]].mean().reset_index()
df_4.sort_values(['Day_', 'Month_'], inplace=True, ascending=[True, True])

w_b_m_1 = dbc.Card(dbc.CardBody([dcc.Graph(id='fig_5', style={
                   'height': '45vh'})]), color="info", outline=True)
w_b_m_2 = dbc.Card(dbc.CardBody([dcc.Graph(id='fig_6', style={
                   'height': '45vh'})]), color="info", outline=True)

fig_9 = px.scatter(df_4, x="Day", y="Month", template='plotly_white', color="Accidents", size="Accidents", size_max=20,
                   facet_col='Period', title="Accidents Weekly Seasonality by Month")
fig_10 = px.scatter(df_4, x="Day", y="Month", template='plotly_white', color="Injuries", size="Injuries", size_max=20,
                    facet_col='Period', title="Injuries Weekly Seasonality by Month")

w_b_m_3 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_9, style={
                   'height': '55vh'})]), color="info", outline=True)
w_b_m_4 = dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_10, style={
                   'height': '55vh'})]), color="info", outline=True)

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("Seasonality"),
                        html.P(text_1),
                    ]), style={'padding': padd_},
            )),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H6("Weekly Seasonality"),
                        html.P(text_2),
                        html.Div(b_1)
                    ]), style={'padding': padd_},
            )),
        dbc.Row(
            [
                dbc.Col(tabs_accidents, style={'padding': padd_}, width=6),
                dbc.Col(tabs_injuries, style={'padding': padd_}, width=6),
            ], className="g-0",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardHeader("Insights:", style={'textAlign': 'center', 'fontWeight': 'bold'}),
                        dbc.CardBody([html.Div(b_4, className="card-text")], style={'textAlign': 'center'}),
                    ], 
                    color="info", inverse=True
                ), width={"size": 8, "offset": 2}
                ),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H6("Weekly Seasonality by Month"),
                        html.P(text_3),
                        html.Div(b_2),
                        html.P('First Selected Month'),
                        dcc.Slider(1, 12, step=None, id='Month_1',
                                   marks=number_month, included=False, value=1),
                        html.P('Second Selected Month'),
                        dcc.Slider(1, 12, step=None, id='Month_2',
                                   marks=number_month, included=False, value=6)
                    ]), style={'padding': padd_}

            )),
        dbc.Row(
            [
                dbc.Col(w_b_m_1, style={'padding': padd_}, width=6),
                dbc.Col(w_b_m_2, style={'padding': padd_}, width=6),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.P(text_4),
                    ]), style={'padding': padd_}
            )),
        dbc.Row(
            [
                dbc.Col(w_b_m_3, style={'padding': padd_}, width=6),
                dbc.Col(w_b_m_4, style={'padding': padd_}, width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardHeader("Insights:", style={'textAlign': 'center', 'fontWeight': 'bold'}),
                        dbc.CardBody([html.Div(b_5, className="card-text")], style={'textAlign': 'center'}),
                    ], 
                    color="info", inverse=True
                ), width={"size": 8, "offset": 2}
                ),
            ]
        ),        
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H6("Daily Seasonality"),
                        html.P(text_5),
                        html.Div(b_3),
                    ]), style={'padding': padd_}
            )),
        dbc.Row(
            [
                dbc.Col(tabs_accidents_daily, style={'padding': padd_}, width=6),
                dbc.Col(tabs_injuries_daily, style={'padding': padd_}, width=6),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.P(text_6),
                    ]), style={'padding': padd_}
            )),
        dbc.Row(
            [
                dbc.Col(dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_16, style={'height': '55vh'})]),
                                color="info", outline=True),
                                style={'padding': padd_}, width=6),

                dbc.Col(dbc.Card(dbc.CardBody([dcc.Graph(figure=fig_17, style={'height': '55vh'})]),
                                color="info", outline=True),
                                style={'padding': padd_}, width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardHeader("Insights:", style={'textAlign': 'center', 'fontWeight': 'bold'}),
                        dbc.CardBody([html.Div(b_6, className="card-text")], style={'textAlign': 'center'}),
                    ], 
                    color="info", inverse=True
                ), width={"size": 8, "offset": 2}
                ),
            ]
        ),          
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H6("Yearly Seasonality"),
                        html.P(text_7),
                    ]), style={'padding': padd_}
            )),
        dbc.Row(
            [
                dbc.Col(tabs_accidents_yearly, style={'padding': padd_}, width=6),
                dbc.Col(tabs_injuries_yearly, style={'padding': padd_}, width=6),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("Effect of Holidays"),
                        html.P(text_8),
                    ]), style={'padding': padd_}
            )),
        dbc.Row(
            [
                dbc.Col(tabs_accidents_holidays, style={'padding': padd_}, width=6),
                dbc.Col(tabs_injuries_holidays, style={'padding': padd_}, width=6),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("Effect of Weather"),
                        html.P(text_9),
                        dash_table.DataTable(id='weather_df_page', columns=[{"name": i, "id": i} for i in df_w_2.columns], page_current=0,
                                             page_size=5, page_action='custom', style_table={'overflowX': 'auto'}, style_cell={'text-align': 'center',
                                                                                                                               'marginLeft': 'auto', 'marginRight': 'auto', 'fontSize': 12},
                                             style_header={
                                                 'backgroundColor': '#E5E8E8', 'fontWeight': 'bold'},
                                             ),
                        html.P(text_10),
                        html.P('Weather Feature:'),
                        dcc.Dropdown(['Temperature', 'Feelslike', 'Dew Point', 'Humidity', 'Precipitation', 'Windspeed', 'Cloudcover', 'Visibility',
                                      'Solar Radation', 'Solar Energy', 'UV Index', 'Moonphase'],
                                     'Temperature', id='weather-dropdown', clearable=False),
                    ]), style={'padding': padd_}
            )),
        dbc.Row(
            [
                dbc.Col(w_b_m_5, style={'padding': padd_}, width=6),
                dbc.Col(w_b_m_6, style={'padding': padd_}, width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(w_b_m_7), width={"size": 6, "offset": 3}),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    children=[
                        html.H4("Effect of Traffic"),
                        html.P(text_11),
                        dash_table.DataTable(id='mta_df_page', columns=[{"name": i, "id": i} for i in df_mta_temp.columns], page_current=0,
                                             page_size=5, page_action='custom', style_cell={'text-align': 'center',
                                                                                            'marginLeft': 'auto', 'marginRight': 'auto', 'fontSize': 12},
                                             style_header={
                                                 'backgroundColor': '#E5E8E8', 'fontWeight': 'bold'},
                                             ),
                        html.P(text_12),
                        html.P('MTA Traffic Feature:'),
                        dcc.Dropdown(['Subway Passengers', 'Bus Passengers', 'LIRR Passenger', 'Metro North Passengers', 'Bridges and Tunnels Traffic'],
                                     'Bridges and Tunnels Traffic', id='mta-dropdown', clearable=False),
                    ]), style={'padding': padd_}
            )),
        dbc.Row(
            [
                dbc.Col(w_b_m_8, style={'padding': padd_}, width=6),
                dbc.Col(w_b_m_9, style={'padding': padd_}, width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(w_b_m_10), width={"size": 4, "offset": 4}),
            ]
        ),
    ]
)


@callback(Output('fig_5', 'figure'), Output('fig_6', 'figure'),
          Input('Month_1', 'value'), Input('Month_2', 'value'))
def update_figure(Month_1, Month_2):
    month_temp_1 = number_month[Month_1]
    month_temp_2 = number_month[Month_2]

    fig_5 = go.Figure()
    df_temp = df_4[(df_4.Month_ == Month_1) & (df_4.Period == 'Pre-Covid')]
    fig_5.add_trace(go.Scatter(x=df_temp['Day'], y=df_temp['Accidents'],
                    name=f'{month_temp_1} Pre-Covid', line=dict(color='red', width=2)))
    df_temp = df_4[(df_4.Month_ == Month_2) & (df_4.Period == 'Pre-Covid')]
    fig_5.add_trace(go.Scatter(x=df_temp['Day'], y=df_temp['Accidents'],
                    name=f'{month_temp_2} Pre-Covid', line=dict(color='red', width=2, dash='dot')))
    df_temp = df_4[(df_4.Month_ == Month_1) & (df_4.Period == 'Post-Covid')]
    fig_5.add_trace(go.Scatter(x=df_temp['Day'], y=df_temp['Accidents'],
                    name=f'{month_temp_1} Post-Covid', line=dict(color='blue', width=2)))
    df_temp = df_4[(df_4.Month_ == Month_2) & (df_4.Period == 'Post-Covid')]
    fig_5.add_trace(go.Scatter(x=df_temp['Day'], y=df_temp['Accidents'],
                    name=f'{month_temp_2} Post-Covid', line=dict(color='blue', width=2, dash='dot')))
    fig_5.update_layout(yaxis_range=[0, 800])
    fig_5.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1), template='plotly_white',
                        margin=dict(l=5, r=5, t=5, b=5), xaxis_title="Day", yaxis_title="Accidents")

    fig_6 = go.Figure()
    df_temp = df_4[(df_4.Month_ == Month_1) & (df_4.Period == 'Pre-Covid')]
    fig_6.add_trace(go.Scatter(x=df_temp['Day'], y=df_temp['Injuries'],
                    name=f'{month_temp_1} Pre-Covid', line=dict(color='red', width=2)))
    df_temp = df_4[(df_4.Month_ == Month_2) & (df_4.Period == 'Pre-Covid')]
    fig_6.add_trace(go.Scatter(x=df_temp['Day'], y=df_temp['Injuries'],
                    name=f'{month_temp_2} Pre-Covid', line=dict(color='red', width=2, dash='dot')))
    df_temp = df_4[(df_4.Month_ == Month_1) & (df_4.Period == 'Post-Covid')]
    fig_6.add_trace(go.Scatter(x=df_temp['Day'], y=df_temp['Injuries'],
                    name=f'{month_temp_1} Post-Covid', line=dict(color='blue', width=2)))
    df_temp = df_4[(df_4.Month_ == Month_2) & (df_4.Period == 'Post-Covid')]
    fig_6.add_trace(go.Scatter(x=df_temp['Day'], y=df_temp['Injuries'],
                    name=f'{month_temp_2} Post-Covid', line=dict(color='blue', width=2, dash='dot')))
    fig_6.update_layout(yaxis_range=[0, 200])
    fig_6.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1), template='plotly_white',
                        margin=dict(l=5, r=5, t=5, b=5), xaxis_title="Day", yaxis_title="Injuries")

    return fig_5, fig_6


@callback(Output('fig_26', 'figure'), Output('fig_27', 'figure'),
          Input('weather-dropdown', 'value'))
def update_figure(weather_feature):

    fig_26 = px.scatter(df_weather, x=weather_feature, y="Accidents", template='plotly_white', opacity=0.5,
                        facet_col='Period', title=f'Number of Accidents vs. {weather_feature}', trendline="ols", trendline_color_override="red")
    fig_26.update_traces(marker=dict(
        size=5, line=dict(width=1, color='black')))
    model = px.get_trendline_results(fig_26)
    rsq = np.round(model.iloc[0]["px_fit_results"].rsquared, 2)
    fig_26.add_annotation(row=1, col=1, text=f'R-Squared: {rsq}', xref="x domain", yref="y domain", x=0.9, y=0.9, showarrow=False,
                          bordercolor="black", borderwidth=1, borderpad=2, bgcolor="white")
    rsq = np.round(model.iloc[1]["px_fit_results"].rsquared, 2)
    fig_26.add_annotation(row=1, col=2, text=f'R-Squared: {rsq}', xref="x domain", yref="y domain", x=0.9, y=0.9, showarrow=False,
                          bordercolor="black", borderwidth=1, borderpad=2, bgcolor="white")

    fig_27 = px.scatter(df_weather, x=weather_feature, y="Injuries", template='plotly_white', opacity=0.5,
                        facet_col='Period', title=f'Number of Injuries vs. {weather_feature}', trendline="ols", trendline_color_override="red")
    fig_27.update_traces(marker=dict(
        size=5, line=dict(width=1, color='black')))
    model = px.get_trendline_results(fig_27)
    rsq = np.round(model.iloc[0]["px_fit_results"].rsquared, 2)
    fig_27.add_annotation(row=1, col=1, text=f'R-Squared: {rsq}', xref="x domain", yref="y domain", x=0.9, y=0.9, showarrow=False,
                          bordercolor="black", borderwidth=1, borderpad=2, bgcolor="white")
    rsq = np.round(model.iloc[1]["px_fit_results"].rsquared, 2)
    fig_27.add_annotation(row=1, col=2, text=f'R-Squared: {rsq}', xref="x domain", yref="y domain", x=0.9, y=0.9, showarrow=False,
                          bordercolor="black", borderwidth=1, borderpad=2, bgcolor="white")

    return fig_26, fig_27


@callback(
    Output('weather_df_page', 'data'),
    Input('weather_df_page', "page_current"),
    Input('weather_df_page', "page_size"))
def update_table(page_current, page_size):
    return df_w_2.iloc[page_current*page_size:(page_current + 1)*page_size].to_dict('records')


@callback(
    Output('mta_df_page', 'data'),
    Input('mta_df_page', "page_current"),
    Input('mta_df_page', "page_size"))
def update_table(page_current, page_size):
    return df_mta_temp.iloc[page_current*page_size:(page_current + 1)*page_size].to_dict('records')


@callback(Output('fig_29', 'figure'), Output('fig_30', 'figure'),
          Input('mta-dropdown', 'value'))
def update_figure(mta_feature):

    fig_29 = px.scatter(df_mta, x=mta_feature, y="Accidents", template='plotly_white', opacity=0.5,
                        title=f'Number of Accidents vs. {mta_feature}', trendline="ols", trendline_color_override="red")
    fig_29.update_traces(marker=dict(
        size=10, line=dict(width=2, color='black')))
    model = px.get_trendline_results(fig_29)
    rsq = np.round(model.iloc[0]["px_fit_results"].rsquared, 2)
    fig_29.add_annotation(text=f'R-Squared: {rsq}', xref="x domain", yref="y domain", x=0.9, y=0.9, showarrow=False,
                          bordercolor="black", borderwidth=1, borderpad=2, bgcolor="white")

    fig_30 = px.scatter(df_mta, x=mta_feature, y="Injuries", template='plotly_white', opacity=0.5,
                        title=f'Number of Injuries vs. {mta_feature}', trendline="ols", trendline_color_override="red")
    fig_30.update_traces(marker=dict(
        size=8, line=dict(width=2, color='black')))
    model = px.get_trendline_results(fig_30)
    rsq = np.round(model.iloc[0]["px_fit_results"].rsquared, 2)
    fig_30.add_annotation(text=f'R-Squared: {rsq}', xref="x domain", yref="y domain", x=0.9, y=0.9, showarrow=False,
                          bordercolor="black", borderwidth=1, borderpad=2, bgcolor="white")

    return fig_29, fig_30
