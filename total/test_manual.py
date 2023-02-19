import unittest
from unittest.mock import patch
import total


class TestTotalManual(unittest.TestCase):
    def test_calculate_total(self):
        # start patching
        patcher = patch("total.read")

        # create a mock object
        mock = patcher.start()

        # assign the return value
        mock.return_value = [1, 2, 3]

        # test the calculate_total
        result = total.calculate("fake-filename")
        self.assertEqual(result, 6)

        # stop patching
        patcher.stop()
