# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.
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

hotel = Restaurant('Kumar','Indian')
hotel.describe_restaurant()
print(hotel.number_served)
hotel.set_number(205)
print(hotel.number_served)
hotel.inc_number(305)
print(hotel.number_served)

