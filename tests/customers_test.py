import unittest
from unittest.mock import patch, MagicMock

from requests.auth import HTTPBasicAuth

from pin_payments.customers import Customers

BAD_REQUEST_TEXT = "Bad Request"


class TestCustomersAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.customers_api = Customers(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.customers_api._api_key, self.api_key)
        self.assertEqual(self.customers_api._base_url, 'https://api.pinpayments.com/1/customers/')
        self.assertEqual(self.customers_api._auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.customers.requests.post')
    def test_post_customers_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.customers_api.create(email='test@example.com')

        self.assertEqual(response, {"success": True})
        mock_post.assert_called_once()

    @patch('pin_payments.customers.requests.post')
    def test_post_customers_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_post.return_value = mock_response

        response = self.customers_api.create(email='invalid@example.com')

        self.assertIn("error", response)
        mock_post.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"customers": []}
        mock_get.return_value = mock_response

        response = self.customers_api.list()

        self.assertEqual(response, {"customers": []})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.customers_api.list()

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"customer": {"token": "cus_token"}}
        mock_get.return_value = mock_response

        response = self.customers_api.details(customer_token='cus_token')

        self.assertEqual(response, {"customer": {"token": "cus_token"}})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.customers_api.details(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.put')
    def test_put_customers_customer_token_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"customer": {"token": "cus_token"}}
        mock_put.return_value = mock_response

        response = self.customers_api.update(
            customer_token='cus_token',
            email='updated@example.com'
        )

        self.assertEqual(response, {"customer": {"token": "cus_token"}})
        mock_put.assert_called_once()

    @patch('pin_payments.customers.requests.put')
    def test_put_customers_customer_token_failure(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_put.return_value = mock_response

        response = self.customers_api.update(
            customer_token='invalid_token',
            email='updated@example.com'
        )

        self.assertIn("error", response)
        mock_put.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_response.json.return_value = {}
        mock_delete.return_value = mock_response

        response = self.customers_api.delete(customer_token='cus_token')

        self.assertEqual(response, {})
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_failure(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_delete.return_value = mock_response

        response = self.customers_api.delete(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_charges_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"charges.rst": []}
        mock_get.return_value = mock_response

        response = self.customers_api.list_charges(customer_token='cus_token')

        self.assertEqual(response, {"charges.rst": []})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_charges_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.customers_api.list_charges(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_cards_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"cards": []}
        mock_get.return_value = mock_response

        response = self.customers_api.list_cards(customer_token='cus_token')

        self.assertEqual(response, {"cards": []})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_cards_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.customers_api.list_cards(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.post')
    def test_post_customers_customer_token_cards_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"card": {"token": "card_token"}}
        mock_post.return_value = mock_response

        response = self.customers_api.create_card(
            customer_token='cus_token',
            number=5520000000000000,
            expiry_month=5,
            expiry_year=2024,
            cvc=123,
            name='Test User',
            address_line1='123 Test Street',
            address_city='Test City',
            address_country='Test Country'
        )

        self.assertEqual(response, {"card": {"token": "card_token"}})
        mock_post.assert_called_once()

    @patch('pin_payments.customers.requests.post')
    def test_post_customers_customer_token_cards_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_post.return_value = mock_response

        response = self.customers_api.create_card(
            customer_token='invalid_token',
            number=5520000000000000,
            expiry_month=5,
            expiry_year=2024,
            cvc=123,
            name='Test User',
            address_line1='123 Test Street',
            address_city='Test City',
            address_country='Test Country'
        )

        self.assertIn("error", response)
        mock_post.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_cards_card_token_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_response.json.return_value = {}
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_card(
            customer_token='cus_token',
            card_token='card_token'
        )

        self.assertEqual(response, {})
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_cards_card_token_failure(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_card(
            customer_token='invalid_token',
            card_token='invalid_card_token'
        )

        self.assertIn("error", response)
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_subscriptions_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"subscriptions": []}
        mock_get.return_value = mock_response

        response = self.customers_api.list_subscriptions(customer_token='cus_token')

        self.assertEqual(response, {"subscriptions": []})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_subscriptions_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_get.return_value = mock_response

        response = self.customers_api.list_subscriptions(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_subscriptions_sub_token_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Subscription cancelled successfully."}
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_subscriptions(
            customer_token='cus_token',
            subscription_token='sub_token'
        )

        self.assertEqual(response, {"message": "Subscription cancelled successfully."})
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_subscriptions_sub_token_failure(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = BAD_REQUEST_TEXT
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_subscriptions(
            customer_token='invalid_token',
            subscription_token='invalid_sub_token'
        )

        self.assertIn("error", response)
        mock_delete.assert_called_once()
