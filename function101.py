#Functions
def prog():
    price = int(input("What is the price: "))
    if price > 75:
        print("the price is too high")
        again()
    elif price < 75:
        print ("The price is really low")
        again()
    else:
        print ("it as it is equal")
        again()      
def again():
    ans= input("do you wish to check another price?")
    if ans == 'y':
        welcome()
    else:
        quit()
        
prog()
