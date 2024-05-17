from pathlib import Path
path = Path("CHAPTER 10/Guest names.txt")

name = input("Enter your name")
path.write_text(name)

