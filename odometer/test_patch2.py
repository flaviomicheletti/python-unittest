import unittest
from unittest.mock import patch
from odometer import speed, alert


class TestOdometer(unittest.TestCase):
    @patch('odometer.randint')
    def test_speed_within_range(self, mock_randint):
        mock_randint.return_value = 75
        expected_min = 40
        expected_max = 120

        result = speed()

        self.assertGreaterEqual(result, expected_min)
        self.assertLessEqual(result, expected_max)
        
    @patch('odometer.speed')
    def test_alert_normal(self, mock_speed):
        # Test that alert() returns False when speed is within the normal range
        mock_speed.return_value = 80
        self.assertFalse(alert())

    @patch('odometer.speed')
    def test_alert_overspeed(self, mock_speed):
        # Test that alert() returns False when speed is above the normal range
        mock_speed.return_value = 110
        self.assertTrue(alert())

    @patch('odometer.speed')
    def test_alert_underspeed(self, mock_speed):
        # Test that alert() returns True when speed is below the normal range
        mock_speed.return_value = 50
        self.assertTrue(alert())


#
# 100%
#