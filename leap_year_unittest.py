import unittest
import leap_year

class testLeapYear(unittest.TestCase):
	# Successful test
	def test_2000(self):
		self.assertEqual(leap_year.leap_year(2000), True)
	# Successful test
	def test_100(self):
		self.assertEqual(leap_year.leap_year(100), False)

	# Failed test
	def test_3(self):
		self.assertEqual(leap_year.leap_year(3), True)
	# Failed test
	def test_0(self):
		self.assertEqual(leap_year.leap_year(0), False)

	if __name__ == '__main__':
		unittest.main()
