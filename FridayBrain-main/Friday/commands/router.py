from commands.app_control import AppControl
from commands.browser import Browser
from commands.battery import Battery
from commands.time_control import TimeControl


class CommandRouter:
    def __init__(self):
        self.app = AppControl()
        self.browser = Browser()
        self.battery = Battery()
        self.time = TimeControl()

    def handle(self, command):
        handlers = [
            self.app.open_app,
            self.browser.open_website,
            self.battery.get_battery,
            self.time.get_time,
        ]

        for handler in handlers:
            result = handler(command)
            if result:
                return result

        return None