# 10-13. User Dictionary: The remember_me.py example only stores one piece of
# information, the username. Expand this example by asking for two more pieces
# of information about the user, then store all the information you collect in a
# dictionary. Write this dictionary to a file using json.dumps(), and read it back
# in using json.loads(). Print a summary showing exactly what your program
# remembers about the user.

from pathlib import Path
import json

path = Path("user_dict.json")
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