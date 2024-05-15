# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    '''Creating a class of restaurant having name and their cuine type as attributes'''
    def __init__(self,name,cuisine_type):
        '''Initializing the name and cuisine type of the Restaurent'''
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        "Describing about the restaurant"
        print(f"The {self.name} of hotel is famous for their {self.cuisine_type} cuisine")
    def open_restaurant(self):
        """Tellig whether the resaturant is open or closed"""
        print(f"The {self.name} restaurant is open now you can have your favorite cuisines")
    def set_number(self,num):
        '''Here we can mannually input the value of number of servings'''
        self.number_served = num
    def inc_number(self,increment):
        '''Here we can mannually add the increment of number of people served'''
        self.number_served += increment
class IceCreamStand(Restaurant):
    '''Creating aspecific class for Ice cream stand under the restaurant class'''
    def __init__(self,name,cusinetype):
        '''Initializing attributes to from thr parent class'''
        super().__init__(name,cusinetype)
        self.flavours = ["Vanila","Pistha","Butterscotch"]
    def show_flaours(self):
        print(f"The flavours of the icecream stand s are {self.flavours}")

skei = IceCreamStand('Skei','Indian')
skei.show_flaours()