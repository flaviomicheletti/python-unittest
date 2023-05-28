from unittest import TestCase
from unittest.mock import patch
from calculator1 import add


class TestCalculator100coverage(TestCase):
    def test_add2(self):
        with patch('calculator1.time.sleep', return_value=None) as mock_sleep:
            result = add(2, 3)
            mock_sleep.assert_called_once_with(5)
            self.assertEqual(result, 5)

#
# 100%
#