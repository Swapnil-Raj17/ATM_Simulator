# 🏦 ATM Simulation in Python (OOP Learning Project)

This project is a basic ATM simulation developed to learn and apply Object-Oriented Programming (OOP) principles using Python. It allows users to set a PIN, check balance, deposit and withdraw funds, and view a transaction history — all through a console-based interface.

---

## 🎯 Purpose

This code was developed during my learning phase of Python’s OOP features. Through this project, I gained:

- A deeper understanding of **classes and objects**
- Practical use of **dunder methods** (like `__init__`)
- Insights into **encapsulation**, **method design**, and **object lifecycle**
- A real-world view of how OOP structures help simulate complex systems like banking

---

## 🚀 Features

- 🔐 Secure PIN setup and validation
- 💰 Balance inquiry (PIN-protected)
- 📥 Deposit and 📤 Withdraw functions
- 🧾 Transaction history log
- 🔁 Loop-driven command-line interface

---

## 🧠 OOP Concepts Demonstrated

| Concept         | How It’s Used in the Code                                |
|----------------|-----------------------------------------------------------|
| **Class**       | `atm` class encapsulates balance, PIN, and operations    |
| **Object**      | Created via `user = atm()` to simulate ATM usage         |
| **Dunder method** | `__init__()` initializes state and runs the menu        |
| **Encapsulation** | Sensitive data like `pin` and `balance` are private to class |
| **Modularity**  | Each operation is handled by a dedicated method (`deposit()`, etc.) |

```python
def withdraw(self):
    temp = input("Enter your pin: ")
    if temp == self.pin:
        ...
