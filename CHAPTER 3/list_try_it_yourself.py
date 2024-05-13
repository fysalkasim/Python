guest = ['Gokul','Mubi','Hari']
message = "You are invited to the dinner.. hope you there"
print(f'{guest[0]},{message}')
print(f'{guest[1]},{message}')
print(f'{guest[2]},{message}')
print()
guest[1] = 'Nami'
print(guest)
print(f'{guest[0]},{message}')
print(f'{guest[1]},{message}')
print(f'{guest[2]},{message}')
guest.insert(0,"Abin")
guest.insert(2,"Abhirami")
guest.append("Aswani")
print(guest)
print("we can only have to people for the dinner")
sorry = "Extremely sorry for the current situation hope we can arrange it later"
pop1 = guest.pop()
pop2 = guest.pop()
pop3 = guest.pop()
pop4 = guest.pop()
print(f'{pop1},{sorry}')
print(f'{pop2},{sorry}')
print(f'{pop3},{sorry}')
print(f'{pop4},{sorry}')
print(guest)
del guest[0]
del guest[0]
print(guest)
