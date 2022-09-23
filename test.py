import unittest 						
from helpers import Detecting_change, Season, Order_status

class Detecting_change_test(unittest.TestCase):
	"""Tests for detecting change """

	def test_detecting_change(self):
		"""Given a data, it's expeted to get the next dictionary
			1/2/20 TRUE
			1/6/20 TRUE
			1/8/20 TRUE	""" 	

		test_output = Detecting_change('test/detecting_change_test.csv')			   
		expected = {'1/2/20': True, '1/6/20': True, '1/8/20': True}
		self.assertDictEqual( expected, test_output)


class Season_test(unittest.TestCase):
	"""Tests for Seasons
		spring = 19/03/-- | 19/06/--
		summer = 20/06/-- | 21/09/--
		fall = 22/09/--   | 20/12/--
		winter = 21/12/-- | 18/03/-- """

	def test_spring(self):
		"""Test data for getting 'Spring ' given a date""" 	 
		test_output = Season('test/seasons_spring.csv')			   
		expected = {'86cdd3ce-a02c-4679-86cc-c64f207a27d2': 'spring'}	
		self.assertDictEqual( expected, test_output)

	def test_summer(self):
		"""Test data for getting 'summer ' given a date""" 	 
		test_output = Season('test/seasons_summer.csv')			   
		expected = {'86cdd3ce-a02c-4679-86cc-c64f207a27d2': 'summer'}	
		self.assertDictEqual( expected, test_output)

	def test_fall(self):
		"""Test data for getting 'fall ' given a date""" 	 
		test_output = Season('test/seasons_fall.csv')			   
		expected = {'86cdd3ce-a02c-4679-86cc-c64f207a27d2': 'fall'}	
		self.assertDictEqual( expected, test_output)

	def test_winter(self):
		"""Test data for getting 'winter ' given a date""" 	 
		test_output = Season('test/seasons_winter.csv')			   
		expected = {'86cdd3ce-a02c-4679-86cc-c64f207a27d2': 'winter'}	
		self.assertDictEqual( expected, test_output)


class Order_status_test(unittest.TestCase):
	"""Tests for Order_status"""

	def test_PENDING_output(self):
		"""Test data for getting 'PENDING' with data ['SHIPPED', 'SHIPPED', 'PENDING']""" 	 
		test_output = Order_status('test/ord_status_test1.csv')			   
		expected = {'Ord_1810': 'PENDING'} 		  
		self.assertDictEqual( expected, test_output)

	def test_SHIPPED_output(self):
		"""Test data for getting 'SHIPPED' with data ['SHIPPED', 'CANCELLED', 'CANCELLED'].""" 	 
		test_output = Order_status('test/ord_status_test2.csv')			   
		expected = {'Ord_1810': 'SHIPPED'} 		
		self.assertDictEqual( expected, test_output)	

	def test_CANCELLED_output(self):
		"""Test data for getting 'CANCELLED	 with data ['CANCELLED', 'CANCELLED'] .""" 	 
		test_output = Order_status('test/ord_status_test3.csv')			   
		expected = {'Ord_1810': 'CANCELLED'} 		  
		self.assertDictEqual( expected, test_output)


if __name__ == '__main__':
	unittest.main()