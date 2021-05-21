import pytest
import leap_year

# Successful test
def test_2000():
	assert leap_year.leap_year(2000) == True, "2000 is not a leap year"
# Successful test
def test_100():
	assert leap_year.leap_year(100) == False, "100 is a leap year"

# Failed test
def test_3():
	assert leap_year.leap_year(3) == True, "3 is not a leap year"
# Failed test
def test_0():
	assert leap_year.leap_year(0) == False, "0 is a leap year"