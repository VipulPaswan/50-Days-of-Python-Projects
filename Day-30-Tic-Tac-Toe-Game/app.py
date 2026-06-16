import tkinter as tk
from tkinter import messagebox

# ---------------- GAME ---------------- #

board = [""] * 9
current_player = "X"

def check_winner():

    winning_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def button_click(index):

    global current_player

    if board[index] == "":

        board[index] = current_player
        buttons[index].config(
            text=current_player,
            state="disabled"
        )

        winner = check_winner()

        if winner == "X" or winner == "O":

            messagebox.showinfo(
                "Winner",
                f"🎉 Player {winner} Wins!"
            )

            disable_all()

        elif winner == "Draw":

            messagebox.showinfo(
                "Draw",
                "🤝 Match Draw!"
            )

        else:

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

            turn_label.config(
                text=f"Player Turn : {current_player}"
            )


def disable_all():
    for btn in buttons:
        btn.config(state="disabled")


def reset_game():

    global board
    global current_player

    board = [""] * 9
    current_player = "X"

    turn_label.config(
        text="Player Turn : X"
    )

    for btn in buttons:
        btn.config(
            text="",
            state="normal"
        )


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("❌⭕ Tic Tac Toe")
root.geometry("700x700")
root.config(bg="#0f172a")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🎮 Tic Tac Toe",
    font=("Segoe UI", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=15)

turn_label = tk.Label(
    root,
    text="Player Turn : X",
    font=("Segoe UI", 16, "bold"),
    bg="#0f172a",
    fg="white"
)

turn_label.pack(pady=10)

frame = tk.Frame(
    root,
    bg="#0f172a"
)

frame.pack()

buttons = []

for row in range(3):
    for col in range(3):

        index = row * 3 + col

        btn = tk.Button(
    frame,
    text="",
    width=5,
    height=2,
    font=("Arial", 32, "bold"),
    bg="#334155",
    fg="white",
    bd=0,
    activebackground="#38bdf8",
    command=lambda i=index: button_click(i)
)

        btn.grid(
            row=row,
            column=col,
            padx=5,
            pady=5
        )

        buttons.append(btn)

reset_btn = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Segoe UI", 14, "bold"),
    bg="#22c55e",
    fg="white",
    width=18,
    command=reset_game
)

reset_btn.pack(pady=25)

root.mainloop()