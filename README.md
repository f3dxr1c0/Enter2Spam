# Enter2Spam

A simple Python tool that spams a message in any chat by simulating keyboard input with `pyautogui`.

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

---

## ⚠️ Disclaimer

This tool is intended **for educational purposes only**.

- The author is **not responsible** for any misuse or consequences.
- Use it only in chats you own, or with people who explicitly consent.

By using this program you accept full responsibility for your actions.

---

## 📋 Requirements

- Python **3.8+**
- Windows (uses `cls` and `os.system("title Enter2Spam")`)
- The following Python packages:

```
pystyle
colorama
pyautogui
```

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/f3dxr1c0/Enter2Spam.git
cd Enter2Spam
```

2. **Install the dependencies**

```bash
pip install pystyle colorama pyautogui
```

Or,

```bash
pip install -r requirements.txt
```

3. **Run the script**

```bash
python main.py
```

---

## 🖥️ Usage

When you launch the program, you'll see a menu:

```
    [1] Messages to spam
    [2] Help
    [3] Exit
```

### [1] Messages to spam

1. Select option **1**
2. Enter the **message** you want to send
3. Enter **how many times** you want to send it
4. You have **5 seconds** to click on the chat where you want to send the message
5. The program will start sending the messages automatically

> 💡 Tip: if you need to stop the spam, press **ESC** or close the terminal.

### [2] Help

Shows a help screen with the available options and instructions.

### [3] Exit

Closes the program.

---

## 📁 Project structure

```
Enter2Spam/
├── main.py           # Main script
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## 🛠️ How it works

The script uses [`pyautogui`](https://pyautogui.readthedocs.io/) to:

1. Write the message with `pg.write(msg)`
2. Press `Enter` with `pg.press('enter')`
3. Repeat for the number of times you specified

The UI is built with [`pystyle`](https://github.com/billythegoat356/pystyle) and [`colorama`](https://pypi.org/project/colorama/) for colored and centered text.

## ⭐ Show your support
If you found this project useful, give it a ⭐.
