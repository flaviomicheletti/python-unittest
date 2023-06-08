import unittest
from unittest.mock import Mock, patch
import odometer


class TestOdometer(unittest.TestCase):

    def test_speed(self):
        """It's a mystery to me why this test doesn't fulfill the function."""
        s = odometer.speed()
        self.assertIsInstance(s, int)


    def test_alert_normal(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 70
        self.assertFalse(odometer.alert())

    def test_alert_overspeed(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 100
        self.assertFalse(odometer.alert())

    def test_alert_underspeed(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 59
        self.assertTrue(odometer.alert())


"""
Interesting because if you run the command below, the `odometer` file is needed.

python -m unittest test_odometer.py
"""

#
# 88%
#
