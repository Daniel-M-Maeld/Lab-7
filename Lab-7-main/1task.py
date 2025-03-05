import json
import requests

city_name = "Fulda"
key = "921eeafea746d0ece9dfd756369061ca"
respones = requests.post(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}")
result = json.loads(respones.text)
print("погода:", result['weather'][0]['main'])
print("влажность:", result['main']['humidity'])
print("давление:", result['main']['pressure'])
