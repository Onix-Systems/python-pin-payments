import unittest
from unittest.mock import patch, MagicMock

from pin_payments.subscriptions import Subscriptions


class TestSubscriptionsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.subscriptions_api = Subscriptions(api_key=self.api_key, mode='test')

    @patch('pin_payments.subscriptions.requests.post')
    def test_create_subscription_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.subscriptions_api.create_subscription(
            plan_token='plan_token',
            customer_token='customer_token'
        )

        self.assertTrue(response['success'])
        mock_post.assert_called_once()

    @patch('pin_payments.subscriptions.requests.get')
    def test_list_subscriptions_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"subscriptions": []}
        mock_get.return_value = mock_response

        response = self.subscriptions_api.list_subscriptions()

        self.assertIsInstance(response['subscriptions'], list)
        mock_get.assert_called_once()

    @patch('pin_payments.subscriptions.requests.get')
    def test_get_subscription_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.subscriptions_api.get_subscription_details('sub_token')

        self.assertTrue(response['success'])
        mock_get.assert_called_once()

    @patch('pin_payments.subscriptions.requests.put')
    def test_update_subscription_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        response = self.subscriptions_api.update_subscription(
            'sub_token', 'new_card_token'
        )

        self.assertTrue(response['success'])
        mock_put.assert_called_once()

    @patch('pin_payments.subscriptions.requests.delete')
    def test_cancel_subscription_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_delete.return_value = mock_response

        response = self.subscriptions_api.cancel_subscription('sub_token')

        self.assertTrue(response['success'])
        mock_delete.assert_called_once()

    @patch('pin_payments.subscriptions.requests.put')
    def test_reactivate_subscription_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        response = self.subscriptions_api.reactivate_subscription('sub_token')

        self.assertTrue(response['success'])
        mock_put.assert_called_once()

    @patch('pin_payments.subscriptions.requests.get')
    def test_fetch_subscription_ledger_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"ledger": []}
        mock_get.return_value = mock_response

        response = self.subscriptions_api.fetch_subscription_ledger('sub_token')

        self.assertIsInstance(response['ledger'], list)
        mock_get.assert_called_once()
