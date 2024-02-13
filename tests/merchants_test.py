import unittest
from unittest.mock import patch, MagicMock

from requests.auth import HTTPBasicAuth

from pin_payments.merchants import Merchants


class TestMerchantsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.merchants_api = Merchants(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.merchants_api._api_key, self.api_key)
        self.assertEqual(self.merchants_api._base_url, 'https://api.pinpayments.com/1/merchants/')
        self.assertEqual(self.merchants_api._auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.merchants.requests.post')
    def test_post_merchants_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.merchants_api.create(
            contact={},
            entity={},
            business={},
            bank_account={},
            director={}
        )

        self.assertEqual(response, {"success": True})
        mock_post.assert_called_once()

    @patch('pin_payments.merchants.requests.post')
    def test_post_merchants_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        response = self.merchants_api.create(
            contact={},
            entity={},
            business={},
            bank_account={},
            director={}
        )

        self.assertIn("error", response)
        mock_post.assert_called_once()

    @patch('pin_payments.merchants.requests.get')
    def test_get_merchants_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"merchants": []}
        mock_get.return_value = mock_response

        response = self.merchants_api.list()

        self.assertEqual(response, {"merchants": []})
        mock_get.assert_called_once()

    @patch('pin_payments.merchants.requests.get')
    def test_get_merchants_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.merchants_api.list()

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.merchants.requests.get')
    def test_get_merchants_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"merchant": {"token": "mrch_token"}}
        mock_get.return_value = mock_response

        response = self.merchants_api.details(merchant_token='mrch_token')

        self.assertEqual(response, {"merchant": {"token": "mrch_token"}})
        mock_get.assert_called_once()

    @patch('pin_payments.merchants.requests.get')
    def test_get_merchants_details_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.merchants_api.details(merchant_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.merchants.requests.get')
    def test_get_merchants_default_settings_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"settings": {}}
        mock_get.return_value = mock_response

        response = self.merchants_api.default_settings()

        self.assertEqual(response, {"settings": {}})
        mock_get.assert_called_once()

    @patch('pin_payments.merchants.requests.get')
    def test_get_merchants_default_settings_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.merchants_api.default_settings()

        self.assertIn("error", response)
        mock_get.assert_called_once()
