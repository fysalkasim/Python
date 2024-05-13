glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'Set':"We can't include duplicated items in the set",
    'if': "We can use if for to make some condition in our python language"
    }
for keys, values in glossary.items():
    print(f"\n{keys}: {values}")
rivers = {
    "Egypth" : "Neil",
    "Kerala" : "Periyar",
    "India" : "Ganga",
    "Karnataka" : "Kaveri" 
}
for keys, values in rivers.items():
    print(f"The {values} runs through {keys}")
print('The river in the dictionaries')
for v in rivers.values():
    print(f"\n{v}")
for k in rivers.keys():
    print(f"\n {k}")
