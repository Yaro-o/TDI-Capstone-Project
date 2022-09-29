from dash import dcc
# Texts used in EDA page:

text_1 = """Any dataset that is generated from human activities, shows seasonality. As the name suggests, seasonality refers to observable seasonal 
characteristics of a dataset; it's a predictable pattern that repeats in certain interval during a year, such as daily, hourly, weekly, and monthly. 
These predetermined patterns in the dataset will be utilized in better predicting the number of accidents/injuries in the future."""

text_2 = """The first seasonality pattern that we will look into is the weekly seasonality; 
that is, ignoring all other factors, which day of the week shows the most number of accidents/injuries.
Figures below shows the average number of accidents/injuries in each day of the week considering two separate time-frame periods, Pre-Covid and Post-Covid. 
In a secondary plot with is available by the different tabs below, the data is normalized with respect to the highest data point 
to assist the reader in comparing the effects of each element. Several important conclusions can be drawing from the figures below:
"""

text_3 = """Weekly seasonality changes in each month of the year. Figures below show the weekly seasonality of the number of accidents and injuries in 
each month of the year. The sliders below can be adjusted to any month to compare the daily accidents/injury values.
It should be noted that the scale of the figures below are different.
"""

text_4 = """A better way of showing Weekly Seasonality in Different Month is to use a heatmap showing the mean values of all 
    Days of the Week in every Month of the year. This is shown below for both the number of Daily Accidents and 
    the Number of Daily Injuries."""

text_5 = """ Daily seasonality can be observed in the figures below which were constructed by resampling the DataFrame on an hourly basis. 
The values for the number of Accidents and Injuries show the mean values without considering any other effect. Several important conclusions can 
be drawing from the figures below:
"""

text_6 = """The heatmaps below shows the daily seasonality with respect to each day of the week. It can be seen that the increase in the 
number of accidents/injuries during the morning rush hour does not exists in weekends. Also, Fridays 4-5PM shows the highest 
number of accidents/injuries, whether Pre- or Post-Covid. Another observation is that the number of accidents and injuries are higher in 
Saturday and Sunday early mornings compared to weekdays. This could be due to weekend effect and late night adventures of 
young and inexperienced drives going to bars/clubs/restaurants. Comparing the same effect for Pre- and Post-Covid, it can be seen that 
this increase in the early morning accidents/injuries is not as dominant Post-Covid. This can be directly correlated to the social distancing
effect of these facilities during covid."""

text_7 = """Figures below depicts the yearly seasonality. June is usually the month with the highest number of accidents and injuries. February is 
also seen as the month showing the lowest number of accidents and injuries. However, this may be due to the fact that the number of days is February is
lower than other month. Therefore, a simple resampling technique may skew the data to an unrealistic representation. The data is therefore normalized
in the second tab of each figure which considers the number of accidents/injuries in a month with respect to the number of days in the month.
In the normalized figures, January can be seen as the month showing the lowest number of accidents/injuries and summer month showing the highest values.
"""

text_8 = """Traffic patterns changes during holidays. This change in traffic pattern will therefore affect the number of accidents and injuries and should
be studied. A trend between dummy holiday variable and number of accidents/injuries will be very helpful for prediction purposes especially since the value of this
dummy variable is known for any future period. Figure below shows a "bee swarmplot" of number of accidents and injuries for periods of Pre- and Post-Covid.
From the Pre-Covid figures, the accidents show a pattern, highest number of accidents occur during the weekdays, followed by Saturdays, then Sundays, and 
then Holidays. This clearly distinguishable trend in the Pre-Covid era, seems much less apparent in the Post-Covid era. This is possibly due to the effect 
of work-from-home and more people traveling with personal car for vacation during holidays compared to Pre-Covid era.
"""

text_9 = """It is intuitive that weather would be an important factor in the number of traffic accidents and also the severity of traffic accidents.
The daily weather data for the period of study was therefore obtained from VisualCrossing, an online platform which provides readily available DataFrames.
This DataFrame can be viewed below. 
"""

