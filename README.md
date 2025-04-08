# 🔐 Password & Gmail Validation Scripts

This repository contains Python scripts that demonstrate basic input validation techniques through two common tasks:

1. **Password Matching and Validation**
2. **Gmail Address Validation**

Each section introduces increasing levels of complexity, making them suitable for learning how to work with user input, conditionals, and regular expressions in Python.

---

## 📂 Contents

- `password matching (2).py` – Basic password confirmation
- `Password matching (3).py` – Adds minimum length check
- `password matching (4).py` – Enforces strong password criteria
- `validates Gmail addresses.py` – Validates Gmail addresses using regex

---

## 1. 🔑 Password Matching Scripts

### `password matching (2).py`

This is the simplest version of the password matching script. It:

- Prompts the user to enter and confirm a password.
- Checks if the two inputs match.
- Displays a message if they do or don’t.

> No checks for length or password strength are included.

---

### `Password matching (3).py`

This version adds a basic validation rule:

- Password must be at least 8 characters long.
- The script exits early if the password is too short.
- Otherwise, it checks if both inputs match.

---

### `password matching (4).py`

This is a more advanced version that validates password strength based on several rules:

- At least 8 characters long
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (e.g., `@`, `#`, `!`)

The script provides detailed feedback for any missing criteria and verifies that the confirmed password matches the original.

---

## 2. 📧 Gmail Address Validator

### `validates Gmail addresses.py`

This script validates whether the input provided by the user is a correctly formatted **Gmail address**, using regular expressions.

- Accepts emails that match the pattern `username@gmail.com`.
- Ignores case sensitivity.
- Does not check for email existence—only format validation.

---

## ✅ Summary

| Script Name                | Description                         | Validation Type              |
|---------------------------|-------------------------------------|------------------------------|
| `password matching (2).py` | Password match only                 | Basic match                  |
| `Password matching (3).py` | Match + length check                | Min. 8 characters            |
| `password matching (4).py` | Match + full strength validation    | Strong password enforcement  |
| `validates Gmail addresses.py` | Format check for Gmail addresses | Regex-based input validation |

---

## 🚀 How to Run

Run any script using:

```bash
python3 script_name.py
