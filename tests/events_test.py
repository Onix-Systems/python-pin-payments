import unittest
from unittest.mock import patch, MagicMock

from pin_payments.events import Events


class TestEventsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.events_api = Events(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.events_api._api_key, self.api_key)
        self.assertTrue(self.events_api._base_url.endswith('events/'))

    @patch('pin_payments.events.requests.get')
    def test_list_events_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": []}
        mock_get.return_value = mock_response

        response = self.events_api.list()

        self.assertEqual(response, {"response": []})
        mock_get.assert_called_once()

    @patch('pin_payments.events.requests.get')
    def test_list_events_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.events_api.list()

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.events.requests.get')
    def test_event_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": {"token": "evt_12K4fafROQsdI5PdwLkX"}}
        mock_get.return_value = mock_response

        response = self.events_api.details(event_token='evt_12K4fafROQsdI5PdwLkX')

        self.assertEqual(response, {"response": {"token": "evt_12K4fafROQsdI5PdwLkX"}})
        mock_get.assert_called_once_with(
            f"{self.events_api._base_url}evt_12K4fafROQsdI5PdwLkX",
            auth=self.events_api._auth
        )

    @patch('pin_payments.events.requests.get')
    def test_event_details_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_get.return_value = mock_response

        response = self.events_api.details(event_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once_with(
            f"{self.events_api._base_url}invalid_token",
            auth=self.events_api._auth
        )
