active = True
while active:
    userage = int(input("Enter you age or enter '0'to quit"))
    if userage == 0:
        active = False 
    elif userage < 3:
        print("The ticket is free")
    elif userage >= 3 and userage <= 12:
        print("The ticket price is $10")
    else:
        print("The ticket price is $15")