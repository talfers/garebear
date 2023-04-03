# Permit Crawler
Application used to crawl recreation.gov permit availability webpages and alert when specified permits are available during desired time periods.

## Working branch
[Parser](https://github.com/talfers/garebear/tree/parser)

## Current updates
Adding methods in [parser.py](https://github.com/talfers/garebear/blob/main/classes/parser.py) to parse availability data structures.

## Env setup
You will need 2 sets of credentials to run this application. 

First you will need a google cloud credentials json file to connect to google sheets. This will need to be saved in the [main project directory](https://github.com/talfers/garebear/) and must be called `gcp_creds.json`. See this [example file](https://github.com/talfers/garebear/blob/main/gcp_creds.example.json) for details.

Next you will need a twilio account and phone number. To set this up go to [Twilio](htts://www.twilio.com). You will need a TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER. See this [example file](https://github.com/talfers/garebear/blob/main/secrets.example.env) for details.


## Development
We use Makefiles to run local environment setup. The following command will setup your virutal environment, load your dependencies and get your machine ready for development:
```shell
make
```

## Run application
Currently the application is run using:
```shell
python app.py
```