text_10 = """Several weather features are provided in this DataFrame. The figures below show the relation between each of these features and the number of daily 
accidents/injuries. A simple linear trendline is also fitted to the plotted data and the R-Squared value of the fit is shown on each plot.
From the figures below it can be seen that Temperature, Feelslike Temperature, Solar Radiation, and Solar Energy show the highest R-Squared Values when plotted against the 
number of accidents/injuries. Higher temperatures can result in more mechanical problems with respect to older car models. This can be a contributing factor in the higher
number of accidents in higher temperatures days. Also, higher UV Index and Solar Energy may impair the vision of the drivers resulting in higher percentage of human error.
That being said, since summer months show higher accidents/injuries as seen above, one should keep in mind the famous phrase that "correlation does not mean causation".
When developing the predictive models, these weather features will be further scrutinized to ensure the correlation is not just coincidental.
A correlation plot is also provided below. Similar to the conclusions obtained by plotting the weather features individually, it can bee seen that 
Temperature/Feels Like and Solar Energy/Radiation show the highest correlation to the target variables. However, this correlation is significantly larger for 
number of Injuries compared to the number of accidents. It appears that during high temperatures and high solar brightness the number of accidents is only marginally 
higher but the number of injuries is significantly higher. Therefore, more severe crashes occur during high temperature/solar energy days.
"""

text_11 = """It is also intuitive that Traffic count would also be an important factor in the number of traffic accidents. Several injuries involves pedestrians,
therefore, the number of people taking the bus or using the train in a day may also be correlated to the number of accidents/injuries.
The daily Traffic for the period of this study was obtained from NYC Open Data Website. Metropolitan Transportation Authority of the State of New York (MTA) provides
an amazing dataset of number of subways and bus rides and also the traffic on bridges and tunnels operated by the agency. This dataset was used to explore 
the relation between these features and the target variables. This DataFrame can be viewed below:
"""

text_12 = """Several features are provided in this DataFrame. The figures below show the relation between each of these features and the number of daily 
accidents/injuries. A simple linear trendline is also fitted to the plotted data and the R-Squared value of the fit is shown on each plot. A correlation heatmap
is also plotted below between the target variables and the features provided in the MTA dataset. A significant correlation
can be seen between the Daily Traffic on MTA operated bridges and tunnels and the number of accidents/injuries. With an R-Squared value of above 0.3 and a correlation
factor of almost 0.6, this feature should be a valuable asset in predicting the future number of accidents/injuries. The next best feature in this dataset is the number
of daily bus passengers with shows a minor correlation with our target variables. 
"""

text_13 = """ Although the number of accidents dropped rapidly Post-Covid, the number of injuries dropped only slightly, showing, the severe car accidents are still 
occurring and only the number of light/fender-bender accidents has decreased. The work-from-home routine resulted in more accidents over the weekend, and less accidents 
during the weekdays. 
"""

# Texts used in ESDA Page:

text_esda_1 = """ Exploratory Spatial Data Analysis (ESDA) extends upon a typical EDA to find patterns and valuable information using locational 
properties of the dataset, specifically Latitude and Longitude of every accident. There are several techniques in ESDA such as determining 
spatial autocorrelation and locating clusters and outliers. Let's start by visualizing the dataset overlaid over a map of New York City. Figure below shows 
the spatial distribution of the accidents Post-Covid. With a very low opacity attribute for plotting the data-points, certain hot-spots can be 
easily distinguished. Staten Island shows a lower number of accidents compared to other boroughs. Certain highways and parkways also show a large number
of accidents. 
"""

text_esda_2 = """A better way of visualizing the density of accidents and locating the hot-spots is binning. Hexagonal binning is a popular method for spatial datasets.
In a 2-D space, hexagons offer several advantages in binning, they are more similar to circles compared with squares or triangles and there is no point 
connection between neighboring hexagons as opposed to squares which have 4 point and 4 side neighbors and triangles which have 9 points and 3 side neighbors.
"""

