import tkinter as tk
from tkinter import messagebox
import random

# ---------------- WORDS ---------------- #

words = [
    "PYTHON",
    "PROGRAM",
    "DEVELOPER",
    "COMPUTER",
    "KEYBOARD",
    "CHALLENGE",
    "GITHUB",
    "CODING",
    "HANGMAN",
    "DATABASE"
]

# ---------------- GAME ---------------- #

def new_game():
    global word, guessed_letters, wrong_guesses

    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0

    lives_label.config(text="❤️ Lives: 6")
    update_word()

    for btn in buttons.values():
        btn.config(state="normal")


def update_word():
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    word_label.config(text=display)

    if "_" not in display:
        disable_buttons()
        messagebox.showinfo(
            "Congratulations",
            "🎉 You Won!"
        )


def disable_buttons():
    for btn in buttons.values():
        btn.config(state="disabled")


def guess(letter):
    global wrong_guesses

    buttons[letter].config(state="disabled")

    if letter in word:
        guessed_letters.append(letter)
        update_word()

    else:
        wrong_guesses += 1

        lives_label.config(
            text=f"❤️ Lives: {6 - wrong_guesses}"
        )

        if wrong_guesses == 6:
            disable_buttons()

            messagebox.showerror(
                "Game Over",
                f"💀 You Lost!\n\nWord was: {word}"
            )


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("🎮 Hangman Game")
root.geometry("700x780")
root.config(bg="#0f172a")
root.resizable(False, False)

# Title

title = tk.Label(
    root,
    text="🎮 Hangman Game",
    font=("Segoe UI", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=15)

# Word Display

word_label = tk.Label(
    root,
    text="",
    font=("Consolas", 30, "bold"),
    bg="#0f172a",
    fg="white"
)

word_label.pack(pady=20)

# Lives

lives_label = tk.Label(
    root,
    text="❤️ Lives: 6",
    font=("Segoe UI", 16, "bold"),
    bg="#0f172a",
    fg="#22c55e"
)

lives_label.pack(pady=10)

# ---------------- POSSIBLE WORDS ---------------- #

words_frame = tk.Frame(
    root,
    bg="#1e293b",
    bd=3,
    relief="ridge"
)

words_frame.pack(pady=15)

words_title = tk.Label(
    words_frame,
    text="📋 POSSIBLE WORDS",
    font=("Segoe UI", 16, "bold"),
    bg="#1e293b",
    fg="#facc15"
)

words_title.pack(pady=(10, 5))

words_label = tk.Label(
    words_frame,
    text="• " + "\n• ".join(words),
    font=("Consolas", 13, "bold"),
    bg="#1e293b",
    fg="white",
    justify="left",
    padx=35,
    pady=15
)

words_label.pack()

# ---------------- KEYBOARD ---------------- #

frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=20)

buttons = {}

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

row = 0
col = 0

for letter in alphabet:

    btn = tk.Button(
        frame,
        text=letter,
        width=4,
        height=2,
        font=("Arial", 10, "bold"),
        bg="#334155",
        fg="white",
        activebackground="#38bdf8",
        activeforeground="black",
        command=lambda l=letter: guess(l)
    )

    btn.grid(
        row=row,
        column=col,
        padx=3,
        pady=3
    )

    buttons[letter] = btn

    col += 1

    if col == 7:
        row += 1
        col = 0

# ---------------- NEW GAME BUTTON ---------------- #

restart_btn = tk.Button(
    root,
    text="🔄 New Game",
    font=("Segoe UI", 14, "bold"),
    bg="#22c55e",
    fg="white",
    width=15,
    command=new_game
)

restart_btn.pack(pady=20)

# Start Game

new_game()

root.mainloop()

