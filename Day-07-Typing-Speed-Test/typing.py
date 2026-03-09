from time import time
import random as r

def mistake(partest, usertest):
    error = 0

    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1

    return error


def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_in_minutes = time_delay / 60

    speed_wpm = (len(userinput) / 5) / time_in_minutes

    return round(speed_wpm, 2)

while(True):
    ck = input("ready to test : yes/no :")
    if ck == "yes":
        test = [
        "about catch message learn join reply out paste team carry laugh join outside game clean fold go cold cake talk",
        "my name is vipul paswan"
        ]

        test1 = r.choice(test)

        print("***** Typing Speed Test *****")
        print()
        print(test1)
        print()

        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()

        print()
        print("Typing Speed:", speed_time(time_1, time_2, testinput), "WPM")
        print("Errors:", mistake(test1, testinput))
    
    elif(ck=="no"):
        print("Thank You...")
        break
    
    else:
        print("wrong input")