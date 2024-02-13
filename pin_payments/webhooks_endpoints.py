import requests

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
        POST /webhook_endpoints
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
        GET /webhook_endpoints
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
        GET /webhook_endpoints/<webhook_endpoint_token>
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
        DELETE /webhook_endpoints/<webhook_endpoint_token>
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
    webhook_endpoints_api = WebhookEndpoints()
