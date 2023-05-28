import unittest
from unittest.mock import MagicMock, patch
from my_module5 import MongoConnection

class TestMongoConnection(unittest.TestCase):
    @patch('pymongo.MongoClient')
    def test_get_collection(self, mock_client):
        # create a mock database object
        mock_db = MagicMock()

        # configure the mock client to return the mock database
        mock_client.return_value.__getitem__.return_value = mock_db

        # create a MongoConnection object
        connection = MongoConnection('mydatabase')

        # get a collection object
        col = connection.get_collection('mycollection')

        # assert that the collection object was obtained from the mock database
        mock_db.__getitem__.assert_called_once_with('mycollection')

#
# 100%
#