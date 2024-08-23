import requests

# API configuration
API_KEY = '2f3d6b727dc8d107efb602c011a23439'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'  # Use 'imperial' for Fahrenheit

# Function to get weather data
def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching weather data for {city}.")
        return None

# Function to determine if the plants should be watered
def should_water_plant(weather_data, temp_threshold, humidity_threshold, wind_threshold):
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    rain = weather_data.get('rain', {}).get('1h', 0)

    print(f"\nCurrent weather conditions:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Rainfall: {rain} mm (last 1 hour)\n")

    if temp > temp_threshold or humidity < humidity_threshold or wind_speed > wind_threshold or rain < 1:
        return True
    else:
        return False

def main():
    city = input("Enter the city name: ")
    temp_threshold = float(input("Enter the temperature threshold in °C (e.g., 30): "))
    humidity_threshold = float(input("Enter the minimum humidity threshold in % (e.g., 30): "))
    wind_threshold = float(input("Enter the maximum wind speed threshold in m/s (e.g., 10): "))

    weather_data = get_weather_data(city)
    if weather_data:
        if should_water_plant(weather_data, temp_threshold, humidity_threshold, wind_threshold):
            print("The weather is hot, dry, or windy. Watering the plants!")
        else:
            print("The weather is fine. No need to water the plants right now.")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
