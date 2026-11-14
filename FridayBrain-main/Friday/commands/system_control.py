from datetime import datetime


class SystemControl:

    def get_time(self, command: str):
        command = command.lower().strip()

        if command in [
            "what time is it",
            "time",
            "current time",
            "tell me the time",
        ]:
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."

        return None