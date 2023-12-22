import unittest
from unittest.mock import patch, MagicMock
from pin_payments.customers import Customers
from requests.auth import HTTPBasicAuth


class TestCustomersAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.customers_api = Customers(api_key=self.api_key)

    def test_init(self):
        self.assertEqual(self.customers_api._CustomersAPI__api_key, self.api_key)
        self.assertEqual(self.customers_api._CustomersAPI__base_url, 'https://api.pinpayments.com/1/customers/')
        self.assertEqual(self.customers_api._CustomersAPI__auth, HTTPBasicAuth(self.api_key, ''))

    @patch('pin_payments.customers.requests.post')
    def test_post_customers_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.customers_api.post_customers(email='test@example.com')

        self.assertEqual(response, {"success": True})
        mock_post.assert_called_once()

    @patch('pin_payments.customers.requests.post')
    def test_post_customers_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        response = self.customers_api.post_customers(email='invalid@example.com')

        self.assertIn("error", response)
        mock_post.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"customers": []}
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers()

        self.assertEqual(response, {"customers": []})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers()

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"customer": {"token": "cus_token"}}
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers_customer_token(customer_token='cus_token')

        self.assertEqual(response, {"customer": {"token": "cus_token"}})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers_customer_token(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.put')
    def test_put_customers_customer_token_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"customer": {"token": "cus_token"}}
        mock_put.return_value = mock_response

        response = self.customers_api.put_customers_customer_token(
            customer_token='cus_token',
            email='updated@example.com'
        )

        self.assertEqual(response, {"customer": {"token": "cus_token"}})
        mock_put.assert_called_once()

    @patch('pin_payments.customers.requests.put')
    def test_put_customers_customer_token_failure(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_put.return_value = mock_response

        response = self.customers_api.put_customers_customer_token(
            customer_token='invalid_token',
            email='updated@example.com'
        )

        self.assertIn("error", response)
        mock_put.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_customers_customer_token(customer_token='cus_token')

        self.assertEqual(response, {"message": "Customer deleted successfully."})
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_failure(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_customers_customer_token(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_charges_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"charges": []}
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers_customer_token_charges(customer_token='cus_token')

        self.assertEqual(response, {"charges": []})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_charges_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers_customer_token_charges(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_cards_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"cards": []}
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers_customer_token_cards(customer_token='cus_token')

        self.assertEqual(response, {"cards": []})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_cards_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers_customer_token_cards(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.post')
    def test_post_customers_customer_token_cards_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"card": {"token": "card_token"}}
        mock_post.return_value = mock_response

        response = self.customers_api.post_customers_customer_token_cards(
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
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        response = self.customers_api.post_customers_customer_token_cards(
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
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_customers_customer_token_cards_card_token(
            customer_token='cus_token',
            card_token='card_token'
        )

        self.assertEqual(response, {"message": "Card deleted successfully."})
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_cards_card_token_failure(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_customers_customer_token_cards_card_token(
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

        response = self.customers_api.get_customers_customer_token_subscriptions(customer_token='cus_token')

        self.assertEqual(response, {"subscriptions": []})
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.get')
    def test_get_customers_customer_token_subscriptions_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        response = self.customers_api.get_customers_customer_token_subscriptions(customer_token='invalid_token')

        self.assertIn("error", response)
        mock_get.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_subscriptions_sub_token_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Subscription cancelled successfully."}
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_customers_customer_token_subscriptions_sub_token(
            customer_token='cus_token',
            subscription_token='sub_token'
        )

        self.assertEqual(response, {"message": "Subscription cancelled successfully."})
        mock_delete.assert_called_once()

    @patch('pin_payments.customers.requests.delete')
    def test_delete_customers_customer_token_subscriptions_sub_token_failure(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_delete.return_value = mock_response

        response = self.customers_api.delete_customers_customer_token_subscriptions_sub_token(
            customer_token='invalid_token',
            subscription_token='invalid_sub_token'
        )

        self.assertIn("error", response)
        mock_delete.assert_called_once()
