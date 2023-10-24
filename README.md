## Building and automating an ETL Pipeline
To set up an automated job that will fetch the data from www.openweathermap.org using API and dump it in AWS S3 Storage on a daily basis. The job will work twice a week and it will collect the data after every three hours. The target city is Delhi, India and we are fetching the below data for below parameters. datetime | min_temp | max_temp | climate | climate_desc | windspeed | humidity

## Tools & Requirements:
Python Programing, Apache Airflow, AWS-EC2, AWS-S3, Visual-Studio

## Step 1: Setting Up AWS & Visual Studio with EC2 instance:
Download Visual Studio and create an account in AWS.
In Visual studio click on ssh connection at the bottom left and then click on "connect to SSH Hosts'. Open config file where you will have to add the host details that you will get from the next step mentioned below.
In Aws create a new EC2 instance with minimun t2.small instance type recommended for this project with ununtu as OS.
Download the Key-Pair file generated while creating the instance.
Provide the pulic ip addresss under hostname, os_type under user and path of the downloaded key_pair path under IdentityFile in step 3 where config was required for new adding new SSH Connection.
Now your EC2 is connected with your Visual studio.
## Step 2: Setting Up ec2 For Airflow
Open the instance in AWS UI and provide the
