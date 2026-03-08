import smtplib  as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('your_email','your_password')
subject = 'Send multple email'
body = "I love Python"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ['vipul@gmail.com','klrahul01@gmail.com']
ob.sendmail('your_email',listadd,message)
print("send Mail")
ob.quit()


