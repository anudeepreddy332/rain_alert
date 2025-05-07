import requests
from twilio.rest import Client
from config import *
account_sid = my_account_sid
auth_token = owm_auth_token
api_key = my_api_key
my_lat = current_lat
my_long = current_long

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_ENDPOINT,params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(json.dumps(weather_data,indent=4))
will_rain = False
for forcast in weather_data["list"]:
    weather_id = forcast["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It might rain. Bring an umbrella dawg!☔️",
        from_=my_twilio_no,
        to=receivers_mobile_no,
    )
    print(message.status)
