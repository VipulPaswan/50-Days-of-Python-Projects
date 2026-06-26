import tkinter as tk
import random

colors = ["Red", "Blue", "Green", "Yellow", "Pink", "Orange", "Purple", "Brown"]

score = 0
time_left = 30


def start_game(event=None):
    if time_left == 30:
        countdown()

    next_color()


def next_color():
    global score

    if time_left > 0:

        e.focus_set()

        if e.get().lower() == colors[1].lower():
            score += 1

        e.delete(0, tk.END)

        random.shuffle(colors)

        label.config(fg=colors[1], text=colors[0])

        score_label.config(text="Score: " + str(score))


def countdown():
    global time_left

    if time_left > 0:

        time_left -= 1

        time_label.config(text="Time Left: " + str(time_left))

        root.after(1000, countdown)


root = tk.Tk()
root.title("Color Guessing Game")
root.geometry("500x350")
root.config(bg="#0f172a")

tk.Label(
    root,
    text="Type the COLOR of the text",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="white"
).pack(pady=10)

score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 14),
    bg="#0f172a",
    fg="#22c55e"
)

score_label.pack()

time_label = tk.Label(
    root,
    text="Time Left: 30",
    font=("Arial", 14),
    bg="#0f172a",
    fg="#ef4444"
)

time_label.pack()

label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    bg="#0f172a"
)

label.pack(pady=20)

e = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center"
)

e.pack()

root.bind("<Return>", start_game)

tk.Label(
    root,
    text="Press ENTER to Start",
    font=("Arial", 12),
    bg="#0f172a",
    fg="white"
).pack(pady=20)

root.mainloop()