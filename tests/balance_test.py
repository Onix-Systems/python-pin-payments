import unittest
from unittest.mock import patch, MagicMock

from pin_payments.balance import Balance
from requests.auth import HTTPBasicAuth


class TestBalanceAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.balance_api = Balance(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.balance_api._api_key, self.api_key)
        self.assertEqual(
            self.balance_api._base_url,
            'https://api.pinpayments.com/1/balance/'
        )
        self.assertEqual(self.balance_api._auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.balance.requests.get')
    def test_get_balance_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": {"available": [{"amount": 400, "currency": "AUD"}],
                         "pending": [{"amount": 1200, "currency": "AUD"}]}
        }
        mock_get.return_value = mock_response

        response = self.balance_api.detail()
        self.assertEqual(response, {
            "response": {"available": [{"amount": 400, "currency": "AUD"}],
                         "pending": [{"amount": 1200, "currency": "AUD"}]}}
                         )
        mock_get.assert_called_once()

    @patch('pin_payments.balance.requests.get')
    def test_get_balance_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Bad request"}
        mock_get.return_value = mock_response

        response = self.balance_api.detail()
        self.assertIn("error", response)
        mock_get.assert_called_once()
