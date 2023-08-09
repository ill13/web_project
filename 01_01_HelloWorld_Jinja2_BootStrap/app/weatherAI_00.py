def get_weather(zipcode):
    # Import libraries
    import requests
    import json

    # Define variables
    base_url = 'https://api.weather.gov/points/{}/conditions'.format(zipcode)
    response = None

    # Make a GET request to NWS API endpoint with zip code as query parameter
    try:
        response = requests.get(base_url, timeout=10)
    except Exception as e:
        print('Error: {}'.format(e))

    # Decode the JSON response and extract weather information
    if response is not None and response.ok:
        print(response)
        data = json.loads(response.text)
        # temperature = data['current_observation']['temperature'][0]['value']
        # humidity = data['current_observation']['relative_humidity'][0]['value']
        # wind_speed = data['current_observation']['wind_speed'][0]['value']

    return
    # Return a dictionary object containing key-value pairs representing the weather conditions
    # return {
    #     'temperature': temperature,
    #     'humidity': humidity,
    #     'wind_speed': wind_speed
    # }


weather_data = get_weather(98122)  # Replace 98122 with your desired zip code
print(weather_data)
# print('Temperature:', weather_data['temperature'])
# print('Humidity:', weather_data['humidity'])
# print('Wind speed:', weather_data['wind_speed'])