text_esda_3 = """
Figure below shows a Hexabin density animation plot of the number of accidents in each hour of the day. Note that the Hexabins with a density of less than 5 are not shown
for clarity. By hitting the "play" button, you are basically observing the heartbeat of New York City as the population wakes up for work, commutes to home, and sleeps. 
Each hexagonal side is almost the size of 2 city blocks. The number of Hexabins can be changed to capture smaller distances, however, two city blocks seems a reasonable bin 
size for this purpose, it captures even the larger complex intersections in one bin which can be beneficial for our observation. 
"""

text_esda_4 = """
Certain hot-spots can be easily distinguished using the plot below. It seems that complex intersections with multiple lanes/service roads are prone to more accidents 
especially during rush hours. Besides these intersections, accidents tend to occur on highway, parkways, state routes in which speed limit is higher than local streets.
"""

text_esda_5 = """
Instead of a randomized binning of the dataset, another dataset can be used to assign every accident to a specific road and then analyze the road sections with the
most number of accidents. This dataset was obtained from data.cityofnewyork.us which contains road-bed representation/geometry of all New York City streets. The size
of this dataset is almost 40MB. It contains 120,811 rows and 32 features. The features that will be used in this study are "the_geom" or the geometry, "FULL_STREE"
which is the full street name of the geometry and the SHAPE_LENGTH which is the length of the geometry. The geometry feature is recoded as a multilinestring 
which is a collection of linestrings. Multilinestrings are generally used to define a road network. In this dataset, most of the Multilinestrings geometries
are just a single line, depicting a straight street. However, some geometries contain multiple lines that are connected together to depict a wavy road. 
A sample of this dataset can be seen below:
"""

text_esda_6 = """
The figures below have been plotted by merging this dataset to the original vehicle collisions dataset. GeoPandas and specifically the geopandas.sjoin_nearest() function
has been used to assign a unique road segment from the CSCL dataset to every accident based on the Latitude and Longitude of the accident. 
In the first tab, the the linemap has been color coded based on the number of accidents per road segment. Four color codes has been chosen based on various 
"percentile" of the data, red shows the top 1% dangerous roads, orange shows the top 5%, and light green shows the top 10%, and green shows the bottom 90%. 
Certain highways such as Belt Parkway, FDR, Cross Island Parkway, Henry Hudson Parkway, and Grand Central Parkway, are among the top 1% dangerous road segments, showing
a higher number of accidents. 
"""

text_esda_7 = """
Before digging in further, a limitation/bias of this visualization is to be discussed. Since the road segments in CSCL dataset discussed above do not have a the same length,
longer road segments may be assigned with higher number of incidents and appear to be more prone to accidents. In order to overcome this issue, in the second tab below, 
the number of accidents per road segment has been divided by the respective length of the segment (then multiplied by 100 ft. in order to deal for whole numbers). 
Therefore, each count represents the number of accidents per 100 ft. of each roadsegment. This Figure has also been color coded using the same percentile methodologies, 
top 1%, 5%, 10%, and the rest. It can be seen that the nature of the roadsegment classified as red or dangerous has been modified tremoundeously compared to the first figure. 
Now highways and parkways are shown to be very safe, and mostly intersections are described as the highest accident prone areas. 
For instance, almost all intersections in Atlantic Avenue in Brooklyn is classified as the top 1% accident prone areas. 
"""

text_esda_8 = """
The purpose of a clustering algorithm is to locate the natural grouping of a set of unlabeled datapoints using one main principle, the points that are closer 
to eachother present a more similar bevahior compared to points farther from eachother. A clustering algorithm usually required very minimal domain knowledge.
k-means clustering is amongst the olders and most-widely-used algorithms for clustering of unlabeled dataset. However, it has several disadvantages such as:
"""

