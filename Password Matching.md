# 🔐 Password Matching Scripts

This document explains three Python scripts that progressively demonstrate how to handle password input and validation using increasingly stronger security checks.

---

## 1. `password matching (2).py`

This is the simplest version of the password matching script. It performs the following steps:

- Prompts the user to enter a password.
- Prompts the user again to re-enter the password for confirmation.
- Compares the two inputs:
  - If the passwords match, it displays a message indicating the match.
  - If they do not match, it notifies the user that the passwords don’t match.

There is no validation of password strength or format—only a basic match check.

---

## 2. `Password matching (3).py`

This version adds a simple validation rule on top of the basic match check:

- The user is asked to enter a password and confirm it.
- Before comparing, the script checks if the password has **at least 8 characters**.
- If the password is too short, it informs the user and ends the process.
- If the length is valid, it checks if both entered passwords match:
  - A success message is shown if they match.
  - An error message is shown if they don’t.

This version is useful for enforcing a minimum length requirement for passwords.

---

## 3. `password matching (4).py`

This version introduces **strong password validation** by enforcing multiple security rules:

- The user is prompted to enter a password and re-enter it for confirmation.
- The password must meet all of the following criteria:
  - At least 8 characters long
  - Contains at least one **uppercase letter**
  - Contains at least one **lowercase letter**
  - Contains at least one **digit**
  - Contains at least one **special character** (such as `@`, `#`, `!`, etc.)
- If any of these conditions are not met, the script provides specific feedback on what is missing.
- After validating the strength of the password, it compares the two entries:
  - If they match, a success message confirms the password is strong and matched.
  - If they do not match, it notifies the user.

This version demonstrates how to build secure password input handling with detailed validation logic.

---

## Summary

| Script Name               | Password Matching | Length Check | Strength Validation |
|--------------------------|-------------------|---------------|----------------------|
| `password matching (2).py` | ✅                 | ❌             | ❌                    |
| `Password matching (3).py` | ✅                 | ✅             | ❌                    |
| `password matching (4).py` | ✅                 | ✅             | ✅                    |

These examples are great for learning about user input, conditionals, and security best practices in Python.
