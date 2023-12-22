import unittest
from unittest.mock import patch, MagicMock
from pin_payments.charges import Charges
from requests.auth import HTTPBasicAuth


class TestChargesAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.charges_api = Charges(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.charges_api._ChargesAPI__api_key, self.api_key)
        self.assertEqual(self.charges_api._ChargesAPI__base_url, 'https://api.pinpayments.com/1/charges/')
        self.assertEqual(self.charges_api._ChargesAPI__auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.charges.requests.post')
    def test_post_charges_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.charges_api.post_charges(
            email='test@example.com',
            description='Test Charge',
            amount=100,
            ip_address='192.168.1.1'
        )

        self.assertEqual(response, {"success": True})
        mock_post.assert_called_once()

    @patch('pin_payments.charges.requests.post')
    def test_post_charges_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        response = self.charges_api.post_charges(
            email='invalid',
            description='Test Charge',
            amount=100,
            ip_address='192.168.1.1'
        )

        self.assertIn("error", response)
        mock_post.assert_called_once()

    @patch('pin_payments.charges.requests.put')
    def test_put_charges_charge_token_void_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        response = self.charges_api.put_charges_charge_token_void(charge_token='ch_token')

        self.assertEqual(response, {"success": True})
        mock_put.assert_called_once()

    @patch('pin_payments.charges.requests.put')
    def test_put_charges_charge_token_void_failure(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_put.return_value = mock_response

        response = self.charges_api.put_charges_charge_token_void(charge_token='invalid_token')

        self.assertIn("error", response)
        mock_put.assert_called_once()

    @patch('pin_payments.charges.requests.put')
    def test_put_charges_charge_token_capture_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        response = self.charges_api.put_charges_charge_token_capture(charge_token='ch_token')

        self.assertEqual(response, {"success": True})
        mock_put.assert_called_once()

    @patch('pin_payments.charges.requests.put')
    def test_put_charges_charge_token_capture_failure(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_put.return_value = mock_response

        response = self.charges_api.put_charges_charge_token_capture(charge_token='invalid_token')

        self.assertIn("error", response)
        mock_put.assert_called_once()

    @patch('pin_payments.charges.requests.get')
    def test_get_charges_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.charges_api.get_charges()

        self.assertEqual(response, {"success": True})
        mock_get.assert_called_once()

    @patch('pin_payments.charges.requests.get')
    def test_get_charges_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.charges_api.get_charges()

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.charges.requests.get')
    def test_get_charges_search_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.charges_api.get_charges_search(query='test')

        self.assertEqual(response, {"success": True})
        mock_get.assert_called_once()

    @patch('pin_payments.charges.requests.get')
    def test_get_charges_search_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.charges_api.get_charges_search(query='test')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.charges.requests.get')
    def test_get_charges_charge_token_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.charges_api.get_charges_charge_token(charge_token='ch_token')

        self.assertEqual(response, {"success": True})
        mock_get.assert_called_once()

    @patch('pin_payments.charges.requests.get')
    def test_get_charges_charge_token_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.charges_api.get_charges_charge_token(charge_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.charges.requests.get')
    def test_get_charges_verify_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"verified": True}
        mock_get.return_value = mock_response

        response = self.charges_api.get_charges_verify(session_token='session_token')

        self.assertEqual(response, {"verified": True})
        mock_get.assert_called_once_with(
            f"{self.charges_api._ChargesAPI__base_url}verify?session_token=session_token",
            auth=self.charges_api._ChargesAPI__auth
        )

    @patch('pin_payments.charges.requests.get')
    def test_get_charges_verify_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.charges_api.get_charges_verify(session_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once_with(
            f"{self.charges_api._ChargesAPI__base_url}verify?session_token=invalid_token",
            auth=self.charges_api._ChargesAPI__auth
        )
