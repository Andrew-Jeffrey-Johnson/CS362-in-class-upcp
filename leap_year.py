###############################################################################
# This file is designed to be run on the OSU FLIP servers. 
# To run the program, enter in the command below into the FLIP servers.
#	python3 hw1.py
###############################################################################

# determine leap year
def leap_year (year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True	
	else:
		return False
