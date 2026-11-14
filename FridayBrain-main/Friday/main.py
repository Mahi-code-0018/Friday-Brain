from ai.brain import Brain
from speech.speaker import Speaker
from speech.listener import Listener
from speech.wake_word import WakeWord
from commands.app_control import AppControl
from commands.browser import Browser


def main():
    brain = Brain()
    speaker = Speaker()
    listener = Listener()
    wake_word = WakeWord()
    app_control = AppControl()
    browser = Browser()

    print("Friday is ready.")

    while True:
        wake_text = listener.listen()

        if not wake_text:
            continue

        if not wake_word.detect(wake_text):
            continue

        speaker.speak("Yes Boss?")

        question = listener.listen()

        if not question:
            continue

        if question.lower() in ["exit", "quit", "bye"]:
            print("\nFriday: Goodbye Boss!")
            speaker.speak("Goodbye Boss!")
            break

        app_result = app_control.open_app(question)
        if app_result:
            print(f"\nFriday: {app_result}")
            speaker.speak(app_result)
            continue

        browser_result = browser.open_website(question)
        if browser_result:
            print(f"\nFriday: {browser_result}")
            speaker.speak(browser_result)
            continue

        answer = brain.ask(question)
        print(f"\nFriday: {answer}")
        speaker.speak(answer)


if __name__ == "__main__":
    main()