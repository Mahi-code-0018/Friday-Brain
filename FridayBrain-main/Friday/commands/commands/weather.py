import requests


class Weather:

    def get_weather(self, command: str):
        command = command.lower().strip()

        if "weather" not in command:
            return None

        city = "Hyderabad"  # Change to your city

        try:
            url = f"https://wttr.in/{city}?format=3"
            weather = requests.get(url, timeout=5).text
            return weather
        except Exception:
            return "Sorry Boss, I couldn't get the weather."