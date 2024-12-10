import requests

from config import get_api_key
from pin_payments.base import Base


class WebhookEndpoints(Base):
    """
    The webhook endpoints API allows you to create and view your webhook endpoints.
    These are URLs that Pin Payments requests when events occur on your account.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'webhook_endpoints/'

    def create_webhook_endpoint(self, url: str) -> dict:
        """
        Creates a new webhook endpoint and returns its details.
        :param url: The destination URL of the webhook endpoint.
        """
        data = {'url': url}
        response = requests.post(self._base_url, auth=self._auth, data=data)
        return self._handle_response(
            response,
            'create_webhook_endpoint',
            201
        )

    def list_webhook_endpoints(self) -> dict:
        """
        Returns a paginated list of all webhook endpoints.
        """
        response = requests.get(self._base_url, auth=self._auth)
        return self._handle_response(
            response,
            'list_webhook_endpoints',
            200
        )

    def get_webhook_endpoint_details(self, webhook_endpoint_token: str) -> dict:
        """
        Returns the details of the specified webhook endpoint.
        :param webhook_endpoint_token: Token of the webhook endpoint.
        """
        url = f"{self._base_url}{webhook_endpoint_token}"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'get_webhook_endpoint_details',
            200
        )

    def delete_webhook_endpoint(self, webhook_endpoint_token: str) -> dict:
        """
        Deletes a webhook endpoint and all of its webhook requests.
        :param webhook_endpoint_token: Token of the webhook endpoint to be deleted.
        """
        url = f"{self._base_url}{webhook_endpoint_token}"
        response = requests.delete(url, auth=self._auth)
        return self._handle_response(
            response,
            'delete_webhook_endpoint',
            204
        )


if __name__ == '__main__':
    webhook_endpoints_api = WebhookEndpoints(api_key=get_api_key(), mode='test')

    new_webhook_url = "https://example.org/webhooks/"
    created_webhook = webhook_endpoints_api.create_webhook_endpoint(url=new_webhook_url)
    print("Created Webhook Endpoint:", created_webhook)

    all_webhook_endpoints = webhook_endpoints_api.list_webhook_endpoints()
    print("All Webhook Endpoints:", all_webhook_endpoints)

    webhook_endpoint_token = "your_webhook_endpoint_token_here"

    webhook_endpoint_details = webhook_endpoints_api.get_webhook_endpoint_details(
        webhook_endpoint_token
    )
    print("Webhook Endpoint Details:", webhook_endpoint_details)

    delete_result = webhook_endpoints_api.delete_webhook_endpoint(webhook_endpoint_token)
    print("Deleted Webhook Endpoint:", delete_result)
