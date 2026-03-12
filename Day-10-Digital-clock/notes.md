# Day 10 – Digital Clock using Python ⏰

## 📌 Project Overview

This project is a simple **Digital Clock Application** built using Python.  
The clock displays the current system time and updates automatically every second.

The application uses the Tkinter library to create a graphical user interface and the time module to retrieve the current time.

---

## 🚀 Features

- Real-time digital clock
- Updates every second
- Simple GUI interface
- Displays hours, minutes, and seconds

---

## 🛠 Technologies Used

- Python 3
- Tkinter (GUI)
- time module

---

## ▶ Python Code

```python
from tkinter import *
import time

root = Tk()
root.title("Digital Clock")

def clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, clock)

label = Label(root, font=("Arial", 60), bg="black", fg="cyan")
label.pack(anchor="center")

clock()

root.mainloop()