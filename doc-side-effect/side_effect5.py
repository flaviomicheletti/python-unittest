import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock


class TestSideEffect(unittest.TestCase):
    def test_01(self):
        """ Test a connection timeout """
        any_function = Mock()
        any_function.side_effect = Timeout

        with self.assertRaises(Timeout):
            any_function()


if __name__ == '__main__':
    unittest.main()
