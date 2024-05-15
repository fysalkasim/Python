# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User:
    '''Here in this class we can collect user information'''
    def __init__(self,first_name,last_name,age,place):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.place = place
        self.login_attempt = 0

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"The user name :{full_name}")
        print(f"The {full_name} has an age of {self.age} and he is from {self.place}")
    def greet_user(self):
        print(f"Thank you for loging in {self.first_name} {self.last_name}")

    def increment_login_attempt(self):
        self.login_attempt += 1
    def rest_login_attempt(self):
        self.login_attempt = 0
jw = User("John","Wick",24, "Kochi")
jw.describe_user()
jw.greet_user()
jw.increment_login_attempt()
jw.increment_login_attempt()
jw.increment_login_attempt()
jw.increment_login_attempt()
jw.increment_login_attempt()
print(f'The total login attempt by {jw.first_name} is {jw.login_attempt}')
jw.rest_login_attempt()
print(f'Resetting login attempt by {jw.first_name}..... Current login attempt is {jw.login_attempt}')