user = {
    "First Name": "Fysal",
    "Last Name": "Kasim",
    "Age":24,
    "Place":"Karunagappally",
}
print(user["Age"])
print(user["First Name"])
print(user["Last Name"])
print(user["Place"])

fav_num = {
    "Fysal":3005,
    "Abin": 2509,
    "Gokul":606,
    "Haritha":407,
}
print(fav_num)

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points',"No Key Found")
print(point_value)