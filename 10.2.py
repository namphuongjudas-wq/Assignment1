import requests

API_KEY = "your_api_key_here"  # Register at https://openweathermap.org/api

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found.")
        return

    description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15  # Convert Kelvin to Celsius

    print(f"Weather: {description}")
    print(f"Temperature: {temp_celsius:.1f}°C")

city = input("Enter city name: ")
get_weather(city)