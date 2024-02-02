import unittest
from unittest.mock import patch, MagicMock

from requests.auth import HTTPBasicAuth

from pin_payments.disputes import Disputes


class TestDisputesAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.disputes_api = Disputes(api_key=self.api_key)

    @patch('pin_payments.disputes.requests.get')
    def test_list_disputes(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"disputes": []})
        response = self.disputes_api.list_disputes()
        self.assertEqual(response, {"disputes": []})

    @patch('pin_payments.disputes.requests.get')
    def test_search_disputes(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"disputes": []})
        response = self.disputes_api.search_disputes(query="test")
        self.assertEqual(response, {"disputes": []})
        mock_get.assert_called_with(
            f"{self.disputes_api._base_url}search",
            auth=HTTPBasicAuth(self.api_key, ''),
            params={'query': 'test', 'direction': 1}
        )

    @patch('pin_payments.disputes.requests.get')
    def test_get_dispute_details(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"detail": "detail_info"})
        response = self.disputes_api.get_dispute_details(dispute_token="token123")
        self.assertEqual(response, {"detail": "detail_info"})
        mock_get.assert_called_with(
            f"{self.disputes_api._base_url}token123",
            auth=HTTPBasicAuth(self.api_key, '')
        )

    @patch('pin_payments.disputes.requests.get')
    def test_get_dispute_activity(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"activity": "activity_info"})
        response = self.disputes_api.get_dispute_activity(dispute_token="token123")
        self.assertEqual(response, {"activity": "activity_info"})
        mock_get.assert_called_with(
            f"{self.disputes_api._base_url}token123/activity",
            auth=HTTPBasicAuth(self.api_key, '')
        )

    @patch('pin_payments.disputes.requests.get')
    def test_get_dispute_evidence(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"evidence": "evidence_info"})
        response = self.disputes_api.get_dispute_evidence(dispute_token="token123")
        self.assertEqual(response, {"evidence": "evidence_info"})
        mock_get.assert_called_with(
            f"{self.disputes_api._base_url}token123/evidence",
            auth=HTTPBasicAuth(self.api_key, '')
        )

    @patch('pin_payments.disputes.requests.put')
    def test_update_dispute_evidence(self, mock_put):
        mock_put.return_value = MagicMock(status_code=200, json=lambda: {"updated": "updated_info"})
        response = self.disputes_api.update_dispute_evidence(dispute_token="token123", evidence_data={"key": "value"})
        self.assertEqual(response, {"updated": "updated_info"})
        mock_put.assert_called_with(
            f"{self.disputes_api._base_url}token123/evidence",
            auth=HTTPBasicAuth(self.api_key, ''),
            json={"key": "value"}
        )

    @patch('pin_payments.disputes.requests.post')
    def test_submit_dispute_evidence(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"submitted": "submitted_info"})
        response = self.disputes_api.submit_dispute_evidence(dispute_token="token123")
        self.assertEqual(response, {"submitted": "submitted_info"})
        mock_post.assert_called_with(
            f"{self.disputes_api._base_url}token123/evidence",
            auth=HTTPBasicAuth(self.api_key, '')
        )

    @patch('pin_payments.disputes.requests.post')
    def test_accept_dispute(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"accepted": "accepted_info"})
        response = self.disputes_api.accept_dispute(dispute_token="token123")
        self.assertEqual(response, {"accepted": "accepted_info"})
        mock_post.assert_called_with(
            f"{self.disputes_api._base_url}token123/accept",
            auth=HTTPBasicAuth(self.api_key, '')
        )
