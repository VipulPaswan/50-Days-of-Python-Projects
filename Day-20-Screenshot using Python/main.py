import pyautogui
from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Screenshot function
def take_ss():
    filename = entry.get()

    if filename == "":
        # Default name with timestamp
        filename = "screenshot_" + datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        ss = pyautogui.screenshot()
        ss.save(filename + ".png")
        messagebox.showinfo("Success", f"Screenshot saved as {filename}.png")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main Window
win = Tk()
win.title("📸 Screenshot App")
win.geometry("500x400")
win.config(bg="#1e1e2f")
win.resizable(False, False)

# Title Label
title = Label(win, text="Screenshot Tool", 
              font=("Poppins", 24, "bold"), 
              bg="#1e1e2f", fg="white")
title.pack(pady=20)

# Entry Label
label = Label(win, text="Enter File Name:", 
              font=("Arial", 14), 
              bg="#1e1e2f", fg="white")
label.pack(pady=5)

# Entry Box
entry = Entry(win, font=("Arial", 16), bd=3, relief=FLAT, justify="center")
entry.pack(pady=10, ipadx=10, ipady=5)

# Button
button = Button(win, text="📸 Take Screenshot",
                font=("Arial", 16, "bold"),
                bg="#4CAF50", fg="white",
                activebackground="#45a049",
                cursor="hand2",
                command=take_ss)
button.pack(pady=20, ipadx=10, ipady=5)

# Exit Button
exit_btn = Button(win, text="❌ Exit",
                  font=("Arial", 12),
                  bg="#ff4d4d", fg="white",
                  command=win.quit)
exit_btn.pack(pady=10)

win.mainloop()