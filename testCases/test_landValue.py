import unittest
import landValueCon


class TestLandValue(unittest.TestCase):

    def test_land_value(self):
        land = landValueCon.get_land_value('Colombo')
        self.assertIsInstance(land, dict, 'Should return a dictionary')
        self.assertEqual(land['city'], 'Colombo', 'Wrong result')
