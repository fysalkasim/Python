import random
sandwich_orders = []
finished_sandwiches = []
while True:
    opens = input("Would you like to order some sanwiches? YES/NO: ")
    if opens.upper() == 'NO':
        break 
    else:
        orders = input("Enter the type of sandwich you would like to order: ")
        sandwich_orders.append(orders)
        print(f"Making the {orders} sandwich...")
        finished_sandwiches.append(orders)
words = ['tasty','delicious','amazing']
print(f"This is your final order list\n{finished_sandwiches}")
for j in finished_sandwiches:
    random_number = random.randint(0, 2)
    print(f"Here is your  {words[random_number]} {j} sandwich")
