import ollama
from config import MODEL_NAME


class Brain:
    def __init__(self):
        self.model = MODEL_NAME

    def ask(self, question):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Friday, an intelligent AI assistant. "
                        "Always call the user 'Boss'. "
                        "Be helpful, concise, and friendly."
                    ),
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        return response["message"]["content"]