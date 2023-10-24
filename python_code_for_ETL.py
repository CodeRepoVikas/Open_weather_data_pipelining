from airflow import DAG
from datetime import datetime,timedelta
from airflow.providers.http.sensors.http import HttpSensor 
from airflow.providers.http.operators.http import SimpleHttpOperator 
from airflow.operators.python import PythonOperator
import json

import pandas as pd
import requests as r
import json
from datetime import datetime


def kel_to_celcius(kel):
  return kel-273.15

def tranform_data(task_instance):
    jdata=task_instance.xcom_pull(task_ids='extract_weather_data') #Pull the data from the privous task output
    city=jdata['city']['name']
    country=jdata['city']['country']
    mintemplst=[]
    maxtemplst=[]
    cllst=[]
    wslst=[]
    clmtdeslst=[]
    humlst=[]
    datelst=[]
    for i in range(0,jdata['cnt']):
        date=datetime.utcfromtimestamp(jdata['list'][i]['dt'] + jdata['city']['timezone'])
        min_temp=kel_to_celcius(jdata['list'][i]['main']['temp_min'])
        max_temp=kel_to_celcius(jdata['list'][i]['main']['temp_max'])
        climate=jdata['list'][i]['weather'][0]['main']
        windspeed=jdata['list'][i]['wind']['speed']
        climatedesc=jdata['list'][i]['weather'][0]['description']
        humidity=jdata['list'][i]['main']['humidity']
        datelst.append(date)
        mintemplst.append(min_temp)
        maxtemplst.append(max_temp)
        cllst.append(climate)
        wslst.append(windspeed)
        clmtdeslst.append(climatedesc)
        humlst.append(humidity)
    data_dict= {'date': datelst,
           'min_temp':mintemplst,
           'max_temp':maxtemplst,
           'climate': cllst,
           'climate_desc': clmtdeslst,
           'windspeed':wslst,
           'humidity': humlst}
    data_frame=pd.DataFrame(data_dict)                  #converting the json into DataFrame
    now=datetime.now()                                     #Will Give CUrrent time
    dt_string=now.strftime('%d%m%Y%H%M')                   #Formatting it
    dt_string= 'last_data_load_'+dt_string                  # creating the file Name                      
    #data_frame.to_csv(f"{dt_string}.csv", index=False)      # loading the file...
    data_frame.to_csv(f"s3://open-weather-airflow-data-dump-daily/{dt_string}.csv", index=False)
    

default_args= {
'owner':'airflow',
'depends_on_past':False,
'start_date': datetime(2023,10,24),
'email': ['vikas.ten96@gmail.com'],
'email_on_failure': False,
'email_on_retry' : False,
'retries':2,
'retry_delay':timedelta(minutes=2)   
}

with DAG('weather_dag_api',
        default_args=default_args,
        schedule_interval = '@daily', 
        catchup=False) as dag:

        is_weather_api_ready = HttpSensor(   #httpsensor is used for testing the website whether it's working and giving back the data using api
            task_id = 'is_weather_api_ready',                  #standrd in a particular DAG
            http_conn_id='weather_api',                        #connection we are creating in Airflow
            endpoint ='/data/2.5/forecast?q=Delhi&appid=01e697aa5473af26f191dd892c021b7b'   
        )

        extract_weather_data = SimpleHttpOperator(
            task_id='extract_weather_data',
            http_conn_id = 'weather_api',                                        
            endpoint ='/data/2.5/forecast?q=Delhi&appid=01e697aa5473af26f191dd892c021b7b',  # Path URL along with the api cred...
            method = 'GET',                                                          # Get/POST
            response_filter = lambda r: json.loads(r.text),                          # Applying funtion for converting the load data that was in text into JSON format
            log_response=True                                                        # For logs
        )

        transform_loaded_data= PythonOperator(
            task_id='transform_loaded_data',
            python_callable=tranform_data                                             # Funcation to run for the particukar task(transform_loaded_data)

        )

        is_weather_api_ready>>extract_weather_data>>transform_loaded_data


# url='https://api.openweathermap.org/data/2.5/forecast?q=Delhi&appid=01e697aa5473af26f191dd892c021b7b
