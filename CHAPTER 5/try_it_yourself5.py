current_users = ["Fysal","Abin","Mubashira","Gokul","Admin"]
new_users = ["Fysal","Gokul","Abhirami","Aswani","Anamika"]
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
            if new_user.lower() in current_users_lower:
                print(f"You need select another username, This username'{new_user}' has been alreday taken")
            else:
                print(f"This username '{new_user}'is available")
print("Thank you for choosing us")