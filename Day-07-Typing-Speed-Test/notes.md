# Day 7 – Typing Speed Test using Python ⌨️

## 📌 Project Overview
This project measures a user's typing speed and accuracy.  
The user is given a sentence to type, and the program calculates the time taken and the typing speed in **words per minute (WPM)**.

Typing speed tests are commonly used to evaluate typing performance and improve keyboard skills.

---

## 🚀 Features

- Random sentence for typing practice
- Calculates typing time
- Measures typing speed (WPM)
- Shows accuracy of typed text

---

## 🛠 Technologies Used

- Python 3
- time module
- random module

---

## ▶ Python Code

```python
import time
import random

sentences = [
    "Python is a powerful programming language",
    "Practice makes perfect",
    "Typing speed improves with daily practice",
    "Artificial intelligence is the future",
]

sentence = random.choice(sentences)

print("Type the following sentence:")
print(sentence)

input("Press Enter when you are ready...")

start_time = time.time()

typed_text = input("\nStart typing: ")

end_time = time.time()

time_taken = end_time - start_time

words = len(typed_text.split())

speed = words / (time_taken / 60)

print("\nTime Taken:", round(time_taken, 2), "seconds")
print("Typing Speed:", round(speed, 2), "words per minute")

if typed_text == sentence:
    print("Accuracy: 100%")
else:
    print("Accuracy: Needs Improvement")

    