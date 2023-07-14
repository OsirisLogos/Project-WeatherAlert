Weather Notifier

This Python script fetches the current weather data for a specified location using the OpenWeatherMap API and sends a desktop notification with the weather details.
Features

    Retrieves current weather data including temperature, weather description, humidity, and wind speed.
    Sends a desktop notification with weather data every day at a specified time.
    Implements error handling and retry mechanism for API requests.

How to Use

    Clone this repository: git clone <repository-url>
    Install the required Python packages: pip install -r requirements.txt
    Get an API key from OpenWeatherMap and set it as an environment variable named OPEN_WEATHER_API_KEY.
    Set your latitude and longitude in the main script.
    Run the script: python main.py
    The script will run continuously and send a weather notification every day at the specified time.

Dependencies

    requests: To make HTTP requests to the OpenWeatherMap API.
    schedule: To schedule the weather notification at the specified time.
    plyer: To display desktop notifications.

Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
License

This project is licensed under the MIT License.