text_esda_9 = """
Due to the above-mentioned disadvantages of k-means algorithm, a density based clustering algorithm has been used in this study, namely, Density Based Spatial 
Clustering of Applications with Noise (DBSCAN). The advantages of DBSCAN over k-means are:
"""

text_esda_10 = """
DBSCAN has two hyperparameter, Epsilon (eps) and minimum number of points (min_samples). Epsilon is the max radius of neighorhood, bascilaly, two data points will 
be considered neighbors if their distance is less than Epsilon. In other words, Epsilon is the distance that DBSCAN uses to determine if two points belong to a single 
cluster. The hyperparameter minPts also determines the minimum number of points within the radius Epsilon for the neighborhood to be considered a cluster.
"""

text_esda_11 = """
Figure below show the result of DBSCAN on the Accident Dataset. Different values of eps and min_samples can be chosen and the plot will be updated automatically.
It can be seen that mostly intersections with complex road design is chosen by the algorithm as the accident hot-spots. Some of the clusters were further analyzed by
looking at a satelite image from Google Maps. Tabs below show the select few.
"""

text_esda_12 = """
Spatial Autocorrelation generally refers to presence of spatial dependance in a geographically mapped variable. For instnace, from the hexabins presented in the figure
above, it can be seen that generally high-accident bins and low-accidents bins are close to each other. Spatial Autocorrelation finds a way to quantify this correlation.
The main goal of Spatial Autocorrelation is to determine the degree to which the value of a location is similar to neighbor values.
Figure on the right shows a visualization of Spatial Autocorrelation; in a positive Spatial Autocorrelation all high and low values are clustered together, in a negative
Spatial Autocorrelation high values are neighboring by low values and vise-versa (similar to a checkerboard), 
and when there is no Spatial Autocorrelation, the high and low values are just randomly distributed.
"""

text_esda_13 = """
Moran's I is a simple method of measuring Spatial Autocorrelation. Similar to a regular correlation coefficient, Moran's I takes a value between -1 and +1 and determines
how well the variable is clustered together in high and low areas. Moran also defines a significant level using Monte Carlo simulation to determine weather the labling 
of each bin in the dataset is significant or not.
"""

text_esda_14 = """
A Moran's I coefficient of 0.94 was obtained for the Accident dataset. It shows that accidents are highly clustered together, accident-prone areas are sorrounded by eachother
and low-accidents areas are also clustered together. Further, this can be visually plotted to observe the clusters are accident-prone areas. 
Certain areas in Manhattan, Bronx, and Brooklyn can be seen to show highly correlated accident prone areas whereas Staten Island and Queens mostly contain Low-Low clusters.
Major Avenues show High-High clusters which clasifies these areas as accident hot-spots.
"""

# Texts used in Intro Page:

text_intro_1 = """In 2021, 42,915 people died in motor vehicle traffic accidents. National Highway Traffic Safety Administration (NHTSA) estimates the total economical impact 
of all traffic accidents to be almost $1 trillion; a whopping 4.3% of the Gross Domestic Product (GDP) in the US.
Globally, the World Health Organisation estimates road traffic accidents to be the eighth leading cause of deaths, with over 1.3 million fatalities costing on average 
around 3% of countries GDP. This study presents an in-depth analysis of the Motor Vehicle Collisions Dataset provided by the NYC Open Data to gain insights and present
recommendations and approaches to increase the safety of the traveling public.
"""

text_intro_2 = """
The approach taken to tackle this project is shown in the flowchart below.
"""

text_intro_3 = """
The benefits of a thorough study on Vehicle Collisions can be summarized as:
"""

# Texts used in Baseline Models Page:

text_bm_1 = """
The first step to developing a predictive model is to find, define, and tune a baseline model. This way, the performance of final chosen model 
can be compared to a baseline to ensure the extra complexity and computational expense, worth it. Several widely used models that are common in 
Time-Series analysis in the literature is utilized here. 
"""
text_bm_2 = """
Naïve Forecasting method is probably the simplest method of time-series forecasting. Using Naïve method, the last datapoint is used as forecast
for the next period. 
"""

