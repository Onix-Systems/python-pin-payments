from typing import Optional

import requests

from pin_payments.base import Base


class Authorisations(Base):
    """
    The authorisations API allows you to create new payment card authorisations,
    retrieve details of previous authorisations,
    void authorisations, and capture authorised funds.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        """
        Initializes the Authorisations API with an API key and mode.

        :param api_key: The secret API key for authentication.
        :param mode: The mode of operation, either 'live' or 'test' for sandbox testing.
        """
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'authorisations/'

    def create_authorisation(
            self,
            email: str,
            description: str,
            amount: int,
            ip_address: str,
            currency: str = 'AUD',
            card: Optional[dict] = None,
            card_token: Optional[str] = None,
            customer_token: Optional[str] = None,
            reference: Optional[str] = None,
            metadata: Optional[dict] = None
    ) -> dict:
        """
        Creates a new authorisation and returns its details.

        :param email: The email address of the purchaser.
        :param description: A description of the item purchased.
        :param amount: The amount to authorise in the currency’s base unit.
        :param ip_address: The IP address of the person submitting the payment.
        :param currency: The three-character ISO 4217 currency code.
        :param card: The full details of the payment card to be authorised.
        :param card_token: The token of the card to be authorised.
        :param customer_token: The token of the customer to be authorised.
        :param reference: A custom text string for the customer's bank statement.
        :param metadata: Arbitrary key-value data associated with the authorisation.
        :return: A dictionary containing the response data.
        """
        payment_details = [card, card_token, customer_token]
        if sum(detail is not None for detail in payment_details) != 1:
            raise ValueError(
                'Only one of the parameters is required '
                '[card, card_token, customer_token]')

        data = {
            'email': email,
            'description': description,
            'amount': amount,
            'ip_address': ip_address,
            'currency': currency
        }

        if card:
            for key, value in card.items():
                data[f'card[{key}]'] = value
        elif card_token:
            data['card_token'] = card_token
        elif customer_token:
            data['customer_token'] = customer_token

        if reference:
            data['reference'] = reference
        if metadata:
            for key, value in metadata.items():
                data[f'metadata[{key}]'] = value

        response = requests.post(self._base_url, auth=self._api_key, data=data)
        return self._handle_response(
            response=response,
            function_name='create_authorisation',
            required_status_code=201
        )

    def void_authorisation(self, auth_token: str) -> dict:
        """
        Voids a previously created authorisation and returns its details.

        :param auth_token: The token of the authorisation to void.
        :return: A dictionary containing the response data.
        """
        url = f'{self._base_url}{auth_token}/void'
        response = requests.put(url, auth=self._api_key)
        return self._handle_response(
            response=response,
            function_name='void_authorisation',
            required_status_code=200
        )

    def capture_authorisation(self, auth_token: str, amount: int) -> dict:
        """
        Captures the authorised funds and returns details of the charge.

        :param auth_token: The token of the authorisation to capture.
        :param amount: The amount to capture in the currency’s base unit.
        :return: A dictionary containing the response data.
        """
        url = f'{self._base_url}{auth_token}/charges'
        data = {'amount': amount}
        response = requests.post(url, auth=self._api_key, data=data)
        return self._handle_response(
            response=response,
            function_name='capture_authorisation',
            required_status_code=200
        )

    def list_authorisations(self) -> dict:
        """
        Returns a paginated list of all authorisations.

        :return: A dictionary containing the response data.
        """
        response = requests.get(self._base_url, auth=self._api_key)
        return self._handle_response(
            response=response,
            function_name='list_authorisations',
            required_status_code=200
        )

    def get_authorisation_details(self, auth_token: str) -> dict:
        """
        Returns the details of an authorisation.

        :param auth_token: The token of the authorisation to retrieve.
        :return: A dictionary containing the response data.
        """
        url = f'{self._base_url}{auth_token}'
        response = requests.get(url, auth=self._api_key)
        return self._handle_response(
            response=response,
            function_name='get_authorisation_details',
            required_status_code=200
        )
