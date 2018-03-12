from unittest import TestCase

import task6

class TestPrime(TestCase):

  def setUp(self):
    """Init"""

  def test_is_json(self):
    """Test for json"""
    self.assertTrue(task6.write_to_json())
    
  def test_is_yaml(self):
    """Test for yaml"""
    self.assertTrue(task6.write_to_yaml())

  def tearDown(self):
    """Finish"""