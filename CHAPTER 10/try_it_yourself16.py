# 10-14. Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the person who last
# used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get the correct
# username.
from pathlib import Path
import json

def existing_user(path):
    """Getting stored info if available"""
    if path.exists():
        content = path.read_text()
        user_dict = json.loads(content)
        return user_dict
    else:
        return None

def new_user(path):
    """Getting new user info from input and adding to the dictionary then to the Json"""
    username = input("What is your name")
    age  = int(input("What is your age"))
    place = input("What is your favorite place in the world")
    user_dict = { 
        'username' : username,
        'Age' : age,
        'Favorite place' : place,
    }
    content = json.dumps(user_dict)
    path.write_text(content)
    return user_dict
def greet():
    '''The greeting to the user'''
    path = Path('user_info.json')
    user_dict = existing_user(path)
    if user_dict:
        print(f"I think you are {user_dict['username']} right?")
        inp = input("are you an existing user? YES/NO")
        if inp == "NO":
            user_dict = new_user(path)
            msg = f"We'll remember you when you return, {user_dict['username']}!"
            print(msg)   
        else:
            print(f"Welcome back, {user_dict['username']}!")
            print(f"Hope you've are still {user_dict['Age']} year old. ")
            print(f"Have you went for a trip to {user_dict['Favorite place']} recently?")

greet()