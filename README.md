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

 ## setting the S3 Bucket.
 1) Create a new S3 bucket.
 2) Add an IAM role( AmaxonEC2FullAccess & AmazonS3FullAccess) attached to the instance so that the instance can dump the file in the S3 bucket created above.
## Creating the python code:
1) 
