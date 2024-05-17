# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org) and find
# a few texts you’d like to analyze. Download the text files for these works, or
# copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
from pathlib import Path
text = Path('alice.txt')
content = text.read_text(encoding='utf-8')
print(content.count("The"))
print(content.count("The "))
print(content.count("the"))
print(content.count("the "))

