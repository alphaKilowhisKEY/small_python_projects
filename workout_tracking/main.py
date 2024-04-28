"""
Exercise Tracker

This Python script tracks exercises entered by the user using the Nutritionix API and stores the data in a Google Sheets spreadsheet using the Sheety API.

Libraries Used:
- requests: for making HTTP requests
- datetime: for working with dates and times

Global Variables:
- GENDER: Gender of the user
- WEIGHT_KG: Weight of the user in kilograms
- HEIGHT_CM: Height of the user in centimeters
- AGE: Age of the user
- APP_ID: Nutritionix application ID
- API_KEY: Nutritionix API key
- URL: Nutritionix API endpoint for exercise tracking
- bearer_headers: Headers for Sheety API authentication
- sheet_endpoint: Sheety API endpoint for accessing the Google Sheets spreadsheet

Methods:
- None

Usage:
- Replace the placeholders (******, *********) with your Nutritionix APP_ID, API_KEY, and Sheety Bearer Token.
- Run the script, which prompts the user to enter the exercises they did: $python3 main.py
- The script then sends the exercise data to the Nutritionix API and retrieves the exercise details.
- It formats the data and sends it to the Google Sheets spreadsheet using the Sheety API.
"""

import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 68
HEIGHT_CM = 168
AGE = 35

APP_ID = "******" 
API_KEY = "*********"

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers =  {
    'x-app-id': APP_ID,
    'x-app-key' : API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=URL, headers=headers, json=parameters)
result = response.json()
#print(result)

#Bearer Token Authentication
bearer_headers = {
"Authorization": "Bearer *************"
}

sheet_endpoint = "https://api.sheety.co/b120b1fd0003fb1f9db422a983dde1de/workout/лист1"


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "лист1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)   


print(sheet_response.text)