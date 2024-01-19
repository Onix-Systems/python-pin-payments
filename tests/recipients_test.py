import unittest
from unittest.mock import patch, MagicMock

from pin_payments.recipients import Recipients
from requests.auth import HTTPBasicAuth

BAD_REQUEST_TEXT = "Bad Request"


class TestRecipientsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.recipients_api = Recipients(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.recipients_api._api_key, self.api_key)
        self.assertEqual(self.recipients_api._base_url, 'https://api.pinpayments.com/1/recipients/')
        self.assertEqual(self.recipients_api._auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.recipients.requests.post')
    def test_create_recipient_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.recipients_api.create(email='test@example.com')
        self.assertEqual(response, {"success": True})

    @patch('pin_payments.recipients.requests.post')
    def test_create_recipient_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_response.json.return_value = {"error": "Bad request error"}
        mock_post.return_value = mock_response

        response = self.recipients_api.create(email='invalid')
        self.assertIn("error", response)

    @patch('pin_payments.recipients.requests.get')
    def test_list_recipients_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.recipients_api.list()
        self.assertEqual(response, {"success": True})

    @patch('pin_payments.recipients.requests.get')
    def test_get_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.recipients_api.get_details(recipient_token='recipient_token')
        self.assertEqual(response, {"success": True})

    @patch('pin_payments.recipients.requests.put')
    def test_update_recipient_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        response = self.recipients_api.update(recipient_token='recipient_token')
        self.assertEqual(response, {"success": True})

    @patch('pin_payments.recipients.requests.put')
    def test_update_recipient_failure(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_put.return_value = mock_response

        response = self.recipients_api.update(recipient_token='invalid_token')
        self.assertIn("error", response)

    @patch('pin_payments.recipients.requests.get')
    def test_list_transfers_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.recipients_api.list_transfers(recipient_token='recipient_token')
        self.assertEqual(response, {"success": True})

    @patch('pin_payments.recipients.requests.get')
    def test_list_transfers_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.recipients_api.list_transfers(recipient_token='invalid_token')
        self.assertIn("error", response)
