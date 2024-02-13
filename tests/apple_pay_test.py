import unittest
from unittest.mock import patch, MagicMock

from pin_payments.apple_pay import ApplePayAPI


class TestApplePayAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.apple_pay_api = ApplePayAPI(api_key=self.api_key, mode='test')

    @patch('pin_payments.apple_pay.requests.post')
    def test_create_domain(self, mock_post):
        expected_response = {'response': {'domain_name': 'example.com', 'registered': True}}
        mock_post.return_value = MagicMock(status_code=201, json=lambda: expected_response)
        response = self.apple_pay_api.create_domain('example.com')
        self.assertEqual(response, expected_response)
        mock_post.assert_called_once()

    @patch('pin_payments.apple_pay.requests.get')
    def test_list_domains(self, mock_get):
        expected_response = {'response': [{'domain_name': 'example.com', 'registered': True}]}
        mock_get.return_value = MagicMock(status_code=200, json=lambda: expected_response)
        response = self.apple_pay_api.list_domains()
        self.assertEqual(response, expected_response)
        mock_get.assert_called_once()

    @patch('pin_payments.apple_pay.requests.delete')
    def test_delete_domain(self, mock_delete):
        mock_delete.return_value = MagicMock(status_code=204)
        self.apple_pay_api.delete_domain('domain_token')
        mock_delete.assert_called_once()

    @patch('pin_payments.apple_pay.requests.get')
    def test_check_host(self, mock_get):
        expected_response = {'response': {'domain_name': 'example.com', 'registered': True}}
        mock_get.return_value = MagicMock(status_code=200, json=lambda: expected_response)
        response = self.apple_pay_api.check_host('example.com')
        self.assertEqual(response, expected_response)
        mock_get.assert_called_once_with(
            f"{self.apple_pay_api._base_url}host_check",
            auth=self.apple_pay_api._auth,
            params={'domain_name': 'example.com'}
        )

    @patch('pin_payments.apple_pay.requests.post')
    def test_create_session(self, mock_post):
        expected_response = {'response': {'session': 'details'}}
        mock_post.return_value = MagicMock(status_code=201, json=lambda: expected_response)
        response = self.apple_pay_api.create_session('validation_url', 'web', 'example.com')
        self.assertEqual(response, expected_response)
        mock_post.assert_called_once()

    @patch('pin_payments.apple_pay.requests.post')
    def test_create_certificate(self, mock_post):
        expected_response = {'response': {'certificate': 'details'}}
        mock_post.return_value = MagicMock(status_code=201, json=lambda: expected_response)
        response = self.apple_pay_api.create_certificate()
        self.assertEqual(response, expected_response)
        mock_post.assert_called_once()

    @patch('pin_payments.apple_pay.requests.get')
    def test_list_certificates(self, mock_get):
        expected_response = {'response': [{'certificate': 'details'}]}
        mock_get.return_value = MagicMock(status_code=200, json=lambda: expected_response)
        response = self.apple_pay_api.list_certificates()
        self.assertEqual(response, expected_response)
        mock_get.assert_called_once()

    @patch('pin_payments.apple_pay.requests.get')
    def test_get_certificate(self, mock_get):
        expected_response = {'response': {'certificate': 'details'}}
        mock_get.return_value = MagicMock(status_code=200, json=lambda: expected_response)
        response = self.apple_pay_api.get_certificate('certificate_token')
        self.assertEqual(response, expected_response)
        mock_get.assert_called_once()

    @patch('pin_payments.apple_pay.requests.put')
    def test_upload_certificate(self, mock_put):
        expected_response = {'response': {'uploaded': True}}
        mock_put.return_value = MagicMock(status_code=200, json=lambda: expected_response)
        response = self.apple_pay_api.upload_certificate('pem_data')
        self.assertEqual(response, expected_response)
        mock_put.assert_called_once()

    @patch('pin_payments.apple_pay.requests.delete')
    def test_delete_certificate(self, mock_delete):
        mock_delete.return_value = MagicMock(status_code=204)
        self.apple_pay_api.delete_certificate('certificate_token')
        mock_delete.assert_called_once()
