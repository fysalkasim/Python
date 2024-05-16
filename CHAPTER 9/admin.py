from user import User
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