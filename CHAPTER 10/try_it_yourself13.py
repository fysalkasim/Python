# 10-12. Favorite Number Remembered: Combine the two programs you wrote in
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

from pathlib import Path
import json

path = Path("favorite_number.json")
try:
    fav = path.read_text()
except FileNotFoundError:
    num = int(input("What is your favorite_number"))
    content = json.dump(num)
    path.write_text(num)
    print("Okey i will remember that")
else:
    num = json.loads(fav)
    print(f"I know {num} is your fav number right!")