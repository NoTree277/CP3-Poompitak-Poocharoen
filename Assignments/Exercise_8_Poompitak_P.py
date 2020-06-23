Username = input("Username :")
Password = input("Password :")
if Username == "LOL222" and Password =="123456":
    print("Login Success")
    print("Welcome To O Shop")
    print("1.Premium Wagyu 1250 THB/Kg")
    print("2.Loin 150 THB/Kg")
    print("3.Belly 200 THB/Kg")
    print("4.Ham 320 THB/Kg")
    UserChoose = int(input(">>"))
    if UserChoose == 1 :
        print("You Choose Premium Wagyu")
        Kg = int(input("How Much Do You Want(Kg):"))
        price = 1250*Kg
        print("Price Is :",price,"THB")
        vat = 7
        result = price + (price * vat / 100)
        print("Plus Vat 7%")
        print("Total :", result,"THB")
        print("Thankyou For Shopping With Us")
    elif UserChoose == 2 :
        print("You Choose Loin")
        Kg = int(input("How Much Do You Want(Kg):"))
        price = 150*Kg
        print("Price Is :",price,"THB")
        vat = 7
        result = price + (price * vat / 100)
        print("Plus Vat 7%")
        print("Total :", result,"THB")
        print("Thankyou For Shopping With Us")
    elif UserChoose == 3 :
        print("You Choose Belly")
        Kg = int(input("How Much Do You Want(Kg):"))
        price = 200*Kg
        print("Price Is :",price,"THB")
        vat = 7
        result = price + (price * vat / 100)
        print("Plus Vat 7%")
        print("Total :", result,"THB")
        print("Thankyou For Shopping With Us")
    elif UserChoose == 4 :
        print("You Choose Ham")
        Kg = int(input("How Much Do You Want(Kg):"))
        price = 320*Kg
        print("Price Is :",price,"THB")
        vat = 7
        result = price + (price * vat / 100)
        print("Plus Vat 7%")
        print("Total :", result,"THB")
        print("Thankyou For Shopping With Us")
    else:
        print("Error")
else:
    print("Worng Username Or Password Please Try Again")