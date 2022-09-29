import pandas as pd

from google.cloud import storage
import google.cloud.storage
import json
import os
import sys
import pandas as pd 
import io
from io import BytesIO

#Method#1:
PATH = os.path.join(os.getcwd() , 'silicon-smithy-363322-a66a48ae0291.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PATH
storage_client = storage.Client(PATH)
bucket = storage_client.get_bucket('silicon-smithy-363322.appspot.com')
df = pd.read_csv(io.BytesIO(bucket.blob(blob_name = 'Data/Motor_Vehicle_Collisions_-_Crashes.csv').download_as_string()), encoding='UTF-8', sep=',',
                    dtype={'CRASH DATE': 'str', 'BOROUGH': 'str', 'LATITUDE': 'float32',  'LONGITUDE': 'float32', 'NUMBER OF PERSONS INJURED': 'int8',
                                'NUMBER OF PERSONS KILLED': 'int8', 'NUMBER OF PEDESTRIANS INJURED': 'int8', 'NUMBER OF PEDESTRIANS KILLED': 'int8',
                                'NUMBER OF CYCLIST INJURED': 'int8', 'NUMBER OF CYCLIST KILLED': 'int8', 'CONTRIBUTING FACTOR VEHICLE 1': 'str',
                                'PHYSICALID': 'int32'})

df['CRASH DATE'] = pd.to_datetime((df['CRASH DATE']), format="%m/%d/%Y %H")
df['Hour'] = df['CRASH DATE'].dt.hour
df['Day'] = df['CRASH DATE'].dt.day_name()
df['Month'] = df['CRASH DATE'].dt.month_name()
df['Count'] = 1

df_streets = pd.read_csv(os.path.join('Data/Centerline.csv'), dtype={
                         'L_LOW_HN': 'str', 'L_HIGH_HN': 'str', 'R_LOW_HN': 'str', 'R_HIGH_HN': 'str'})
df_streets = df_streets[~df_streets.RW_TYPE.isin(
    [5, 6, 7, 8, 10, 11, 12, 13, 14])]


df_weather_temp = pd.read_csv(os.path.join('Data/Weather.csv'))
df_weather_temp['datetime'] = pd.to_datetime(df_weather_temp['datetime'])

df_mta_temp = pd.read_csv(os.path.join('Data/MTA_Daily_Ridership_Data__Beginning_2020.csv'), 
                            usecols=['Date', 'Subways: Total Estimated Ridership', 'Buses: Total Estimated Ridership', 
                                        'LIRR: Total Estimated Ridership', 'Metro-North: Total Estimated Ridership',
                                        'Bridges and Tunnels: Total Traffic'])
df_mta_temp.columns = ['Date', 'subway', 'bus', 'lirr', 'mnorth', 'bandt'] 
df_mta_temp['Date'] = pd.to_datetime(df_mta_temp['Date'])