text_bm_3 = """
Mean Absolute Error is used as the main metric to compare the models together. Each model will be tested for a 
period of one week in future, which is our main objective, in a 12-fold cross validation time-series split. 
The mean and standard deviation of the 12-fold scores is reported on the plots.
"""

text_bm_4 = """
Rolling Average forecast method is similar to Naïve. The only difference is that the algorithm uses the average of the last 7-day (instead of just
the last day alone) as prediction for the next period.
"""

text_bm_5 = """
Similar to the previous tab, the average of the last 21-day is used as prediction for the next period.
"""

text_bm_6 = """
Naïve-seasonal uses a lag as prediction for the next period.
"""

text_bm_7 = """
Naïve-seasonal can also be used to use an average of number of lags (in this case 4-lags) as prediction for the next period.
"""

text_bm_8 = """
Exponential smoothing uses a exponential decaying function to predict the next period based on the results of last periods, with one simple caveat,
the most recent periods, carry a bigger weight in prediction.
"""

text_bm_9 = """
From the figures above, it can be seen that the 21-Day Rolling Average is the most accurate method in predicting the target variable. The mean cv score 
of this method is 17.2 with a standard deviation of 6.31. Now the question is, whether another model can predict the target variable more accurately
or this is the most accurate model can come up with? It is intuitive that any variable related to human activity, such as number of daily injuries, has some
degree of randomeness/unpredictability in it, therefore, it cannot be 100% accurately predicted. But how can one determine whether that threshhold is reached and the model 
cannot be improved any longer. This is where residual plots come handy. Bascially, the residuals will be studied to see whether they are just purely random, 
or they show some sort of pattern that can also be predicted. There are several methods in studying the residuals of a predictive model. 
Tabs below go through the most common methods for residuals analysis.
"""

text_bm_10 = """
If the residuals are truly random, they should follow a normal distribution. Plot below shows the distribution of the residuals vs. a normal distribution plot fitted 
to the data. Towards the tails of the plot, the values are a bit higher than the fit line, but in general, the path of normal distribution is followed pretty closely
"""

text_bm_11 = """
A Quantile-Quantile plot as show here, also compares the quantile of the residuals with that of a normal distribution to see how closely they are related. 
It can again be seen that towards the tails of the plot, the values do not match 100%.
"""

text_bm_12 = """
Autocorrelation plots show the correlation between a variable and its own lag. In a truly random dataset, no correlation would be observed between the data and its lag. 
Figure below shows that some predictable portion of the data is still left in there. For instance, the correlation of the residuals with respect to its 7th lag (one week),
is above the uncertainty band, meaning, the baseline model was not able to capture the entirety of the weekly seasonality of the target variable and there is still some 
seasonality left in the dataset.
"""

# text_bm_13 = """
# Although the Autocorrelation plot shows some significant values, one could say that the residuals may be "random walk" data, meaning, there is indeed some correlation 
# within the dataset, however, the data cannot be predicted. In random walk, the value of next period is dependant upon last period plus some noise. Random walk shows
# high autocorrelation but it does not mean that it can be predicted, as it is still purely random. A partial autocorrelation plot can be used to ensure the residuals are
# not purely random. Plot below still shows some significance within the residuals. 
# """

# Texts used in Dashboard:
text_dash_1 = """
NYC Open Data provides the Motor Vehicle Collisions crash dataset containing details of every crash event based on police reports. 
Every row of this dataset relates to a collision in which someone is injured or killed, or where there is at least $1000 worth of damage. 
The dataset has more than 1.9M rows and is updated almost daily. A preliminary analysis of this dataset is presented in this dashboard. 
Accident prone zone is also identified using state-of-the art Machine Learning Algorithms. Moreover, the total number of injuries is predicted 
for the following week. Note that the analyzed data is up to July 8th of 2022, The prediction is provided till July 15th of 2022.
"""

