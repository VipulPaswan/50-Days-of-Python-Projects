import tkinter as tk
import random

def roll_dice():
    result.config(text=f"🎲 {random.randint(1,6)}")

root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x250")
root.config(bg="#0f172a")

title = tk.Label(
    root,
    text="🎲 Dice Roller",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=20)

result = tk.Label(
    root,
    text="🎲",
    font=("Arial", 50),
    bg="#0f172a",
    fg="#38bdf8"
)
result.pack()

btn = tk.Button(
    root,
    text="Roll Dice",
    command=roll_dice,
    font=("Arial", 14, "bold"),
    bg="#22c55e",
    fg="white",
    width=12
)
btn.pack(pady=20)

root.mainloop()