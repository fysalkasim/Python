colours = 'green'
if colours == 'green':
    print("You just earned five points")
if colours == 'red':
    print("Thanks") # here we doesnt have an output 
if colours == 'green':
    print("You just earned 5 points for shooting down the alien")
else:
    print("You just earned 10 points")

# if elif else
if colours == 'green':
    points = 5
elif colours == 'yellow':
    points = 10
else:
    points = 15
print(f"You just earned {points} points")

#stages of life
age = 25
if age < 2:
    print("The person is a Baby")
elif age < 4:
    print("The person is a Toddler")
elif age < 13:
    print("The person is a Kid")
elif age < 20:
    pring("The person is a Teenager")
elif age < 65:
    print("The person is an adult")
else:
    print("The person is Elder")

fruits = ["Orange","Mango","Jack fruit","Water Melon","Kiwi"]
if "Orange" in fruits:
    print("You really like orange")
if "Mango" in fruits:
    print("Glad to hear you really likes the mango")
if ("Water Melon" in fruits):
    print("You love the combo of Water melon and Mango")
