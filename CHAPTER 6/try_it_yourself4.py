polling_list = ['jen','sarah','edward','phil','faayiz','fysal','gokul']

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 'faayiz' : 'Java'
 }
for i in polling_list:
    if i in favorite_languages.keys():
        print(f"Thanks for voting {i}")
    else:
        print(f"{i} You should participate in the polling")
print(set(favorite_languages.values()))