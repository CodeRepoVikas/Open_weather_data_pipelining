# Open_weather_data_pipelining
Objective:
To set up an automated job that will fetch the data from www.openweathermap.org using API and dump it in AWS S3 Storage on a daily basis. The job will work twice a week and it will collect the data after every three hours. The target city is Delhi, India and we are fetching the below data for below parameters.
datetime | min_temp	| max_temp | climate	| climate_desc	| windspeed	| humidity



