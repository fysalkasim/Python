print("Hello\tWorld")
print("Languages:\nPython\nC\nJava")
print("Language:\n\tPython\n\t\tC\n\t\t\tJava")
#stripping means removing white space

language = "Python    "
print(language)
language = language.rstrip()
print(language)

country = " India"
print(country)
country = country.lstrip()
print(country)

location = "    My current location is Kerala    "
location = location.strip()
print(location)

