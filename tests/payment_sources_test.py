import unittest
from unittest.mock import patch, MagicMock

from pin_payments.payment_sources import PaymentSources


class TestPaymentSourcesAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.mode = 'test'
        self.payment_sources_api = PaymentSources(self.api_key, self.mode)

    @patch('pin_payments.payment_sources.requests.post')
    def test_create_payment_source_card_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "response": {
                "token": "ps_38KhC82RhpupmeV4pqw6cw",
                "type": "card",
                "source": {
                    "token": "card_BXQoEjTRxEEAdBz59D--zw"
                }
            }
        }
        mock_post.return_value = mock_response

        source = {
            "number": "5520000000000000",
            "expiry_month": "05",
            "expiry_year": "2025",
            "cvc": "123",
            "name": "Roland Robot",
            "address_line1": "42 Sevenoaks St",
            "address_city": "Lathlain",
            "address_postcode": "6454",
            "address_state": "WA",
            "address_country": "Australia"
        }

        result = self.payment_sources_api.create_payment_source("card", source)
        self.assertEqual(result['response']['token'], "ps_38KhC82RhpupmeV4pqw6cw")

    @patch('pin_payments.payment_sources.requests.post')
    def test_create_payment_source_applepay_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "response": {
                "token": "ps_9hXlCIqqClQAElKT_dw2Pw",
                "type": "applepay",
                "source": {
                    "token": "card_2wBUaxkiwRXT7ElyynUrOQ"
                }
            }
        }
        mock_post.return_value = mock_response

        source = {
            "data": "applepay_data",
            "signature": "applepay_signature",
            "header": {
                "publicKeyHash": "applepay_publicKeyHash",
                "ephemeralPublicKey": "applepay_ephemeralPublicKey",
                "transactionId": "applepay_transactionId"
            },
            "version": "EC_v1"
        }

        result = self.payment_sources_api.create_payment_source("applepay", source)
        self.assertEqual(result['response']['token'], "ps_9hXlCIqqClQAElKT_dw2Pw")

    @patch('pin_payments.payment_sources.requests.post')
    def test_create_payment_source_googlepay_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "response": {
                "token": "ps_UKOm94HHNcYliozFVfpdTw",
                "type": "googlepay",
                "source": {
                    "token": "card_BJC5kA-rP9QesNJu8P6_kw"
                }
            }
        }
        mock_post.return_value = mock_response

        source = {
            "protocolVersion": "ECv2",
            "signature": "googlepay_signature",
            "intermediateSigningKey": {
                "signedKey": "googlepay_signedKey",
                "signatures": ["googlepay_signature1"]
            },
            "signedMessage": "googlepay_signedMessage"
        }

        result = self.payment_sources_api.create_payment_source(
            "googlepay",
            source
        )
        self.assertEqual(result['response']['token'], "ps_UKOm94HHNcYliozFVfpdTw")

    @patch('pin_payments.payment_sources.requests.post')
    def test_create_payment_source_network_token_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "response": {
                "token": "ps_MV7zVxpamEriVlUVLLAHWg",
                "type": "network_token",
                "source": {
                    "token": "card_RZriFDPF3JKAKEb_ICS2eg"
                }
            }
        }
        mock_post.return_value = mock_response

        source = {
            "number": "5520000000000000",
            "network_type": "googlepay",
            "expiry_month": "05",
            "expiry_year": "2025",
            "eci": "06",
            "cryptogram": "cryptogram_value"
        }

        result = self.payment_sources_api.create_payment_source(
            "network_token",
            source
        )
        self.assertEqual(
            result['response']['token'],
            "ps_MV7zVxpamEriVlUVLLAHWg"
        )
