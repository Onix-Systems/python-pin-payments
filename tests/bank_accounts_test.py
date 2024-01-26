import unittest
from unittest.mock import patch, MagicMock

from requests.auth import HTTPBasicAuth

from pin_payments.bank_accounts import BankAccounts


class TestBankAccountsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.bank_accounts_api = BankAccounts(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.bank_accounts_api._api_key, self.api_key)
        self.assertTrue(self.bank_accounts_api._base_url.endswith('/bank_accounts/'))
        self.assertEqual(self.bank_accounts_api._auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.bank_accounts.requests.post')
    def test_create_bank_account_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"response": {"token": "ba_token"}}
        mock_post.return_value = mock_response

        response = self.bank_accounts_api.create(
            name='John Doe',
            bsb='123456',
            number='987654321'
        )

        self.assertEqual(response, {"response": {"token": "ba_token"}})
        mock_post.assert_called_once()

    @patch('pin_payments.bank_accounts.requests.post')
    def test_create_bank_account_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.json.return_value = {"error": "Invalid resource"}
        mock_post.return_value = mock_response

        response = self.bank_accounts_api.create(
            name='Invalid',
            bsb='123',
            number='123'
        )

        self.assertIn("error", response)
        mock_post.assert_called_once()
