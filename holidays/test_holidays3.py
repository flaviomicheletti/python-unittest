import unittest
from unittest.mock import Mock
import holidays


# class TestCalendar(unittest.TestCase):
#     def test_get_holidays_success(self):
#         # Mock the requests.get method to return a successful response
#         requests = Mock()
#         requests.get.side_effect = lambda url: Mock(
#             status_code=200,
#             json=lambda: {
#                 "12/25": "Christmas",
#                 "7/4": "Independence Day",
#             },
#         )

#         # Test that the get_holidays function returns the expected result
#         result = holidays.get_holidays()
#         self.assertEqual(result["12/25"], "Christmas")
#         self.assertEqual(result["7/4"], "Independence Day")

#     def test_get_holidays_failure(self):
#         # Mock the requests.get method to return a failed response
#         requests = Mock()
#         requests.get.side_effect = lambda url: Mock(status_code=404)

#         # Test that the get_holidays function returns None when the response is not successful
#         result = holidays.get_holidays()
#         self.assertIsNone(result)
