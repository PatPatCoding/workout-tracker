import requests
from datetime import datetime
import os

APP_ID = os.environ.get('ENV_APP_ID')
API_KEY = os.environ.get('ENV_API_KEY')
sheety_token = os.environ.get('ENV_TOKEN')

exercises = input("What did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
body = {
    "query": exercises,
    "gender": "female",
    "weight_kg": 62,
    "height_cm": 169,
    "age": 30,
}
endpoint_nutr = 'https://trackapi.nutritionix.com/v2/natural/exercise'

response = requests.post(url=endpoint_nutr, headers=headers, json=body).json()
print(response)

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
endpoint_sheety = os.environ.get('ENV_SHEET_ENDPOINT')
headers_sheety = {
    "Authorization": sheety_token,
}

for activity in response['exercises']:
    body_workout = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": activity['name'].title(),
            "duration": activity['duration_min'],
            "calories": activity["nf_calories"],
        }
    }

    # response = requests.post(url=endpoint_sheety, json=body_workout, headers=headers_sheety)
    # print(response.json())
