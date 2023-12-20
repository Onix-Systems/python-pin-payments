import unittest
from unittest.mock import patch, MagicMock

from requests.auth import HTTPBasicAuth

from pin_payments.refunds import RefundsAPI


class TestRefundsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.refunds_api = RefundsAPI(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.refunds_api._RefundsAPI__api_key, self.api_key)
        self.assertEqual(self.refunds_api._RefundsAPI__base_url, 'https://api.pinpayments.com/1/')
        self.assertEqual(self.refunds_api._RefundsAPI__auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.requests.get')
    def test_get_refunds_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"refunds": []}
        mock_get.return_value = mock_response

        response = self.refunds_api.get_refunds()

        self.assertEqual(response, {"refunds": []})
        mock_get.assert_called_once()

    @patch('pin_payments.requests.get')
    def test_get_refunds_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.refunds_api.get_refunds()

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.requests.get')
    def test_get_refunds_refund_token_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"refund": {"token": "refund_token"}}
        mock_get.return_value = mock_response

        response = self.refunds_api.get_refunds_refund_token(refund_token='refund_token')

        self.assertEqual(response, {"refund": {"token": "refund_token"}})
        mock_get.assert_called_once()

    @patch('pin_payments.requests.get')
    def test_get_refunds_refund_token_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.refunds_api.get_refunds_refund_token(refund_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.requests.post')
    def test_post_charges_charge_token_refunds_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"refund": {"token": "refund_token"}}
        mock_post.return_value = mock_response

        response = self.refunds_api.post_charges_charge_token_refunds(charge_token='charge_token')

        self.assertEqual(response, {"refund": {"token": "refund_token"}})
        mock_post.assert_called_once()

    @patch('pin_payments.requests.post')
    def test_post_charges_charge_token_refunds_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        response = self.refunds_api.post_charges_charge_token_refunds(charge_token='invalid_token')

        self.assertIn("error", response)
        mock_post.assert_called_once()

    @patch('pin_payments.requests.get')
    def test_get_charges_charge_token_refunds_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"refunds": []}
        mock_get.return_value = mock_response

        response = self.refunds_api.get_charges_charge_token_refunds(charge_token='charge_token')

        self.assertEqual(response, {"refunds": []})
        mock_get.assert_called_once()

    @patch('pin_payments.requests.get')
    def test_get_charges_charge_token_refunds_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.refunds_api.get_charges_charge_token_refunds(charge_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()
