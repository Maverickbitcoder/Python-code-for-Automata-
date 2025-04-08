# Gmail Address Validator 📨

This is a simple Python script that validates Gmail email addresses using regular expressions. It checks whether a given input is a correctly formatted Gmail address (e.g., `example@gmail.com`).

---

## 📌 Features

- Validates Gmail addresses using a regex pattern
- Ensures correct email structure and domain
- Simple command-line interface

---

## 🧠 How It Works

The script uses Python's built-in `re` module (Regular Expressions) to match the email address format:

- Starts with one or more **alphanumeric characters** (including dots and underscores)
- Followed by `@gmail.com`
- Case-insensitive match

Example of valid emails:
- `example@gmail.com`
- `user.name123@gmail.com`
- `username_1@gmail.com`
---

## 🛠️ Requirements

- Python 3.x

No additional libraries are needed.

---

## 🚀 How to Run

1. Clone or download this script:

   ```bash
   git clone https://github.com/your-username/gmail-validator.git
   cd gmail-validator
