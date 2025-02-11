# Vanquish's Password Generator 🔐

A fast, secure, and convenient password generator that creates random, strong passwords at the press of a keyboard shortcut. This tool uses `Ctrl+Shift+X` to generate a password, copies it to the clipboard, and sends a notification to let you know it's ready for use. Perfect for enhancing your security workflow!

---

## Features ✨
- **Password Generation**: Generates strong, random passwords using a combination of letters (both uppercase and lowercase), digits, and special characters. 🔑
- **Clipboard Copy**: Automatically copies the generated password to your clipboard for easy use. 📋
- **Notifications**: Displays a notification with the generated password for better user experience. 🔔
- **Hotkey Activation**: Trigger the password generation process using the convenient keyboard shortcut `Ctrl+Shift+X`. ⌨️

---

## Installation 📦

To get started, follow these simple steps to clone and install the necessary libraries:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/boycotted/Vanquish-Password-Generator.git
    cd Vanquish-Password-Generator
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Requirements 📝
Make sure you have the following libraries installed:
- `keyboard`: Used for listening to keyboard events to trigger the password generation hotkey. ⌨️
- `pyperclip`: Automatically copies the generated password to the clipboard. 📋
- `win10toast`: Displays a toast notification when a password is generated. 🎉
- `secrets`: Used to securely generate random passwords. 🔒

To install the dependencies, run:
```bash
pip install keyboard pyperclip win10toast
```

Heres a video preview

https://cdn.discordapp.com/attachments/1338834942515482746/1338863997985882234/password_gen.mp4?ex=67aca1c4&is=67ab5044&hm=255e9b608604b5ba60bc74417d358e02906d0aeafaa5d40857f8ee4427cfaae2&
