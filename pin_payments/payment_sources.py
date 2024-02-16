from typing import Optional

import requests

from config import get_api_key, get_test_card_dict
from pin_payments.base import Base


class PaymentSources(Base):
    """
    The Payment Sources API allows you to securely store payment source details
    in exchange for a payment source token.
    This token can then be used to create a single charge with the charges API.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        """
        Initializes the Payment Sources API client with the given API key and mode.

        :param api_key: The API key to authenticate requests.
        :param mode: Either 'live' or 'test' to set the environment.
        """
        super().__init__(api_key, mode)
        self._base_url += 'payment_sources/'

    def create_payment_source(
            self,
            source_type: str,
            source: dict,
            publishable_api_key: Optional[str] = None
    ) -> dict:
        """
        Securely stores a payment source’s details and returns its token and other information.

        :param source_type: The type of payment source to create
        (e.g., 'card', 'applepay', 'googlepay', 'network_token').
        :param source: A dictionary containing the details of the payment source.
        :param publishable_api_key: Optional;
        Your publishable API key if requesting from an insecure environment
        like a web browser or mobile app.
        :return: A dictionary with the payment source token and other details.
        """
        if source_type not in ('card', 'applepay', 'googlepay', 'network_token'):
            raise ValueError('Use only one of [card, applepay, googlepay, network_token]')

        data = {
            'type': source_type,
            'source': source
        }

        if publishable_api_key:
            data['publishable_api_key'] = publishable_api_key

        response = requests.post(self._base_url, auth=self._auth, json=data)
        return self._handle_response(
            response,
            'create_payment_source',
            201
        )


if __name__ == '__main__':
    payment_sources_api = PaymentSources(api_key=get_api_key(), mode='test')

    payment_source = payment_sources_api.create_payment_source(
        source_type='card',
        source=get_test_card_dict()
    )
    print(payment_source)
