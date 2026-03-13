from tkinter import *
import speedtest
import threading

def check_speed():
    try:
        st = speedtest.Speedtest()

        status_label.config(text="Checking Download Speed...")

        download_speed = round(st.download() / 10**6, 2)
        download_label.config(text=str(download_speed) + " Mbps")

        status_label.config(text="Checking Upload Speed...")

        upload_speed = round(st.upload() / 10**6, 2)
        upload_label.config(text=str(upload_speed) + " Mbps")

        status_label.config(text="Test Completed")

    except Exception as e:
      print(e)
      status_label.config(text="Error checking speed")

def start_test():
    thread = threading.Thread(target=check_speed)
    thread.start()


root = Tk()
root.title("Internet Speed Tester")
root.geometry("500x600")
root.config(bg="#0A2647")

title = Label(root,text="Internet Speed Test",
              font=("Times New Roman", 28, "bold"),bg="#0A2647",fg="white")
title.pack(pady=30)
download_text = Label(root,text="Download Speed",
                      font=("Times New Roman", 20, "bold"),bg="#0A2647",fg="white")
download_text.pack()

download_label = Label(root,text="0 Mbps",
                       font=("Times New Roman", 26, "bold"),bg="#0A2647",fg="#FFD700")
download_label.pack(pady=10)


upload_text = Label(root,text="Upload Speed",
                    font=("Times New Roman", 20, "bold"),bg="#0A2647",fg="white"
)
upload_text.pack()

upload_label = Label(root,text="0 Mbps",
                     font=("Times New Roman", 26, "bold"),bg="#0A2647",fg="#FFD700"
)
upload_label.pack(pady=10)


status_label = Label(root,text="Click button to start test",
                     font=("Times New Roman", 14),bg="#0A2647",fg="lightgreen"
)
status_label.pack(pady=20)


test_button = Button(root,text="Check Speed",
                     font=("Times New Roman", 20, "bold"),bg="#E94560",fg="white",
padx=20,pady=10,command=start_test
)
test_button.pack(pady=20)

root.mainloop()