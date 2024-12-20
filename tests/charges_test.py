import unittest
from unittest.mock import patch, MagicMock

from requests.auth import HTTPBasicAuth

from pin_payments.charges import Charges

BAD_REQUEST_TEXT = "Bad Request"


class TestChargesAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.charges_api = Charges(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.charges_api._api_key, self.api_key)
        self.assertEqual(self.charges_api._base_url, 'https://api.pinpayments.com/1/charges/')
        self.assertEqual(self.charges_api._auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.charges.rst.requests.post')
    def test_post_charges_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.charges_api.create(
            email='test@example.com',
            description='Test Charge 1',
            amount=100,
            ip_address='192.168.1.1',
            card_token='test_card_token'
        )

        self.assertEqual(response, {"success": True})
        mock_post.assert_called_once()

        expected_data = {
            "email": 'test@example.com',
            "description": 'Test Charge 1',
            "amount": 100,
            "ip_address": '192.168.1.1',
            "card_token": 'test_card_token'
        }
        mock_post.assert_called_with(self.charges_api._base_url, auth=self.charges_api._auth, data=expected_data)

    @patch('pin_payments.charges.rst.requests.post')
    def test_post_charges_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_response.json.return_value = {"error": "Bad request error"}
        mock_post.return_value = mock_response

        response = self.charges_api.create(
            email='invalid',
            description='Test Charge',
            amount=100,
            ip_address='192.168.1.1',
            card_token='invalid_card_token'
        )

        self.assertIn("error", response)
        mock_post.assert_called_once()

        expected_data = {
            "email": 'invalid',
            "description": 'Test Charge',
            "amount": 100,
            "ip_address": '192.168.1.1',
            "card_token": 'invalid_card_token'
        }
        mock_post.assert_called_with(self.charges_api._base_url, auth=self.charges_api._auth, data=expected_data)

    @patch('pin_payments.charges.rst.requests.put')
    def test_put_charges_charge_token_void_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        response = self.charges_api.void(charge_token='ch_token')

        self.assertEqual(response, {"success": True})
        mock_put.assert_called_once()

    @patch('pin_payments.charges.rst.requests.put')
    def test_put_charges_charge_token_void_failure(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_put.return_value = mock_response

        response = self.charges_api.void(charge_token='invalid_token')

        self.assertIn("error", response)
        mock_put.assert_called_once()

    @patch('pin_payments.charges.rst.requests.put')
    def test_put_charges_charge_token_capture_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        response = self.charges_api.capture(charge_token='ch_token')

        self.assertEqual(response, {"success": True})
        mock_put.assert_called_once()

    @patch('pin_payments.charges.rst.requests.put')
    def test_put_charges_charge_token_capture_failure(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_put.return_value = mock_response

        response = self.charges_api.capture(charge_token='invalid_token')

        self.assertIn("error", response)
        mock_put.assert_called_once()

    @patch('pin_payments.charges.rst.requests.get')
    def test_get_charges_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.charges_api.list()

        self.assertEqual(response, {"success": True})
        mock_get.assert_called_once()

    @patch('pin_payments.charges.rst.requests.get')
    def test_get_charges_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.charges_api.list()

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.charges.rst.requests.get')
    def test_get_charges_search_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.charges_api.search(query='test')

        self.assertEqual(response, {"success": True})
        mock_get.assert_called_once()

    @patch('pin_payments.charges.rst.requests.get')
    def test_get_charges_search_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.charges_api.search(query='test')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.charges.rst.requests.get')
    def test_get_charges_charge_token_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.charges_api.charge(charge_token='ch_token')

        self.assertEqual(response, {"success": True})
        mock_get.assert_called_once()

    @patch('pin_payments.charges.rst.requests.get')
    def test_get_charges_charge_token_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.charges_api.charge(charge_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.charges.rst.requests.get')
    def test_get_charges_verify_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"verified": True}
        mock_get.return_value = mock_response

        response = self.charges_api.verify(session_token='session_token')

        self.assertEqual(response, {"verified": True})
        mock_get.assert_called_once_with(
            f"{self.charges_api._base_url}verify?session_token=session_token",
            auth=self.charges_api._auth
        )

    @patch('pin_payments.charges.rst.requests.get')
    def test_get_charges_verify_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.charges_api.verify(session_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once_with(
            f"{self.charges_api._base_url}verify?session_token=invalid_token",
            auth=self.charges_api._auth
        )
