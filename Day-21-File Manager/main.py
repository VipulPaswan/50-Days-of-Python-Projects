import os
import shutil

path = input("Enter Your Path: ")

files = os.listdir(path)

for i in files:
    file_path = os.path.join(path, i)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    filename, extension = os.path.splitext(i)

    # Handle files without extension
    if extension == "":
        folder_name = "no_extension"
    else:
        folder_name = extension[1:]

    folder_path = os.path.join(path, folder_name)

    # Create folder if not exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Move file
    shutil.move(file_path, os.path.join(folder_path, i))

print("✅ Files organized successfully!")