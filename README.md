## Building and automating an ETL Pipeline
To set up an automated job that will fetch the data from www.openweathermap.org using API and dump it in AWS S3 Storage on a daily basis. The job will work twice a week and it will collect the data after every three hours. The target city is Delhi, India and we are fetching the below data for below parameters. \
o/p Data Format: 
datetime | min_temp | max_temp | climate | climate_desc | windspeed | humidity

## Tools & Requirements:
Python Programing, Apache Airflow, AWS-EC2, AWS-S3, Visual-Studio

## Step 1: Setting Up AWS & Visual Studio with EC2 instance: 
1) Download Visual Studio and create an account in AWS.
2) In Visual studio click on ssh connection at the bottom left and then click on "connect to SSH Hosts'. Open config file where you will have to add the host details that you will get from the next step mentioned below.
3) In Aws create a new EC2 instance with minimun t2.small instance type recommended for this project with ununtu as OS.
4) Download the Key-Pair file generated while creating the instance.
5) Provide the pulic ip addresss under hostname, os_type under user and path of the downloaded key_pair path under IdentityFile in step 3 where config was required for new adding new SSH Connection.
6) Now your EC2 is connected with your Visual studio.

## Step 2: Setting Up ec2 For Airflow
1) Open the instance in AWS UI and connect to your EC2 instance.
2) Run the below command:
   sudo apt update
  sudo apt install python3-pip
  sudo apt install python3.10-venv
  python3 -m venv airflow_venv
  sudo pip install pandas
  sudo pip install s3fs
  sudo pip install apache-airflow
  airflow standalone
3) Now after running the below commands and copying the public ipv4 DNS and paste it in the browser search bar and add ':8080/home' at the end of the url.
4)  After providing the credentials, you can see Apache airflow running on your instance.

## Step 3: Set up the S3 Bucket.
 1) Create a new S3 bucket.
 2) Add an IAM role( AmaxonEC2FullAccess & AmazonS3FullAccess) attached to the instance so that the instance can dump the file in the S3 bucket created above.
## Step 4: Creating the python code:
1) Generate a free API from the host.  https://openweathermap.org/api
2) import the important libraries.
3) define the default arguments for the dag.  
4) create a user-defined function that will process the fetched data from the json format and convert it into the dataframe. After converting into dataframe the data needs to be dumped in the S3 file path.
5) create a task that will test whether the API  is responding or not using HttpSensor.
6) One task that will GET the data from the website using SimpleHttpOperator.
7) We will include one more task that will call the function using PythonOperator created at the step for performing ETL to the data.
8) also we will mention the tasks position and how they will run in the airflow here.

## Step 5: Setting up the Airflow:
1) Open the airflow in the browser.
2) create a new connection that will help us to test the data from or fetch the data from the OpenWeatherMap website.
3) In connection id mention the http_conn_id you name in the python file for the task, in connection_type mention 'HTTP' and in host write the domain name of url i.e https://api.openweathermap.org. Save the file.
4) Refresh the Dag, You will see the new conn that you have created.
5) now open the dag and you will see the tasks are aligned as you have mentioned in the python file.
6) Run the dag, you can see the status for each task if it is green that means your dag ran successfully also check the file in the S3 bucket.
7) If there is any chance the dag has failed, check the log for the failed task.

## Reference:
A big thanks to Tuplespectra for such a good explanation.
https://www.youtube.com/watch?v=uhQ54Dgp6To
https://www.youtube.com/watch?v=0_caTDCZnd0
https://www.youtube.com/watch?v=sQQjMnEkGjs

