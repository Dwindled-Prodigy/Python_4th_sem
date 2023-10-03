import json

with open('weather_data.json') as f:
    data = json.load(f)

cur_temp = data['main']['temp']
humidity = data['main']['humidity']
weather_description = data['weather'][0]['description']

print(f"Current temp: {cur_temp}°C")
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_description}")
