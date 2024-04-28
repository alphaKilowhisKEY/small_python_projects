"""
Rain Alert with SMS by using Open Weather Map API and Twilio REST

This Python script checks the weather forecast using the OpenWeatherMap API and sends an SMS alert via Twilio if rain is expected. 
The script is intended to be run instantly on PythonAnywhere.

Libraries Used:
- os: for accessing environment variables
- requests: for making HTTP requests to the OpenWeatherMap API
- twilio: for sending SMS alerts

Variables:
- OWM_ENDPOINT: OpenWeatherMap API endpoint for weather forecast
- API_KEY: API key for accessing the OpenWeatherMap API
- IS_RAIN: Boolean variable to track if rain is expected
- account_sid: Twilio account SID
- auth_token: Twilio authentication token
- weather_parameters: Parameters for the weather forecast API request, including latitude, longitude, API key, 
    and number of forecasted periods

Process:
- Make a request to the OpenWeatherMap API to fetch the weather forecast data.
- Extract the weather condition IDs from the forecasted periods.
- Check if any weather condition ID indicates rain (less than 700).
- If rain is expected, set IS_RAIN to True and send an SMS alert using Twilio.

Usage:
- Set up environment variables for Twilio's account SID and authentication token.
- Replace the latitude and longitude in the weather_parameters dictionary with the desired location.
- Replace Phone Numbers with actual numbers.
- Run the script on PythonAnywhere to receive rain alerts via SMS: $python3 main.py

Note: Ensure that you have set up Twilio and obtained necessary API keys before running the script.
"""

import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
IS_RAIN = False

YOUR_NUMBER = "***"
NUMBER_TO_SEND = "***"

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")

weather_parameters = {
    "lat" : 47.257849,
    "lon" : 11.351306,
    "appid" : API_KEY,
    "cnt" : 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()

weather_data = response.json()

weather_ids = [item['weather'][0]['id'] for item in weather_data['list']]

# Weather IDs less than 700 (6XX: Snow, 5XX: Rain, 3XX: Drizzle, 2XX: Thunderstorm )
if any(id < 700 for id in weather_ids):
    IS_RAIN = True
    print("It is raining indeed.")

if IS_RAIN:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
                    .create(
                        body="It's going to rain today. Take an umbrella.",
                        from_= YOUR_NUMBER,
                        to= NUMBER_TO_SEND
                    )

print(message.sid)