import os

def create_env():
    name = input("Enter environment name: ")
    os.system(f"python -m venv {name}")
    print(f"✅ Virtual Environment '{name}' created")

def install_packages():
    pkg = input("Enter package name: ")
    os.system(f"pip install {pkg}")
    print(f"✅ {pkg} installed")

def generate_requirements():
    os.system("pip freeze > requirements.txt")
    print("✅ requirements.txt created")

def show_packages():
    os.system("pip list")

def delete_env():
    name = input("Enter env name to delete: ")
    os.system(f"rmdir /s /q {name}")
    print(f"❌ {name} deleted")

def menu():
    while True:
        print("\n==== ENV MANAGER ====")
        print("1. Create Virtual Env")
        print("2. Install Package")
        print("3. Generate requirements.txt")
        print("4. Show Installed Packages")
        print("5. Delete Environment")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_env()
        elif choice == "2":
            install_packages()
        elif choice == "3":
            generate_requirements()
        elif choice == "4":
            show_packages()
        elif choice == "5":
            delete_env()
        elif choice == "6":
            break
        else:
            print("Invalid choice ❌")

menu()