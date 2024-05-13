prompt = "\nTell me your pizza topping:"
prompt += "\nEnter 'quit' to end the program. "
while True:
    toopings = input(prompt)
    if toopings == 'quit':
        break
    else:
        print(f"Adding the {toopings} to your pizza")