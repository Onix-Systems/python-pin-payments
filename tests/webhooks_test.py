import unittest
from unittest.mock import patch, MagicMock

from pin_payments.webhooks import Webhooks


class TestWebhooksAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.webhooks_api = Webhooks(api_key=self.api_key)

    @patch('pin_payments.webhooks.requests.get')
    def test_list_webhooks_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"webhooks": []}
        mock_get.return_value = mock_response

        response = self.webhooks_api.list_webhooks()

        self.assertEqual(response, {"webhooks": []})
        mock_get.assert_called_once()

    @patch('pin_payments.webhooks.requests.get')
    def test_get_webhook_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"webhook": {"token": "whr_123"}}
        mock_get.return_value = mock_response

        response = self.webhooks_api.get_webhook_details("whr_123")

        self.assertEqual(response, {"webhook": {"token": "whr_123"}})
        mock_get.assert_called_once_with(
            f"{self.webhooks_api._base_url}whr_123", auth=self.webhooks_api._auth
        )

    @patch('pin_payments.webhooks.requests.put')
    def test_replay_webhook_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Webhook replayed successfully."}
        mock_put.return_value = mock_response

        response = self.webhooks_api.replay_webhook("whr_123")

        self.assertEqual(response, {"message": "Webhook replayed successfully."})
        mock_put.assert_called_once_with(
            f"{self.webhooks_api._base_url}whr_123/replay", auth=self.webhooks_api._auth
        )
