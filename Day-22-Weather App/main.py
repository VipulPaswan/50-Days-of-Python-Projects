from tkinter import *
from tkinter import ttk
import requests

API_KEY = "ad94e2b5d1345ee628a36de61f0d6f5b"

def data_get():
    city = city_name.get()
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    
    if data["cod"] != 200:
        w_label_1.config(text="Invalid city")
        wd_label_1.config(text="")
        temp_label_1.config(text="")
        press_label1.config(text="")
        return
    
    w_label_1.config(text=data["weather"][0]["main"])
    wd_label_1.config(text=data["weather"][0]["description"])
    temp_label_1.config(text=str(data["main"]["temp"]) + " °C")
    press_label1.config(text=str(data["main"]["pressure"]) + " hPa")

win = Tk()
win.title("Weather App")
win.configure(bg="skyblue")
win.geometry("560x600")

name_label = Label(win, text="Weather App", font=("Times New Roman",40,"bold"), bg="skyblue")
name_label.place(x=25, y=50, height=55, width=500)
city_name = StringVar()
list_name = [
    "Delhi","Mumbai","Lucknow","Patna","Jaipur","Bhopal",
    "Kolkata","Chennai","Bangalore","Hyderabad"
]

com = ttk.Combobox(win, values=list_name, font=("Times New Roman",20,"bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=500)


done_button = Button(win, text="Done", font=("Times New Roman",20,"bold"), command=data_get)
done_button.place(x=240, y=190, height=50, width=100)


w_label = Label(win, text="Weather Climate", font=("Times New Roman",18), bg="skyblue")
w_label.place(x=30, y=260, height=50, width=240)

w_label_1 = Label(win, text="", font=("Times New Roman",18), bg="skyblue")
w_label_1.place(x=290, y=260, height=50, width=240)


wd_label = Label(win, text="Weather Description", font=("Times New Roman",18), bg="skyblue")
wd_label.place(x=30, y=330, height=50, width=240)

wd_label_1 = Label(win, text="", font=("Times New Roman",18), bg="skyblue")
wd_label_1.place(x=290, y=330, height=50, width=240)


temp_label = Label(win, text="Temperature", font=("Times New Roman",18), bg="skyblue")
temp_label.place(x=30, y=400, height=50, width=240)

temp_label_1 = Label(win, text="", font=("Times New Roman",18), bg="skyblue")
temp_label_1.place(x=290, y=400, height=50, width=240)


press_label = Label(win, text="Pressure", font=("Times New Roman",18), bg="skyblue")
press_label.place(x=30, y=470, height=50, width=240)

press_label1 = Label(win, text="", font=("Times New Roman",18), bg="skyblue")
press_label1.place(x=290, y=470, height=50, width=240)

win.mainloop()