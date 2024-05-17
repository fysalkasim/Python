# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block
# executes properly.
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
        print("The file is not found")
    else:
        print(content)