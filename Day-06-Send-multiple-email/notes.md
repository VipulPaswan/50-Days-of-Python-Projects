# Day 6 – Send Multiple Emails using Python 📧

## 📌 Project Overview
This project demonstrates how to send emails to multiple recipients using Python.  
The program uses the **SMTP protocol** to connect with Gmail's mail server and send messages automatically.

This type of automation is useful for:
- Sending notifications
- Sending newsletters
- Sending automated alerts
- Bulk messaging systems

---

## 🚀 Features

- Connects to Gmail SMTP server
- Secure login using TLS
- Sends email to multiple recipients
- Custom subject and message body

---

## 🛠 Technologies Used

- Python 3
- smtplib (SMTP protocol)

---

## 📦 Installation

No external libraries are required.  
`smtplib` comes built into Python.

---

## ▶ Python Code

```python
import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

ob.login('your_email', 'your_password')

subject = "Send multiple email"
body = "I love Python"

message = "subject:{}\n\n{}".format(subject, body)

listadd = ['vipul@gmail.com', 'klrahul01@gmail.com']

ob.sendmail('your_email', listadd, message)

print("Email Sent Successfully")

ob.quit()