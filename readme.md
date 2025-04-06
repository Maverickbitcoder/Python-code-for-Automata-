# DFA Password Validator 🔐

This project implements a **Deterministic Finite Automaton (DFA)** in Python to validate passwords based on specific rules. It simulates state transitions to ensure a password meets the required structure.

## 🔍 Password Validation Rules

The password is **valid** if it satisfies **all** of the following:

1. **Starts** with at least **one uppercase letter** (A–Z)
2. Followed by at least **one lowercase letter** (a–z)
3. Followed by at least **one digit** (0–9)
4. **Ends** with exactly **one special character**: `!`, `@`, or `#`
5. **No characters are allowed** after the special character

## ✅ Example of Valid Passwords

- `Aabc1@`
- `XYZdef3!`
- `Pq1#`

## ❌ Example of Invalid Passwords

- `abc1@` → No uppercase at the start
- `ABCD123!` → No lowercase after uppercase
- `Abc!123` → Characters after special symbol
- `Abc1` → Missing special character

## 📁 Files

- `dfa_password.py` – Main Python script containing the DFA implementation and test logic

## 💻 How to Run

1. Make sure you have Python installed.
2. Run the script in terminal or command prompt:

```bash
python dfa_password.py
```

3. Enter a password when prompted, and it will tell you whether it's valid or not.

## 🚀 Features

- Pure Python implementation
- Simulates DFA state transitions
- Easily extendable to support more complex rules

---

Feel free to contribute or suggest improvements!
