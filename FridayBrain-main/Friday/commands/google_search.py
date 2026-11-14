import webbrowser


class GoogleSearch:

    def search(self, command: str):
        command = command.lower().strip()

        if command == "search google" or command == "open google":
            webbrowser.open_new_tab("https://www.google.com")
            return "Opening Google."

        return None