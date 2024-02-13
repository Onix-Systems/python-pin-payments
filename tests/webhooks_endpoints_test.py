import unittest
from unittest.mock import patch, MagicMock

from pin_payments.webhooks_endpoints import WebhookEndpoints


class TestWebhookEndpoints(unittest.TestCase):

    def setUp(self):
        self.api_key = 'test_api_key'
        self.webhook_endpoints = WebhookEndpoints(api_key=self.api_key)

    @patch('pin_payments.webhooks_endpoints.requests.post')
    def test_create_webhook_endpoint(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {'response': {'token': 'test_token'}}
        mock_post.return_value = mock_response

        response = self.webhook_endpoints.create_webhook_endpoint(url='https://example.org/webhooks/')
        self.assertEqual(response, {'response': {'token': 'test_token'}})
        mock_post.assert_called_once()

    @patch('pin_payments.webhooks_endpoints.requests.get')
    def test_list_webhook_endpoints(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'response': []}
        mock_get.return_value = mock_response

        response = self.webhook_endpoints.list_webhook_endpoints()
        self.assertEqual(response, {'response': []})
        mock_get.assert_called_once()

    @patch('pin_payments.webhooks_endpoints.requests.get')
    def test_get_webhook_endpoint_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'response': {'token': 'test_token'}}
        mock_get.return_value = mock_response

        response = self.webhook_endpoints.get_webhook_endpoint_details(webhook_endpoint_token='test_token')
        self.assertEqual(response, {'response': {'token': 'test_token'}})
