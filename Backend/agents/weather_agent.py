class WeatherAgent:

    def get_weather(self, destination):

        weather_data = {
            "Goa": "Sunny",
            "Manali": "Cold",
            "Jaipur": "Warm"
        }

        return weather_data.get(
            destination,
            "Weather information unavailable"
        )