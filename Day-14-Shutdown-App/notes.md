# Day 14 – Shutdown & Restart Laptop using Python 💻⚡

## 📌 Project Overview

This project demonstrates how to **shutdown or restart a computer using Python commands**.

The script uses Python's `os` module to execute system-level commands that control the power state of the computer.

This type of automation can be useful for:
- Automating system maintenance
- Scheduling shutdown tasks
- Managing system operations programmatically

---

## 🚀 Features

- Shutdown the computer using Python
- Restart the computer using Python
- Simple command-based automation
- Uses system commands through Python

---

## 🛠 Technologies Used

- Python 3
- OS module
- System commands

---

## ▶ Python Code Example

```python
import os

# Shutdown computer
os.system("shutdown /s /t 1")

# Restart computer
os.system("shutdown /r /t 1")