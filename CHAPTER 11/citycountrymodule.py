# 11-1. City, Country: Write a function that accepts two parameters: a city name
# and a country name. The function should return a single string of the form
# City, Country, such as Santiago, Chile. Store the function in a module called
# city_functions.py, and save this file in a new folder so pytest won’t try to run the
# tests we’ve already written.
# Create a file called test_cities.py that tests the function you just wrote.
# Write a function called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string. Run the
# test, and make sure test_city_country() passes.
def citycountry(city,country):
    '''A FUNCTION WHICH RETURN AS VALUE IN CONTINUES'''
    answer = f"{city.title()}, {country.title()}"
    return answer
def population(city,country,population):
    '''A FUNCTION WHICH RETURN AS VALUE IN CONTINUES'''
    answer = f"{city.title()}, {country.title()}-the population is {population}"
    return answer
# 11-2. Population: Modify your function so it requires a third parameter, population.
# It should now return a single string of the form City, Country – population xxx,
# such as Santiago, Chile – population 5000000. Run the test again, and make sure
# test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run the test,
# and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies
# you can call your function with the values 'santiago', 'chile', and 'population
# =5000000'. Run the tests one more time, and make sure this new test passes.