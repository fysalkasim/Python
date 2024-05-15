# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
class Restaurant:
    '''Creating a class of restaurant having name and their cuine type as attributes'''
    def __init__(self,name,cuisine_type):
        '''Initializing the name and cuisine type of the Restaurent'''
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        "Describing about the restaurant"
        print(f"The {self.name} of hotel is famour for their {self.cuisine_type} cuisine")
    def open_restaurant(self):
        """Tellig whether the resaturant is open or closed"""
        print(f"The {self.name} restaurant is open now you can have your favorite cuisines")
    
kumar = Restaurant("Kumar","Indian")
kumar.describe_restaurant()
kumar.open_restaurant()

print(kumar.name)
print(kumar.cuisine_type)