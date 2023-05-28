from unittest import TestCase
from unittest.mock import patch
from calculator1 import add


class TestCalculator100coverage(TestCase):
    @patch("calculator1.add")
    def test_add(self, mock):
        expected = 9

        mock.return_value = expected

        actual = mock(5, 5)
        self.assertEqual(actual, expected)

#
# 50%
#