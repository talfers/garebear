# Permit Crawler
Application used to crawl recreation.gov permit availability webpages and alert when specified permits are available during desired time periods.


## Environment setup
In order to run and develop this application, you will need to create a virtual environment and install all necessary dependencies. To do this run the below commands:


#### Create your virtual env
```python
python3 -m venv venv
```

#### Activate your virtual env
```python
source venv/bin/activate
```

#### Install all dependencies
```python
pip install -r requirements.txt
```

## Secrets configuration
You will also need to configure all needed secrets to access external APIs. There are two sets of credentials that must be configured to run this application:

#### Google Cloud
1. You will need a json credentials file from [Google Cloud](https://cloud.google.com/) to connect to [Google Sheets](https://sheets.google.com/). This will need to be saved in the [root directory](https://github.com/talfers/garebear/) and must be called `gcp_creds.json`. See this [example file](https://github.com/talfers/garebear/blob/main/gcp_creds.example.json) for more details.

#### Twilio
2. You will need a [Twilio](https://www.twilio.com/) account to send text messages. To set this up go to [twilio.com](https://www.twilio.com). Once you have an account, you will need a `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`. See this [example file](https://github.com/talfers/garebear/blob/main/secrets.example.env) for details.


## Run application
This applicaiton can be run using the main file [app.py](https://github.com/talfers/garebear/blob/main/app.py). To execute this file, run the below command:
```python
python app.py
```