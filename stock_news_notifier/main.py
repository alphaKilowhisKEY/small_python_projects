"""
Stock News Alert with SMS using Alpha Vantage API and News API, sent via Twilio

This Python script checks the stock price of a specified company (Tesla Inc in this case) using the Alpha Vantage API. 
If the stock price increased or decreased by 5% between yesterday and the day before yesterday, 
it fetches the latest news related to the company from the News API and sends an SMS alert via Twilio.

Libraries Used:
- requests: for making HTTP requests to APIs
- twilio: for sending SMS alerts

Variables:
- COMPANY_NAME: Name of the company (e.g., "Tesla Inc").
- STOCK: Stock symbol of the company (e.g., "TSLA").
- ALPHA_KEY: API key for accessing the Alpha Vantage API.
- ALPHA_URL: Base URL for the Alpha Vantage API.
- alpha_param: Parameters for the Alpha Vantage API request.
- NEWS_API: URL for the News API.
- NEWS_API_KEY: API key for accessing the News API.
- news_params: Parameters for the News API request.
- TWILIO_SID: Twilio account SID.
- TWILIO_AUTH_TOKEN: Twilio authentication token.
- VIRTUAL_TWILIO_NUMBER: Twilio virtual phone number.
- VERIFIED_NUMBER: Your own phone number verified with Twilio.

Process:
- Make a request to the Alpha Vantage API to fetch daily stock prices for the specified company.
- Calculate the percentage difference between yesterday's and the day before yesterday's closing prices.
- If the percentage difference is 5% or more, set GET_NEWS to True and proceed to fetch news.
- Make a request to the News API to fetch news articles related to the specified company.
- Format the news articles and send them as SMS alerts using Twilio.

Usage:
- Set up environment variables for the Alpha Vantage API key, News API key, Twilio account SID, and Twilio authentication token.
- Replace placeholders for the company name, stock symbol, and other Twilio-related variables with appropriate values.
- Run the script to receive SMS alerts with news articles if there is a significant change in the stock price.
- $ python3 main.py
"""

import requests
from twilio.rest import Client

COMPANY_NAME = "Tesla Inc"
GET_NEWS = False

## API https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK = "TSLA"
ALPHA_KEY = "*************"
ALPHA_URL = "https://www.alphavantage.co/query"

alpha_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK, 
    "apikey" : ALPHA_KEY
}

response = requests.get(ALPHA_URL, params=alpha_param)
tesla_data = response.json()["Time Series (Daily)"]

tesla_prices = list(tesla_data.keys())

yesterday_close = float(tesla_data[tesla_prices[1]]["4. close"])
day_before_yesterday_close = float(tesla_data[tesla_prices[2]]["4. close"])

print("Yesterday's closing price:", yesterday_close)
print("Day before yesterday's closing price:", day_before_yesterday_close)

percentage_difference = (yesterday_close - day_before_yesterday_close) / ((yesterday_close + day_before_yesterday_close) / 2) * 100

# Compare if there is a 5% difference
if abs(percentage_difference) >= 5:
    print("There is a 5% or more difference between yesterday's and the day before yesterday's closing prices.")
    GET_NEWS = True
else:
    print("There is less than a 5% difference between yesterday's and the day before yesterday's closing prices.")

up_down = None
if percentage_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


## API https://newsapi.org
# Get the first 3 news pieces for the COMPANY_NAME. 
NEWS_API = "https://newsapi.org/v2/everything?q=tesla&from=2024-03-13&sortBy=publishedAt&apiKey=API_KEY"
NEWS_API_KEY = ""

news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

## API TWILIO https://www.twilio.com - sending a SMS with news
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"


if GET_NEWS:
    news_response = requests.get(NEWS_API, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )