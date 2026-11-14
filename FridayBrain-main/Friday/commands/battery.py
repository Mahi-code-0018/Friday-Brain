import psutil


class Battery:

    def get_battery(self, command: str):
        command = command.lower().strip()

        if any(word in command for word in [
            "battery",
            "battery percentage",
            "battery status",
            "charge",
        ]):
            battery = psutil.sensors_battery()

            if battery is None:
                return "Sorry Boss, I couldn't detect the battery."

            return f"Your battery is at {battery.percent:.0f} percent."

        return None