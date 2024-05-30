from citycountrymodule import population
def test_city_population():
    '''Do population is required here we are going to test'''
    result = population('delhi', 'india', '100000')
    assert result == 'Delhi, India-the population is 100000'