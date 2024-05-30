from citycountrymodule import optpopulation
def test_city_population():
    '''Do population is required here we are going to test'''
    result = optpopulation('delhi', 'india', '100000')
    assert result == 'Delhi, India'