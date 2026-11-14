import pyautogui
from datetime import datetime
from pathlib import Path


class Screenshot:

    def take_screenshot(self, command: str):
        command = command.lower().strip()

        triggers = [
            "take screenshot",
            "take a screenshot",
            "capture screen",
            "screenshot",
        ]

        if any(trigger in command for trigger in triggers):
            folder = Path.home() / "Desktop" / "Friday Screenshots"
            folder.mkdir(exist_ok=True)

            filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")

            path = folder / filename

            image = pyautogui.screenshot()
            image.save(path)

            return f"Screenshot saved to {path.name}."

        return None