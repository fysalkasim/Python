# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dumps() to store this number in a file. 
# Write a separate program that reads in this value and prints the message “I know your favorite
# number! It’s _____.”

from pathlib import Path
import json

fav = int(input("Enter your favourite number: "))

path = Path("CHAPTER 10/favnum.json")
content = json.dumps(fav)
path.write_text(content)

print(f"I know your fav number is {fav}")

content2 = path.read_text()
num = json.loads(content2)
print(num)
