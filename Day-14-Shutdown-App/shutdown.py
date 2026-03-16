from tkinter import *
from tkinter import messagebox
import os

# -------- Functions --------

def restart():
    confirm = messagebox.askyesno("Restart", "Are you sure you want to Restart?")
    if confirm:
        os.system("shutdown /r /t 1")


def shutdown():
    confirm = messagebox.askyesno("Shutdown", "Are you sure you want to Shutdown?")
    if confirm:
        os.system("shutdown /s /t 1")


def logout():
    confirm = messagebox.askyesno("Logout", "Are you sure you want to Logout?")
    if confirm:
        os.system("shutdown -l")


def restart_time():
    confirm = messagebox.askyesno("Restart Timer", "Restart after 1 minute?")
    if confirm:
        os.system("shutdown /r /t 60")


# -------- Window --------

st = Tk()
st.title("System Control App")
st.geometry("500x500")
st.config(bg="#1e1e2f")

# -------- Title --------

title = Label(
    st,
    text="System Control Panel",
    font=("Times New Roman", 28, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=30)

# -------- Buttons --------
btn_style = {
    "font": ("Times New Roman", 16, "bold"),
    "width": 18,
    "height": 2,
    "bd": 3,
    "cursor": "hand2"
}

restart_btn = Button(st, text="Restart", bg="#00c853", fg="white",
                     command=restart, **btn_style)
restart_btn.pack(pady=10)

restart_timer_btn = Button(st, text="Restart in 1 Min", bg="#2962ff", fg="white",
                           command=restart_time, **btn_style)
restart_timer_btn.pack(pady=10)

logout_btn = Button(st, text="Log Out", bg="#ff9100", fg="white",
                    command=logout, **btn_style)
logout_btn.pack(pady=10)

shutdown_btn = Button(st, text="Shutdown", bg="#d50000", fg="white",
                      command=shutdown, **btn_style)
shutdown_btn.pack(pady=10)

# -------- Run --------

st.mainloop()