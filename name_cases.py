name = "fysal"
message = f"Hello {name}, would you like to learn some python today"
print(message)

print(name.title())
print(name.upper())
print(name.lower())

quote = "Do it with passion or not at all"
print(f"{name} once said '{quote}'  ")

name2 = " Fysal\t\nKasim "
print(name2)
print(name2.lstrip())
print(name2.rstrip())
print(name2.strip())

file_name = "python notes.txt"
file_name = file_name.removesuffix(".txt")
print(file_name)