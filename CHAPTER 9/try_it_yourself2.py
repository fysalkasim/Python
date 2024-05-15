# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
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
thaza = Restaurant("Thaza","Arabian")

kumar.describe_restaurant()
thaza.describe_restaurant()