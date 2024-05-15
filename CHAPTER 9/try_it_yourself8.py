# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class User:
    '''Here in this class we can collect user information'''
    def __init__(self,first_name,last_name,age,place):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.place = place

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"The user name :{full_name}")
        print(f"The {full_name} has an age of {self.age} and he is from {self.place}")
    def greet_user(self):
        print(f"Thank you for loging in {self.first_name} {self.last_name}")
class Admin(User):
    '''Creating an admin class special for the user'''
    def __init__(self,first_name,last_name,age,place):
        super().__init__(first_name,last_name,age,place)
        self.privileges = ['Can add post','cn delet post','can ban user']
    '''adding a special method to call the privilages attributes'''
class privileges(Admin):
    '''Creating a seperate class named privileges'''
    def __init__(self, first_name, last_name, age, place):
        super().__init__(first_name, last_name, age, place)
        self.privileges = []
    def show_privileges(self):
        print(f'The Admin have a different kind of privileges those are: {self.privileges}')
cilian = privileges('cilian','Murphy',40,'Irelend')
cilian.privileges = ['Can edit','Can delete','Can copy']
cilian.show_privileges()