import random
import string
import secrets
import keyboard
import pyperclip
from win10toast import ToastNotifier

# Send notifications when a password is generated

notification = ToastNotifier()

# the actual generator

active = True
def create_password(length=15):
    dictionary = string.ascii_letters + string.punctuation + string.digits

    length = max(length, 15)

    password = ''.join(secrets.choice(dictionary) for x in range(length))

    return password

# shortcut to generate the password

def on_shortcut():
    password = create_password()
    pyperclip.copy(password)
    print(f'generated password: {password}')
    notification.show_toast(f'generated password : {password}', 'vanquishs password generator')




keyboard.add_hotkey('ctrl+shift+x', on_shortcut)

keyboard.wait()
