import tkinter as tk
from tkinter import messagebox
import random

# ---------------- GAME LOGIC ---------------- #

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0


def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "🤝 It's a Tie!"

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        player_score += 1

    else:
        result = "💻 Computer Wins!"
        computer_score += 1

    player_label.config(text=f"👤 You: {player_choice}")
    computer_label.config(text=f"💻 Computer: {computer_choice}")

    result_label.config(text=result)

    score_label.config(
        text=f"🏆 You: {player_score}   |   Computer: {computer_score}"
    )


def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    player_label.config(text="👤 You: -")
    computer_label.config(text="💻 Computer: -")
    result_label.config(text="Choose Rock, Paper or Scissors")

    score_label.config(
        text="🏆 You: 0   |   Computer: 0"
    )


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("✊ Rock Paper Scissors ✂️")
root.geometry("500x500")
root.config(bg="#0f172a")
root.resizable(False, False)

title = tk.Label(
    root,
    text="✊ Rock Paper Scissors ✂️",
    font=("Segoe UI", 20, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=15)

score_label = tk.Label(
    root,
    text="🏆 You: 0   |   Computer: 0",
    font=("Segoe UI", 14, "bold"),
    bg="#0f172a",
    fg="#facc15"
)

score_label.pack(pady=10)

player_label = tk.Label(
    root,
    text="👤 You: -",
    font=("Segoe UI", 14),
    bg="#0f172a",
    fg="white"
)

player_label.pack()

computer_label = tk.Label(
    root,
    text="💻 Computer: -",
    font=("Segoe UI", 14),
    bg="#0f172a",
    fg="white"
)

computer_label.pack(pady=5)

result_label = tk.Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Segoe UI", 14, "bold"),
    bg="#0f172a",
    fg="#22c55e"
)

result_label.pack(pady=20)

# Buttons

btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=20)

rock_btn = tk.Button(
    btn_frame,
    text="🪨 Rock",
    width=12,
    font=("Segoe UI", 12, "bold"),
    bg="#3b82f6",
    fg="white",
    command=lambda: play("Rock")
)

rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    btn_frame,
    text="📄 Paper",
    width=12,
    font=("Segoe UI", 12, "bold"),
    bg="#22c55e",
    fg="white",
    command=lambda: play("Paper")
)

paper_btn.grid(row=0, column=1, padx=10)

scissor_btn = tk.Button(
    btn_frame,
    text="✂️ Scissors",
    width=12,
    font=("Segoe UI", 12, "bold"),
    bg="#ef4444",
    fg="white",
    command=lambda: play("Scissors")
)

scissor_btn.grid(row=0, column=2, padx=10)

reset_btn = tk.Button(
    root,
    text="🔄 Reset Game",
    width=18,
    font=("Segoe UI", 12, "bold"),
    bg="#a855f7",
    fg="white",
    command=reset_game
)

reset_btn.pack(pady=25)

root.mainloop()