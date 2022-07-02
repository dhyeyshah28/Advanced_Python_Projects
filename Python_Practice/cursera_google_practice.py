def enter_valid_username() :
    x = input("Please Enter your Name: ")
    if len(x) >= 10 :
        print("Entered UserName is more than the specified word limit !")
    elif len(x) <= 3 :
        print("Entered UserName is less than the specified word limit !")
    else :
        print("Valid UserName. Hurray ! ")

    y = input("Enter Your Age: ")
    if int(y) >= 50 :
        print("You are old ! :-P ")
    elif int(y) <= 10 :
        print("You are too young !")
    else :
        print("Perfect, Welcome You are allowed to avail our services !!!")

    Male = 0
    Female = 0
    z = input("Enter Your Gender: ")
    if int(y)>=10 and int(y)<= 50 :
        if z == Male :
            print("You are welcome to the Exclusive Boys Club ! ! !")

    
enter_valid_username()