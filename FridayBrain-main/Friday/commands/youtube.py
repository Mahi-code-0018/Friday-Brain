import webbrowser
from urllib.parse import quote_plus


class YouTube:

    def search(self, command: str):
        command = command.lower().strip()

        trigger = "search youtube for"

        if command.startswith(trigger):
            query = command.replace(trigger, "", 1).strip()

            if not query:
                return None

            url = (
                f"https://www.youtube.com/results?search_query="
                f"{quote_plus(query)}"
            )

            webbrowser.open_new_tab(url)

            return f"Searching YouTube for {query}."

        return None