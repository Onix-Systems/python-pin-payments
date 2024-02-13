from typing import Optional

import requests

from pin_payments.base import Base


class Subscriptions(Base):
    """
    The Subscriptions API allows managing subscriptions against plans,
    including creating new subscriptions, retrieving details of existing subscriptions,
    updating, reactivating, and cancelling subscriptions,
    and fetching subscription ledger entries.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        """
        Initializes the Subscriptions API with an API key and mode.
        :param api_key: The secret API key for authentication.
        :param mode: The mode of operation, 'live' or 'test' for sandbox testing.
        """
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'subscriptions/'

    def create_subscription(
            self,
            plan_token: str,
            customer_token: str,
            include_setup_fee: bool = True
    ) -> dict:
        """
        Activates a new subscription and returns its details.
        :param plan_token: The token of the plan to subscribe to.
        :param customer_token: The token of the customer to be subscribed.
        :param include_setup_fee: Whether the setup fee should be applied.
        :return: A dictionary containing the response data.
        """
        data = {
            'plan_token': plan_token,
            'customer_token': customer_token,
            'include_setup_fee': str(include_setup_fee).lower()
        }
        response = requests.post(f'{self._base_url}', auth=self._auth, data=data)
        return self._handle_response(
            response,
            'create_subscription',
            201
        )

    def list_subscriptions(self) -> dict:
        """
        Returns a paginated list of all subscriptions.
        :return: A dictionary containing the response data.
        """
        response = requests.get(f'{self._base_url}', auth=self._auth)
        return self._handle_response(
            response,
            'list_subscriptions',
            200
        )

    def get_subscription_details(self, sub_token: str) -> dict:
        """
        Returns the details of the subscription identified by subscription token.
        :param sub_token: The token of the subscription.
        :return: A dictionary containing the response data.
        """
        response = requests.get(f'{self._base_url}{sub_token}', auth=self._auth)
        return self._handle_response(
            response,
            'get_subscription_details',
            200
        )

    def update_subscription(
            self,
            sub_token: str,
            card_token: Optional[str] = None
    ) -> dict:
        """
        Updates the card associated with a subscription.
        :param sub_token: The token of the subscription.
        :param card_token: The token of the new card to associate with the subscription.
        :return: A dictionary containing the response data.
        """
        data = {'card_token': card_token} if card_token else {}
        response = requests.put(
            f'{self._base_url}{sub_token}',
            auth=self._auth,
            data=data
        )
        return self._handle_response(
            response,
            'update_subscription',
            200
        )

    def cancel_subscription(self, sub_token: str) -> dict:
        """
        Cancels the subscription identified by subscription token.
        :param sub_token: The token of the subscription.
        :return: A dictionary containing the response data.
        """
        response = requests.delete(f'{self._base_url}{sub_token}', auth=self._auth)
        return self._handle_response(
            response,
            'cancel_subscription',
            200
        )

    def reactivate_subscription(
            self,
            sub_token: str,
            include_setup_fee: bool = True
    ) -> dict:
        """
        Reactivates the subscription identified by subscription token.
        :param sub_token: The token of the subscription.
        :param include_setup_fee: Whether the setup fee should be applied.
        :return: A dictionary containing the response data.
        """
        data = {'include_setup_fee': str(include_setup_fee).lower()}
        response = requests.put(
            f'{self._base_url}{sub_token}/reactivate',
            auth=self._auth,
            data=data
        )
        return self._handle_response(
            response,
            'reactivate_subscription',
            200
        )

    def fetch_subscription_ledger(self, sub_token: str) -> dict:
        """
        Fetches the ledger entries relating to a subscription.
        :param sub_token: The token of the subscription.
        :return: A dictionary containing the response data.
        """
        response = requests.get(f'{self._base_url}{sub_token}/ledger', auth=self._auth)
        return self._handle_response(
            response,
            'fetch_subscription_ledger',
            200
        )


if __name__ == '__main__':
    subscriptions_api = Subscriptions(api_key=..., mode='test')

    res1 = subscriptions_api.create_subscription(
        plan_token='plan_ZyDee4HNeUHFHC4SpM2idg',
        customer_token='cus_XZg1ULpWaROQCOT5PdwLkQ',
        include_setup_fee=False
    )
    print(res1)
