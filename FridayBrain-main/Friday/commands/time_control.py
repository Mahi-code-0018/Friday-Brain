from datetime import datetime


class TimeControl:

    def get_time(self, command: str):
        command = command.lower().strip()

        triggers = [
            "time",
            "what time is it",
            "current time",
            "tell me the time",
        ]

        if any(trigger in command for trigger in triggers):
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."

        return None