import webbrowser


class Browser:

    def open_website(self, command: str):
        command = command.lower()
        command = command.strip()

        websites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "gmail": "https://mail.google.com",
            "chatgpt": "https://chat.openai.com",
            "github": "https://github.com",
            "linkedin": "https://linkedin.com",
            "instagram": "https://instagram.com",
            "facebook": "https://facebook.com",
            "twitter": "https://x.com",
        }

        for key, url in websites.items():
            if key in command:
                webbrowser.open_new_tab(url)
                print(f"Opening browser: {url}")
                return f"Opening {key.title()}."

        return None