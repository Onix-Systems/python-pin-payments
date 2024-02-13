import io
import unittest
from unittest.mock import patch, MagicMock

from pin_payments.files import Files


class TestFilesAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.files_api = Files(api_key=self.api_key, mode='test')

    @patch('pin_payments.files.requests.post')
    def test_upload_file_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": {
                "token": "file_M3wowEURfIpSQI6xCEoamQ",
                "purpose": "dispute_evidence",
                # Additional response fields...
            }
        }
        mock_post.return_value = mock_response

        mock_file = io.BytesIO(b'This is a test file')
        mock_file.name = 'test_file.jpeg'

        with patch('pin_payments.files.open', return_value=mock_file, create=True):
            response = self.files_api.upload_file(
                '~/Documents/cat.jpeg',
                'dispute_evidence'
            )

        self.assertIn("response", response)
        self.assertEqual(response["response"]["purpose"], "dispute_evidence")
        mock_post.assert_called_once()

    @patch('pin_payments.files.requests.get')
    def test_get_file_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": {
                "token": "file_M3wowEURfIpSQI6xCEoamQ",
                "original_filename": "cat.jpeg",
                # Additional response fields...
            }
        }
        mock_get.return_value = mock_response

        file_token = 'file_M3wowEURfIpSQI6xCEoamQ'
        response = self.files_api.get_file_details(file_token)

        self.assertIn("response", response)
        self.assertEqual(response["response"]["token"], file_token)
        mock_get.assert_called_once_with(
            f'{self.files_api._base_url}{file_token}',
            auth=self.files_api._auth
        )

    @patch('pin_payments.files.requests.delete')
    def test_delete_file_success(self, mock_delete):
        # Mock the response of the DELETE request
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_response.json.return_value = {}  # Simulate .json() returning an empty dictionary

        mock_delete.return_value = mock_response

        file_token = 'file_M3wowEURfIpSQI6xCEoamQ'
        self.files_api.delete_file(file_token)
        mock_delete.assert_called_once_with(
            f'{self.files_api._base_url}{file_token}',
            auth=self.files_api._auth
        )
