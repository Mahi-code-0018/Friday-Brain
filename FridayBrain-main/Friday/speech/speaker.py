import subprocess


class Speaker:
    VOICE = "Samantha"
    SPEECH_RATE = 185

    def speak(self, text: str):
        subprocess.run(
            [
                "say",
                "-v",
                self.VOICE,
                "-r",
                str(self.SPEECH_RATE),
                text,
            ],
            check=False,
        )