# Texts used in Machine Learning Models:
text_ml_1 = """
Linear Regression, Logistic Regression, and XGBoost is used here to perform time-series analysis on the number of Daily Injuries. Similar to the Baseline Models, a 12-Fold
cross validation is used to assess the performance of each model and compare them with the baseline model. Mean-Absolute-Error is also used as a scoring method. The results
are shown in the tabs below.
"""

text_ml_5 = dcc.Markdown("""
Using EDA, the most important features was used to develop a predictive model. Namely, Temperature, Total number of Traffic on MTA Bridges and Tunnels, Solar Radiation, 
was used as the most relevant features based on EDA. One problem with using such variables as features for the model is that the future value of these variables is unknown. 
This is a common problem is time-series analysis. A very simple workaround yet effective method to offset this problem is to use a **lag** of these variables. 
For instance, instead of using today's temperature to predict the number of injuries, we can use last week's temperature. This way, we predict into the future
by inputting the current values. 
""")

text_ml_6 = dcc.Markdown("""
Using various **Autocorrelation** plots, the most relevant lag values were used as input for the model. After a thorough analysis, the following were chosen as the most 
relevant feartures to develop the model:
""")

text_ml_7 = dcc.Markdown("""
    * 7-Day Lag of Temperature
    * 8-Day Lag of Temperature
    * 7-Day Lag of 30-Day Rolling Average of Temperature
    * 30-Day Lag of Solar Radation
    * 7-Day lag of Target Variable
    * 8-Day Lag of Total Number of Traffic on MTA Bridges and Tunnels
""")

text_ml_2 = """
Linear Regression is probably the simplest and most widely used Machine Learning algorithm. The results of the 12-Fold Cross Validation and the next-week prediction
is showsn in the figure below. Temperature and Number of Traffic on MTA Bridges and Tunnels carry the highest coefficient in the model. 
"""

text_ml_3 = """
Logistic Regression was also used as a traditional Machine Learning Algorithm to predict the number of Daily Injuries. The model performed worse than Linear Regression.
The C parameter of the algorithm was tuned using the result obtained from 12-Fold Cross Validation. The best results achieved is shown in the figure below.
"""

text_ml_4 = """
XGBoost is a very strong algorithm capable of achieving highly accurate results. Using the same features discussed above, XGBoost model was tuned with the goal of obtaining 
more accurate results compared to the baseline models. Number of Estimators, Maximum Depth, Learning Rate, Column Sample Rate by Tree, Parameter Sample Rate by Tree, and Gamma 
Regularization Term were tuned using the results obtained from 12-Fold Cross Validation. For each of these parameter, a test vs. train graph were plotted for multiple values
to achieve the best performing model. It can be seen that XGBoost performed slightly better compared to the basemodels and Linear Regression. 
"""

# Texts used in Art:

text_art_1="""
Prophet (Developed and Open-Sourced by Meta) is a state-of-the-art model for Time Series analysis and forecasting. Prophet is particularly good in handling Time Series with 
multi-level seasonality; in our dataset, presence of Daily and Monthly seasonality has been discussed previously in the EDA section. At its core, it operates as an additive 
model by breaking down the target variable into several smaller sub-sections as described below:

"""

text_art_2=dcc.Markdown('''
    * Growth, g(t): By default the model approximates the total linear upward or downward trend of the data. This trend can be changed at so-called "changepoints". 
    The number of changepoint can be determined as a hyperparameter in the model. A logistic growth function can also be defined as an alternative to the linear model.
    * Seasonality, s(t): Fourier Series as function of time is used to approximate seasonality. The number of Fourier Series Terms can be defined in the model; the higher 
    the model, the better fit to training data, and more chance of overfitting. 
    * Holiday, h(t): Dummy variables are used to address Holidays and Special Events such as Black Friday sales, etc. 
    * Error term, ε(t): This term quantifies any changes that the other components of the model were not able to capture. Prophet assumes that this error term is normally 
    distributed.
''')

