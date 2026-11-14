class WakeWord:

    WAKE_WORD = "hey friday"

    def detect(self, text: str) -> bool:
        if not text:
            return False

        return self.WAKE_WORD in text.lower()