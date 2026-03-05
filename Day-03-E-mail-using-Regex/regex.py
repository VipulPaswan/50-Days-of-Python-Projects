import re

email = input("Enter your Email: ")

pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

if re.search(pattern, email):
    print("Right Email")
else:
    print("Wrong Email")
    
    
# ----OUTPUT----

    """
    
    Case 1 -> Enter your Email:vipul
                Wrong Email 
    
    Case 2 -> Enter your Email:1vipul
                Wrong Email 
    
    Case 3 -> Enter your Email:vipulgmail.com
                Wrong Email 
    
    Case 4 -> Enter your Email:vipul@gmail. com
                Wrong Email 
    
    Case 5 -> Enter your Email:Vipul@gmail.com
                Wrong Email 
    
    Case 6 -> Enter your Email:vipul@gmail.in
                Right Email.
            Enter your Email:vipul@gmail.com
                Right Email.   
    
    """