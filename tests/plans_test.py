import unittest
from unittest.mock import patch, MagicMock

from requests.auth import HTTPBasicAuth

from pin_payments.plans import Plans


class TestPlansAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.plans_api = Plans(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.plans_api._api_key, self.api_key)
        self.assertEqual(self.plans_api._base_url, 'https://api.pinpayments.com/1/plans/')
        self.assertEqual(self.plans_api._auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.plans.requests.post')
    def test_create_plan_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"response": {"token": "plan_token"}}
        mock_post.return_value = mock_response

        response = self.plans_api.create(name='Test Plan', amount=1000, interval=30, interval_unit='day')

        self.assertEqual(response, {"response": {"token": "plan_token"}})
        mock_post.assert_called_once()

    @patch('pin_payments.plans.requests.get')
    def test_list_plans_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": []}
        mock_get.return_value = mock_response

        response = self.plans_api.list()

        self.assertEqual(response, {"response": []})
        mock_get.assert_called_once()

    @patch('pin_payments.plans.requests.get')
    def test_plan_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": {"token": "plan_token"}}
        mock_get.return_value = mock_response

        response = self.plans_api.details(plan_token='plan_token')

        self.assertEqual(response, {"response": {"token": "plan_token"}})
        mock_get.assert_called_once()

    @patch('pin_payments.plans.requests.put')
    def test_update_plan_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": {"token": "plan_token"}}
        mock_put.return_value = mock_response

        response = self.plans_api.update(plan_token='plan_token', name='Updated Plan')

        self.assertEqual(response, {"response": {"token": "plan_token"}})
        mock_put.assert_called_once()

    @patch('pin_payments.plans.requests.delete')
    def test_delete_plan_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_response.json.return_value = {}
        mock_delete.return_value = mock_response

        response = self.plans_api.delete(plan_token='plan_token')

        self.assertEqual(response, {})
        mock_delete.assert_called_once()

    @patch('pin_payments.plans.requests.post')
    def test_create_subscription_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": {"token": "subscription_token"}}
        mock_post.return_value = mock_response

        response = self.plans_api.create_subscription(plan_token='plan_token', customer_token='customer_token')

        self.assertEqual(response, {"response": {"token": "subscription_token"}})
        mock_post.assert_called_once()

    @patch('pin_payments.plans.requests.get')
    def test_list_subscriptions_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": []}
        mock_get.return_value = mock_response

        response = self.plans_api.list_subscriptions(plan_token='plan_token')

        self.assertEqual(response, {"response": []})
        mock_get.assert_called_once()
