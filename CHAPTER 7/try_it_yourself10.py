# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.
active = True
poll = {}
while active:
    name = input("Enter your name: ")
    place = input("If you could visit one place in the world, where would you go?...")
    poll[name] = place
    repeat = input("Woul you like to let another person respond?: YES/NO")
    if repeat.upper() == 'NO':
        active = False
print(".....The Polling is finished thank you for participating.....")
print("The results are")
for k,v in poll.items():
    print(f"The {k} wishes to go to {v}")