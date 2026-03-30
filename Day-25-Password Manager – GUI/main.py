from tkinter import *
from tkinter import messagebox
import json
import random
import string
import pyperclip

# -------- Functions -------- #
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(chars, k=12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def save_password():
    website = website_entry.get().lower()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Warning", "Fill all fields")
        return

    new_data = {website: {"username": username, "password": password}}

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except:
        data = {}

    data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo("Saved", "Password saved successfully!")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

def search_password():
    website = website_entry.get().lower()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo("Found", f"User: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Error", "No data found")
    except:
        messagebox.showerror("Error", "No file found")

def copy_password():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copied", "Password copied!")

def toggle_password():
    if password_entry.cget('show') == "*":
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# -------- UI -------- #
root = Tk()
root.title("Password Manager Pro")
root.geometry("500x450")
root.config(bg="#0f172a")  # deep dark

# Main Card Frame
frame = Frame(root, bg="#1e293b", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=380)

# Title
Label(frame, text="🔐 Password Manager",
      font=("Segoe UI", 18, "bold"),
      bg="#1e293b", fg="#38bdf8").pack(pady=15)

# -------- Input Fields -------- #
def create_label(text):
    Label(frame, text=text,
          font=("Segoe UI", 10),
          bg="#1e293b", fg="white").pack(anchor="w", padx=30, pady=(10, 2))

def create_entry():
    return Entry(frame, font=("Segoe UI", 11), bd=0, bg="#334155", fg="white",
                 insertbackground="white")

# Website
create_label("Website")
website_entry = create_entry()
website_entry.pack(fill="x", padx=30, ipady=6)

# Username
create_label("Email / Username")
username_entry = create_entry()
username_entry.pack(fill="x", padx=30, ipady=6)

# Password
create_label("Password")
pass_frame = Frame(frame, bg="#1e293b")
pass_frame.pack(fill="x", padx=30)

password_entry = Entry(pass_frame, font=("Segoe UI", 11), bd=0,
                       bg="#334155", fg="white", show="*",
                       insertbackground="white")
password_entry.pack(side="left", fill="x", expand=True, ipady=6)

Button(pass_frame, text="👁", bg="#334155", fg="white",
       bd=0, command=toggle_password).pack(side="right", padx=5)

# -------- Buttons -------- #
btn_frame = Frame(frame, bg="#1e293b")
btn_frame.pack(pady=20)

Button(btn_frame, text="Generate", width=12,
       bg="#22c55e", fg="white", bd=0,
       command=generate_password).grid(row=0, column=0, padx=5, pady=5)

Button(btn_frame, text="Copy", width=12,
       bg="#3b82f6", fg="white", bd=0,
       command=copy_password).grid(row=0, column=1, padx=5, pady=5)

Button(btn_frame, text="Search", width=12,
       bg="#f59e0b", fg="white", bd=0,
       command=search_password).grid(row=1, column=0, padx=5, pady=5)

Button(btn_frame, text="Save", width=12,
       bg="#a855f7", fg="white", bd=0,
       command=save_password).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()