# TDI Capstone Project

This repository contains all source files to develop and deploy the nycaccidents.app web application. The following resources was used to build this app:

### Data
* The accident dataset was obtained from [NYC Open Data](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95). This dataset is updated daily and contains more than 1.9 million rows and 29 columns. The total size of the dataset is **400+ MB**. Every row contains the details of one accident such as date, time, location, etc.
* The weather dataset was obtained from [Visual Crossing](https://www.visualcrossing.com/). This dataset contains daily weather information such as temperature, precipitation, UV index, etc.
* The traffic data was obtained from [NYC Open Data](https://data.cityofnewyork.us/Transportation/MTA-Data/mmu8-8w8b). This dataset contains daily information regarding traffic/ridershpi on subways, buses, commuter rail, bridges, and tunnels that are operated by MTA.
* The Street Centerline was also obtain from [NYC Open Data](https://data.cityofnewyork.us/City-Government/NYC-Street-Centerline-CSCL-/exjm-f27b). This dataset has more than 120,000 rows. Every row contains information of a street/parkway/highway segment. 

### Framework for building the App:
[Dash Plotly](https://dash.plotly.com/introduction) was used to build this dashboard. 
Dash is a framework for building highly-customizable, data-oriented, user interfaces apps and dashboard in Python.

### Deployment:
The developed app was deployed using Google Cloud and Google App Engine. The dataset files and any other files were stored in the Google Cloud Storage bins, accessible by the app. A flexible environment with 1 CPU core and 4 Gb of memory was used to take an app online. The flexible environment is capable of automatically scaling up to 10 instances-if needed.
