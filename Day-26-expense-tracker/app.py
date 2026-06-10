import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# ---------------- Database Setup ---------------- #
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    type TEXT NOT NULL,
    date TEXT NOT NULL
)
""")
conn.commit()

# ---------------- Functions ---------------- #
def add_transaction():
    title = title_entry.get().strip()
    amount = amount_entry.get().strip()
    category = category_entry.get().strip()
    trans_type = type_var.get()

    if not title or not amount or not category:
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO expenses (title, amount, category, type, date)
        VALUES (?, ?, ?, ?, ?)
    """, (title, amount, category, trans_type, date))
    conn.commit()

    messagebox.showinfo("Success", "Transaction added successfully!")
    clear_fields()
    load_data()
    update_summary()

def load_data():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM expenses ORDER BY id DESC")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

def delete_transaction():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a record to delete")
        return

    values = tree.item(selected, "values")
    record_id = values[0]

    cursor.execute("DELETE FROM expenses WHERE id=?", (record_id,))
    conn.commit()

    messagebox.showinfo("Deleted", "Record deleted successfully!")
    load_data()
    update_summary()

def clear_fields():
    title_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    type_var.set("Expense")

def update_summary():
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE type='Income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE type='Expense'")
    expense = cursor.fetchone()[0] or 0

    balance = income - expense

    income_label.config(text=f"Total Income: ₹{income:.2f}")
    expense_label.config(text=f"Total Expense: ₹{expense:.2f}")
    balance_label.config(text=f"Balance: ₹{balance:.2f}")

# ---------------- UI ---------------- #
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("900x600")
root.config(bg="#0f172a")

title = tk.Label(root, text="Expense Tracker", font=("Segoe UI", 22, "bold"),
                 bg="#0f172a", fg="white")
title.pack(pady=10)

# Top Frame
top_frame = tk.Frame(root, bg="#0f172a")
top_frame.pack(pady=10)

tk.Label(top_frame, text="Title", font=("Segoe UI", 11),
         bg="#0f172a", fg="white").grid(row=0, column=0, padx=10, pady=5)
title_entry = tk.Entry(top_frame, font=("Segoe UI", 11), width=20)
title_entry.grid(row=1, column=0, padx=10, pady=5)

tk.Label(top_frame, text="Amount", font=("Segoe UI", 11),
         bg="#0f172a", fg="white").grid(row=0, column=1, padx=10, pady=5)
amount_entry = tk.Entry(top_frame, font=("Segoe UI", 11), width=20)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(top_frame, text="Category", font=("Segoe UI", 11),
         bg="#0f172a", fg="white").grid(row=0, column=2, padx=10, pady=5)
category_entry = tk.Entry(top_frame, font=("Segoe UI", 11), width=20)
category_entry.grid(row=1, column=2, padx=10, pady=5)

tk.Label(top_frame, text="Type", font=("Segoe UI", 11),
         bg="#0f172a", fg="white").grid(row=0, column=3, padx=10, pady=5)

type_var = tk.StringVar(value="Expense")
type_combo = ttk.Combobox(top_frame, textvariable=type_var, values=["Expense", "Income"], width=18, state="readonly")
type_combo.grid(row=1, column=3, padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Transaction", command=add_transaction,
          font=("Segoe UI", 11, "bold"), bg="#22c55e", fg="white",
          width=16, bd=0).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Delete Selected", command=delete_transaction,
          font=("Segoe UI", 11, "bold"), bg="#ef4444", fg="white",
          width=16, bd=0).grid(row=0, column=1, padx=10)

tk.Button(btn_frame, text="Clear Fields", command=clear_fields,
          font=("Segoe UI", 11, "bold"), bg="#3b82f6", fg="white",
          width=16, bd=0).grid(row=0, column=2, padx=10)

# Summary Frame
summary_frame = tk.Frame(root, bg="#1e293b")
summary_frame.pack(fill="x", padx=20, pady=10)

income_label = tk.Label(summary_frame, text="Total Income: ₹0.00",
                        font=("Segoe UI", 12, "bold"), bg="#1e293b", fg="#22c55e")
income_label.pack(side="left", padx=20, pady=10)

expense_label = tk.Label(summary_frame, text="Total Expense: ₹0.00",
                         font=("Segoe UI", 12, "bold"), bg="#1e293b", fg="#ef4444")
expense_label.pack(side="left", padx=20, pady=10)

balance_label = tk.Label(summary_frame, text="Balance: ₹0.00",
                         font=("Segoe UI", 12, "bold"), bg="#1e293b", fg="#38bdf8")
balance_label.pack(side="left", padx=20, pady=10)

# Table
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = ("ID", "Title", "Amount", "Category", "Type", "Date")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=120)

tree.column("ID", width=60)
tree.column("Date", width=180)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

load_data()
update_summary()

root.mainloop()

conn.close()