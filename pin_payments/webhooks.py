import requests

from config import get_api_key
from pin_payments.base import Base


class Webhooks(Base):
    """
    The webhooks API allows you to view and replay webhooks—requests
    that have been sent to your webhook endpoints.
    When an event occurs, Pin Payments creates a webhook record and
    sends a web request to each of your endpoints.
    Replaying a webhook causes Pin Payments to request the URL again.
    It will not repeat other webhook requests for the same event.
    Replaying a webhook will reset the error information recorded during
    the original request and record any new errors that occur during the replay.
    Webhooks are only guaranteed to be stored for 30 days after they are created.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'webhooks/'

    def list_webhooks(self) -> dict:
        """
        Returns a paginated list of all webhooks.
        GET /webhooks
        """
        response = requests.get(self._base_url, auth=self._auth)
        return self._handle_response(
            response,
            'list_webhooks',
            200
        )

    def get_webhook_details(self, webhook_token: str) -> dict:
        """
        Returns the details of a webhook.
        GET /webhooks/<webhook_token>
        :param webhook_token: Token of the webhook.
        """
        url = f"{self._base_url}{webhook_token}"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'get_webhook_details',
            200
        )

    def replay_webhook(self, webhook_token: str) -> dict:
        """
        Replays a webhook.
        PUT /webhooks/<webhook_token>/replay
        :param webhook_token: Token of the webhook to be replayed.
        """
        url = f"{self._base_url}{webhook_token}/replay"
        response = requests.put(url, auth=self._auth)
        return self._handle_response(
            response,
            'replay_webhook',
            200
        )


if __name__ == '__main__':
    webhooks_api = Webhooks(api_key=get_api_key(), mode='test')

    all_webhooks = webhooks_api.list_webhooks()
    print("All Webhooks:", all_webhooks)

    webhook_token = "your_webhook_token_here"

    webhook_details = webhooks_api.get_webhook_details(webhook_token)
    print("Webhook Details:", webhook_details)

    replayed_webhook = webhooks_api.replay_webhook(webhook_token)
    print("Replayed Webhook:", replayed_webhook)
