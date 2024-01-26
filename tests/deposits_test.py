import unittest
from unittest.mock import patch, MagicMock

from pin_payments.deposits import Deposits


class TestDepositsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.deposits_api = Deposits(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.deposits_api._api_key, self.api_key)
        self.assertIn('deposits/', self.deposits_api._base_url)

    @patch('pin_payments.deposits.requests.get')
    def test_list_deposits_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": []}
        mock_get.return_value = mock_response

        response = self.deposits_api.list()

        self.assertEqual(response, {"response": []})
        mock_get.assert_called_once()

    @patch('pin_payments.deposits.requests.get')
    def test_list_deposits_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Bad request"}
        mock_get.return_value = mock_response

        response = self.deposits_api.list()

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.deposits.requests.get')
    def test_deposit_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": {"token": "dpo_token"}}
        mock_get.return_value = mock_response

        response = self.deposits_api.details(deposit_token='dpo_token')

        self.assertEqual(response, {"response": {"token": "dpo_token"}})
        mock_get.assert_called_once_with(f'{self.deposits_api._base_url}dpo_token', auth=self.deposits_api._auth)

    @patch('pin_payments.deposits.requests.get')
    def test_deposit_details_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"error": "Not found"}
        mock_get.return_value = mock_response

        response = self.deposits_api.details(deposit_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once_with(f'{self.deposits_api._base_url}invalid_token', auth=self.deposits_api._auth)
