from unittest import TestCase
from unittest.mock import patch
from calc1 import add


class Testcalc1(TestCase):

    @patch('time.sleep', return_value=None)
    def test_add1(self, mock_sleep):
        result = add(2, 3)
        self.assertEqual(result, 5)
        mock_sleep.assert_called_once_with(5)

    def test_add2(self):
        with patch('calc1.time.sleep', return_value=None) as mock_sleep:
            result = add(2, 3)
            self.assertEqual(result, 5)
            mock_sleep.assert_called_once_with(5)

#
# 100%
#