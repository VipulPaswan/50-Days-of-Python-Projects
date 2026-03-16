# Day 13 – Website Blocker using Python 🚫🌐

## 📌 Project Overview

This project is a **Website Blocker Application** built using Python that helps improve productivity by blocking distracting websites during specific working hours.

The program works by modifying the system's **hosts file** and redirecting selected websites to the local machine (`127.0.0.1`). This prevents the browser from accessing those websites while the blocker is active.

It can be useful for students, developers, and professionals who want to avoid distractions during work or study time.

---

## 🚀 Features

- Block distracting websites during work hours
- Automatically allow websites after working hours
- Simple and lightweight script
- Helps improve focus and productivity

---

## 🛠 Technologies Used

- Python 3
- File Handling
- Datetime module

---

## ▶ How It Works

1. The script contains a list of websites to block.
2. During working hours, the program adds those websites to the system **hosts file**.
3. Each website is redirected to `127.0.0.1`, preventing it from opening.
4. After working hours, the script removes the blocked entries from the hosts file.

---

## 📦 Example Blocked Websites
www.facebook.com

www.instagram.com

www.youtube.com

www.twitter.com