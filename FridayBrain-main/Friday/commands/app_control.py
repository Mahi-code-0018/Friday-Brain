import subprocess


class AppControl:

    def open_app(self, command: str):
        command = command.lower()

        apps = {
            "chrome": "Google Chrome",
            "google chrome": "Google Chrome",
            "safari": "Safari",
            "terminal": "Terminal",
            "finder": "Finder",
            "calculator": "Calculator",
            "notes": "Notes",
            "calendar": "Calendar",
            "music": "Music",
            "vs code": "Visual Studio Code",
            "visual studio code": "Visual Studio Code",
        }

        for key, app in apps.items():
            if key in command:
                subprocess.run(["open", "-a", app])
                return f"Opening {app}."

        return None