text_art_3="""
Due to this decomposing style of modeling, the result is extremely interpretable. Prophet also provides several built-in plots to better observe this decomposition in effect.
Similar to Prophet, LinkedIn also developed a model, Silverkite, which uses similar decomposition as Prophet and uses Lasso/Ridge for final molde building and prediction. 
Below you can find the prediction result for both Prophet and Silverkite are reported below.
"""



##################################################################################################################################
#                           MARKDOWNS
##################################################################################################################################
# Markdowns used in eda:

b_1 = dcc.Markdown('''
    * The number of daily accidents was dropped by almost 50% Post-Covid, however, the number of accident related injuries dropped by only 11%. This
    shows that although the number of accidents was decreased considerably, possibly caused by less traffic on roads, the number of injuries did not decrease
    by the same rate. Therefore, the severe crashes resulting in injuries are still occurring the same tune that they were occurring Pre-Covid.
    * By looking at the normalized plots, it can be seen that the weekly seasonality of the number of accidents and injuries was dampened Post-Covid. 
    For instance, Pre-Covid the number of accidents and injuries on Sundays was less than Fridays by 27% and 12%, respectively. 
    However, this dropped was changed to 16% and 7% Post-Covid. This shows a significant pattern shift in the data due to Covid which can 
    be correlated to less traffic during weekdays due to the effect of **Work-From-Home**,
    and more traffic on Weekends as people are more likely to get out of the house.
''')

b_2 = dcc.Markdown('''
    * It can again be seen that the number of Accidents are significantly apart for the Pre-Covid and Post-Covid era. However,
    number of daily injuries are rather closer.
    * The effect of holidays can also be recognized during different month. For instance, for the number of accidents, generally,
    Thursday is the second highest day of the week. However, in November, due to Thanksgiving, the number of accidents drop slightly on Thursday.
    Similarly, in September, due to Labor Day Holiday, the number of accidents in Monday shows a lower trend compared to other month.
    It can therefore be concluded that an accurate weekly seasonality should also consider the month effect and the Holidays in each month.
    * By looking at the normalized plots, it can be seen that the weekly seasonality of the number of accidents and injuries was dampened Post-Covid. 
    For instance, Pre-Covid the number of accidents and injuries on Sundays was less than Fridays by 27% and 12%, respectively. 
    However, this dropped was changed to 16% and 7% Post-Covid. This shows a significant pattern shift in the data due to Covid which can 
    be correlated to less traffic during weekdays due to the effect of **Work-From-Home**,
    and more traffic on Weekends as people are more likely to get out of the house.
''')

b_3 = dcc.Markdown('''
    * Two distinct peak can be observed in the data, one around 8AM during the morning rush hour and another around 4PM during the afternoon rush hour.
    * The effect of these two peaks in the Accident data is dampened Post-Covid. As it can be seen from the Normalized plots.
    The drop in the number of Accidents from the 4PM afternoon rush hour to the 3AM early morning for Pre-Covid and Post-Covid is 86% and 74%.
    This can again show that due to the effect of **Work-From-Home**, less people are likely to drive during the regular rush hours.
    * A peak in the midnight can also be observed. However, this peak should be analyzed with some level of uncertainty. It appears that the
    "0:00" time is the default time in the DataFrame. So it is difficult to distinguish whether this input is actual or a placeholder.
    For the purpose of this study, this peak can be ignored.
''')

b_4 = dcc.Markdown("""
> Although the number of accidents dropped rapidly Post-Covid, the number of injuries dropped only slightly, showing, 
the severe car accidents are still occurring and only the number of light/fender-bender accidents has decreased. 
>
> The work-from-home routine resulted in relatively more accidents over the weekend, and less accidents during the weekdays; flattening the weekly seasonality. 
""")

