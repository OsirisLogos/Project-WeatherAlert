import requests
import schedule
import time
from plyer import notification
import os


def get_weather(api_key, lat, lon):
    url_root = 'https://api.openweathermap.org/data/3.0/onecall'
    url_complete = f'{url_root}?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={api_key}'

    for attempt in range(3):  # retry up to 3 times
        try:
            response = requests.get(url_complete)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Error occurred: {e}. Attempt {attempt + 1} of 3.')
            time.sleep(10)  # wait for 10 seconds before the next attempt
        else:
            data = response.json()

            if 'current' in data:
                current = data['current']
                current_temperature = current.get('temp')
                current_weather = current['weather'][0]['description'] if 'weather' in current and current[
                    'weather'] else 'N/A'
                current_humidity = current.get('humidity', 'N/A')
                current_wind_speed = current.get('wind_speed', 'N/A')

                current_temperature_fahrenheit = round((current_temperature - 273.15) * 9 / 5 + 32,
                                                       2) if current_temperature else 'N/A'

                return current_temperature_fahrenheit, current_weather, current_humidity, current_wind_speed
    print('Could not retrieve weather data after 3 attempts.')
    return None, None, None, None


def getting_temperature(api_key, lat, lon):
    temp_fahrenheit, weather, humidity, wind_speed = get_weather(api_key, lat, lon)
    if temp_fahrenheit is not None:
        notification.notify(
            title='Weather Update',
            message=f"Temperature is {temp_fahrenheit}°F. Weather: {weather}. Humidity: {humidity}%. Wind speed: {wind_speed} m/s",
            timeout=10
        )


api_key = os.getenv('OPEN_WEATHER_API_KEY')
lat = 'YOUR_LATITUDE'
lon = 'YOUR_LONGITUDE'

schedule.every().day.at('12:00').do(getting_temperature, api_key, lat, lon)

while True:
    schedule.run_pending()
    time.sleep(60)
