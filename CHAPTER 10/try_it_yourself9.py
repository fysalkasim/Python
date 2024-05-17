# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail
# silently if either file is missing.
from pathlib import Path
path1 = Path("CHAPTER 10/Cats.txt")
path2 = Path("CHAPTER 10/Dogs.txt")
path1.write_text
list1 = [["Mike","Ranger","King-Ini"],["RODRIGO","ROCKY","KACKSON"]]
file_string = ''
for i in list1:
    file_string += f"{i}\n"

path1.write_text(file_string)
files = [path1,path2]
for i in files:
    print(f'Reading the files {i}:')
    try:
        content = i.read_text()
    except FileNotFoundError:
        pass
    else:
        print(content)