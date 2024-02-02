import unittest
from unittest.mock import patch, MagicMock

from pin_payments.transfers import Transfers
from requests.auth import HTTPBasicAuth


class TestTransfersAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.transfers_api = Transfers(api_key=self.api_key)

    @patch('pin_payments.transfers.requests.post')
    def test_create_transfer_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.transfers_api.create(
            description='Test Transfer',
            amount=100,
            currency='AUD',
            recipient='rp_token'
        )

        self.assertEqual(response, {"success": True})
        mock_post.assert_called_once_with(
            self.transfers_api._base_url,
            auth=HTTPBasicAuth(self.api_key, ''),
            data={
                'description': 'Test Transfer',
                'amount': 100,
                'currency': 'AUD',
                'recipient': 'rp_token'
            }
        )

    @patch('pin_payments.transfers.requests.get')
    def test_list_transfers_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"transfers": []}
        mock_get.return_value = mock_response

        response = self.transfers_api.list()

        self.assertEqual(response, {"transfers": []})
        mock_get.assert_called_once_with(
            self.transfers_api._base_url,
            auth=HTTPBasicAuth(self.api_key, '')
        )

    @patch('pin_payments.transfers.requests.get')
    def test_search_transfers_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"transfers": []}
        mock_get.return_value = mock_response

        response = self.transfers_api.search(query='Test')

        self.assertEqual(response, {"transfers": []})
        mock_get.assert_called_once_with(
            f"{self.transfers_api._base_url}search",
            auth=HTTPBasicAuth(self.api_key, ''),
            params={
                'query': 'Test'
            }
        )

    @patch('pin_payments.transfers.requests.get')
    def test_transfer_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"transfer": {"token": "transfer_token"}}
        mock_get.return_value = mock_response

        response = self.transfers_api.details(transfer_token='transfer_token')

        self.assertEqual(response, {"transfer": {"token": "transfer_token"}})
        mock_get.assert_called_once_with(
            f"{self.transfers_api._base_url}transfer_token",
            auth=HTTPBasicAuth(self.api_key, '')
        )

    @patch('pin_payments.transfers.requests.get')
    def test_line_items_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"line_items": []}
        mock_get.return_value = mock_response

        response = self.transfers_api.line_items(transfer_token='transfer_token')

        self.assertEqual(response, {"line_items": []})
        mock_get.assert_called_once_with(
            f"{self.transfers_api._base_url}transfer_token/line_items",
            auth=HTTPBasicAuth(self.api_key, '')
        )
