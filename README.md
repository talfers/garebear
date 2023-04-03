# Permit Crawler
Application used to crawl [recreation.gov](https://www.recreation.gov/) permit availability webpages and alert when desired permits are available during time periods specified in [this Google Sheet](https://docs.google.com/spreadsheets/d/1Fv0ut4FTRywssG2naRxMQmxX5Ax-7MCqU7PuDiO4hy8/edit?usp=sharing).


## Environment setup
In order to run and develop this application, you will need to create a virtual environment and install all necessary dependencies. To do this run the below commands:


#### Create your virtual env
```shell
python3 -m venv venv
```

#### Activate your virtual env
```shell
source venv/bin/activate
```

#### Install all dependencies
```shell
pip install -r requirements.txt
```

## Secrets configuration
You will also need to configure all needed secrets to access external APIs. There are two sets of credentials that must be configured to run this application:

#### Google Cloud
1. You will need a json credentials file from [Google Cloud](https://cloud.google.com/) to connect to [Google Sheets](https://sheets.google.com/). This will need to be saved in the [root directory](https://github.com/talfers/garebear/) and must be called `gcp_creds.json`. See this [example file](https://github.com/talfers/garebear/blob/main/gcp_creds.example.json) for more details.

#### Twilio
2. You will need a [Twilio](https://www.twilio.com/) account to send text messages. To set this up go to [twilio.com](https://www.twilio.com). Once you have an account, you must copy your `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` into the a file called `secrets.env`. See this [example file](https://github.com/talfers/garebear/blob/main/secrets.example.env) for details.


## Run application
Once all the above configuration is complete, you can run this applicaiton using the main file: [app.py](https://github.com/talfers/garebear/blob/main/app.py). To execute this file, run the below command:
```shell
python app.py
```