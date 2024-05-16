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