# Markdowns used in esda:

b_esda_1 = dcc.Markdown("""
> Highways, Parkways, and State Routes with highers speed limits show higher number of accidents
>
> Complex intersections are prone to accidents. 
> 
> Since the exact coordination/center of each hexabin cannot be determined, the density plot may somewhat suffer from this randomization. 
For instance, a hexabin can fall in the middle of an intersection and as a result, the data will not be comparable to other bins. A better way of "binning" 
should be explored instead to obtain solid conclusions.
""")

b_esda_2 = dcc.Markdown("""
> If only the number of accidents per road is considered, highways and parkways are classified as the most accident prone areas.
>
> If the average number of accidents per 100 ft. is considered, intersections are classified as the most accident prone areas.
> 
> Using the CSCL dataset it is difficult to analyze the accident data without any bias. It is noted that the method of separating the road network into road segments
severly affects the outcome of the classification.
> 
> An unsupervised classification Machine Learning method can be used instead to find accident hot-spots without any regards to street segments.
Using a clustering algorithm accidents at an intersection will not be assigned to different road segments, instead, the entire intersection can be classified 
as an accident prone zone.
""")

b_esda_3 = dcc.Markdown("""
    * The number of clusters has to be pre-defined, requiring some domain knowledge. In this study, the number of accident-prone areas is unknown and should
    be decided by the algorithm itself rather than a pre-defined value. 
    * Since the "closeness" of datapoints is defined in a Euclidean space, only circular shapes are expected and irregular shapes are bascically ignored. In this
    study, an intersection with a cross-like shape or a wavy parkway can show some difficulty in being classified as a cluster.
    * Noise is not accounted for, as every point has to be assigned to a cluster.
""")

b_esda_4 = dcc.Markdown("""
    * The number of clusters does not need to be pre-defined. Based on the input values, the algorithm will detect how many clusters matches the criteria which is
    specified.
    * Any arbitrary shape can be identified as a cluster based on "density-reachability".
    * Any datapoint that is not part of a cluster, is adentified as noise or outlier.
""")

b_esda_6 = dcc.Markdown("""
> Moran's I Spatial Autocorrelation can be used to identify accident hot spots. 
>
> It was shown that the spatial distribution of accidents is highly correlated, i.e., high accident and low accidents areas are clustered separately. 
> 
> This shows that the hot zones can be easily recongnized and addressed in a traffic study to lower the number of accidents. 
""")

b_esda_5 = dcc.Markdown("""
> Locations identified by DBSCAN as accident hot-spots usually contain several cross roads in a rather confusing intersections in which a major road crosses one or two local
streets somtimes containing service routes as well. 
>
> There are limited number of pedestrian protection devices such as bullards or tubular markers, which may make the pedestrians more vulnerable in these intersections.
> 
> The results from DBSCAN algortithm can be used to perform an in-depth traffic study to better understand why certain intersections are accident-prone zones.
""")

# Markdowns used in intro:
b_intro_1 = dcc.Markdown("""
    * The number of accidents that are likely to occur in future can benefit insurance companies in determining the cost of the premiums. 
    Further, it can assist the Emergency Medical Department and the Police Departments to better optimize their workforce; for instance, 
    if a relatively low number of accidents is anticipated for the coming week, the number of on-call personnel can be reduced. 
    * The knowledge of accident prone locations can assist residents and even rideshare companies to take safer routes. Services like GoogleMap 
    and Waze can adjust their routes to choose relatively safer options and to avoid areas with increased risk of accidents. This is similar to 
    avoiding traffic jams by choosing less congested routes.
""")

# Markdowns used in Baseline Models:
b_bm_1 = dcc.Markdown("""
> 21-Day roling average model can pretty acurately predict the number of daily injuries.
>
> Based on alayzing the residuals of the baseline model, a more accurate model should be sought after as there still exists some predictable behvaior in the residuals. 
""")