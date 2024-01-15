import unittest
from unittest.mock import patch, MagicMock

from requests.auth import HTTPBasicAuth

from pin_payments.cards import Cards


class TestCardsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.cards_api = Cards(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.cards_api._api_key, self.api_key)
        self.assertEqual(self.cards_api._base_url, 'https://api.pinpayments.com/1/cards/')
        self.assertEqual(self.cards_api._auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.cards.requests.post')
    def test_create_card_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"token": "card_pIQJKMs93GsCc9vLSLevbw"}
        mock_post.return_value = mock_response

        card_details = {
            "number": 5520000000000000,
            "expiry_month": 5,
            "expiry_year": 2025,
            "cvc": 123,
            "name": "Roland Robot",
            "address_line1": "42 Sevenoaks St",
            "address_city": "Lathlain",
            "address_country": "Australia"
        }

        response = self.cards_api.create(**card_details)

        self.assertEqual(response, {"token": "card_pIQJKMs93GsCc9vLSLevbw"})
        mock_post.assert_called_once()

        expected_data = {
            "number": 5520000000000000,
            "expiry_month": 5,
            "expiry_year": 2025,
            "cvc": 123,
            "name": "Roland Robot",
            "address_line1": "42 Sevenoaks St",
            "address_city": "Lathlain",
            "address_country": "Australia"
        }
        mock_post.assert_called_with(self.cards_api._base_url, auth=self.cards_api._auth, data=expected_data)
