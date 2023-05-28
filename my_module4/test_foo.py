# test_my_module.py
import unittest
from unittest.mock import MagicMock, patch
import my_module4


class TestCreateFile(unittest.TestCase):
    def test_create_file_success(self):
        mock_os_path_exists = MagicMock(return_value=False)

        with patch("os.path.exists", mock_os_path_exists), patch(
            "builtins.open", create=True
        ) as mock_open:
            result = my_module4.create_file("test.txt")

            mock_os_path_exists.assert_called_once_with("test.txt")
            mock_open.assert_called_once_with("test.txt", "w")
            # mock_open.return_value.write.assert_called_once_with("Hello, world!")
            self.assertTrue(result)

    def test_create_file_failure(self):
        mock_os_path_exists = MagicMock(return_value=True)

        with patch("os.path.exists", mock_os_path_exists):
            result = my_module4.create_file("test.txt")

            mock_os_path_exists.assert_called_once_with("test.txt")
            self.assertFalse(result)

#
# 100%
#