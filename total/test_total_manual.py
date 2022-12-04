import unittest
from unittest.mock import patch
import total


class TestTotalManual(unittest.TestCase):
    def test_calculate_total(self):
        # start patching
        patcher = patch("total.read")

        # create a mock object
        mock_read = patcher.start()

        # assign the return value
        mock_read.return_value = [1, 2, 3]

        # test the calculate_total
        result = total.calculate_total("")
        self.assertEqual(result, 6)

        # stop patching
        patcher.stop()
