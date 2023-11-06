<h1 align="center">Google Bard Telegram Bot 🤖</h1>

<p align="center">
  <em>Google Bard is a ‎Chat Based AI Tool from Google, This is a Python Telegram Bot script leveraging the aiogram library to interact with Google Bard through cookie value. This repository contains the core script that facilitates the communication between the user and Bard, </em>
</p>

<hr>

## 🌟 Features

- 🔄 Asynchronous Communication: Leverage the power of async for seamless interactions
- ⚙️ Error Handling: Robust error handling for a smoother user experience
- 🍪 Accepts text prompts and generates text using the Google Bard through cookie value 
- 📲 Provides generated text as a response in Telegram 
- ✍️ Supports the `/start` command for welcoming users 👋 and the `/bard` command for generating text 

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Libraries: `aiogram,` `requests`
- A Telegram bot token.
- `__Secure-1PSID` and `__Secure-1PSIDTS` from bard.google.com. 

### How to get the 1PSID and 1PSIDTS Key

1. **Secure-1PSID Key**:
   - Visit the [Google Bard](https://bard.google.com/).
   - Open Inspect or `CTLR+Shift+I`
   - Go to the : Application → Cookies → Copy the value of `__Secure-1PSID cookie`.
   - Warning Do not expose the `Secure-1PSID`

2. **Secure-1PSIDTS Key**:
   - Visit the [Google Bard](https://bard.google.com/).
   - Open Inspect or `CTLR+Shift+I`
   - Go to the : Application → Cookies → Copy the value of `__Secure-1PSIDTS cookie`.

### Installation

1. Install the required Python packages:

 - This is a framework for Telegram Bot API. You can install it using pip:
   `````
   pip install aiogram==2.6
- This is a popular Python HTTP library. You can install it with pip:
  `````
  pip install requests
2. Update the `bard.py` file with your [Telegram bot token], `V = Secure-1PSID cookie key`, and `W = Secure-1PSIDTS cookie key`

3. Run the Google Bard bot:
  `````
 python bard.py
  `````
## 📚 Usage

1. Start a chat with your bot on Telegram.
2. Ask question to Bard: `/bard <query>`.

## Author

- Name: Bisnu Ray
- Telegram: [@SmartBisnuBio](https://t.me/SmartBisnuBio)

Feel free to reach out if you have any questions or feedback.
