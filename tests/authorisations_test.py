import unittest
from unittest.mock import patch, MagicMock

from pin_payments.authorisations import Authorisations


class TestAuthorisationsAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.mode = 'test'
        self.authorisations_api = Authorisations(api_key=self.api_key, mode=self.mode)

    @patch('pin_payments.authorisations.requests.post')
    def test_create_authorisation_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.authorisations_api.create_authorisation(
            email='test@example.com',
            description='Test Authorisation',
            amount=100,
            card_token='test_token',
            ip_address='127.0.0.1'
        )

        self.assertTrue(response['success'])
        mock_post.assert_called_once()

    @patch('pin_payments.authorisations.requests.put')
    def test_void_authorisation_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_put.return_value = mock_response

        response = self.authorisations_api.void_authorisation(auth_token='auth_token')

        self.assertTrue(response['success'])
        mock_put.assert_called_once()

    @patch('pin_payments.authorisations.requests.post')
    def test_capture_authorisation_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.authorisations_api.capture_authorisation(auth_token='auth_token', amount=50)

        self.assertTrue(response['success'])
        mock_post.assert_called_once()

    @patch('pin_payments.authorisations.requests.get')
    def test_list_authorisations_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"authorisations": []}
        mock_get.return_value = mock_response

        response = self.authorisations_api.list_authorisations()

        self.assertIsInstance(response['authorisations'], list)
        mock_get.assert_called_once()

    @patch('pin_payments.authorisations.requests.get')
    def test_get_authorisation_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_get.return_value = mock_response

        response = self.authorisations_api.get_authorisation_details(auth_token='auth_token')

        self.assertTrue(response['success'])
        mock_get.assert_called_once()
