import pytest
from citycountrymodule import citycountry
def test_city_country():
    """Do cities like'Delhi','India' wiull work"""
    result = citycountry('delhi','india')
    assert result == 'Delhi, India'