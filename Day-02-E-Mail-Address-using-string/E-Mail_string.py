email = input("Enter your Email:")
k=j=d = 0
if(len(email)>=6):
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                        
                    elif i.isalpha():
                        if i==i.upper():
                            j = 1
                            
                    elif i.isdigit():
                        continue
                    
                    elif i == "_" or i=="." or i=="@":
                        continue
                    
                    else:
                        d = 1                        
                if k==1 or j==1 or d==1:
                    print("Wrong Email 5")
                    
                else:
                    print("Right Email.")            
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")
    
    
# ----OUTPUT----

    """
    
    Case 1 -> Enter your Email:vipul
                Wrong Email 1
    
    Case 2 -> Enter your Email:1vipul
                Wrong Email 2
    
    Case 3 -> Enter your Email:vipulgmail.com
                Wrong Email 3
    
    Case 4 -> Enter your Email:vipul@gmail. com
                Wrong Email 4
    
    Case 5 -> Enter your Email:Vipul@gmail.com
                Wrong Email 5
    
    Case 6 -> Enter your Email:vipul@gmail.in
                Right Email.
            Enter your Email:vipul@gmail.com
                Right Email.   
    
    """