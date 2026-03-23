# Day 21 – File Manager App using Python 📂

## 📌 Project Overview

This project is a simple file manager that automatically organizes files in a directory based on their file extensions.

It scans a folder and moves files into categorized subfolders, making file management easier and more efficient.

---

## 🚀 Features

- Organizes files by extension
- Automatically creates folders
- Handles files without extension
- Improves folder structure

---

## 🛠 Technologies Used

- Python 3
- os module
- shutil module

---

## ▶ Python Code

```python
import os
import shutil

path = input("Enter Your Path: ")

files = os.listdir(path)

for i in files:
    file_path = os.path.join(path, i)

    if os.path.isdir(file_path):
        continue

    filename, extension = os.path.splitext(i)

    if extension == "":
        folder_name = "no_extension"
    else:
        folder_name = extension[1:]

    folder_path = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(file_path, os.path.join(folder_path, i))

print("Files organized successfully!")