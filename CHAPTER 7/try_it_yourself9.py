sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []
print("Sorry we are out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    prep = sandwich_orders.pop()
    print(f"We are making {prep} sandwiches for you")
    finished_sandwiches.append(prep)
print("\n")
for i in finished_sandwiches:
    print(f"we made {i} sandwich perfectly for you!")