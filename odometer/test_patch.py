import unittest
from unittest.mock import patch
import odometer


class TestOdometer(unittest.TestCase):
    @patch("odometer.speed")
    def test_alert_normal(self, mock):
        mock.return_value = 70
        self.assertFalse(odometer.alert())

    @patch("odometer.speed")
    def test_alert_overspeed(self, mock):
        mock.return_value = 100
        self.assertFalse(odometer.alert())

    @patch("odometer.speed")
    def test_alert_underspeed(self, mock):
        mock.return_value = 59
        self.assertTrue(odometer.alert())

#
# 88%
#
