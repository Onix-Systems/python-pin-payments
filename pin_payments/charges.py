import logging
from typing import Optional
from urllib.parse import urlencode

import requests

from config import get_api_key, get_test_card_dict
from pin_payments.base import Base


class Charges(Base):
    """
    A class to interact with the Charges API for processing payment card charges.
    This class provides methods to create, void, capture, list, search, and verify charges.
    :param api_key: The API key for authentication.
    :param mode: The mode of operation, either 'live' or 'test'. Default is 'live'.
    """

    def __init__(
            self,
            api_key: str,
            mode: str = 'live'
    ):
        """
        Initializes the Charges class with the provided API key and mode
        :param api_key: The API key for authentication.
        :param mode: The mode of operation, either 'live' or 'test'. Default is 'live'.
        """
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'charges/'

    def create(
            self,
            email: str,
            description: str,
            amount: int,
            ip_address: str,
            currency: Optional[str] = None,
            capture: Optional[bool] = None,
            reference: Optional[str] = None,
            metadata: Optional[dict] = None,
            three_d_secure: Optional[dict] = None,
            platform_adjustment: Optional[dict] = None,
            # need to use one of the following
            card: Optional[dict] = None,
            card_token: Optional[str] = None,
            payment_source_token: Optional[str] = None,
            customer_token: Optional[str] = None
    ) -> dict:
        """
        Creates a new charge and returns its details
        This method requires one of the following parameters to be provided:
        card, card_token, payment_source_token, or customer_token
        :param email: The email address of the purchaser.
        :param description: A description of the item purchased.
        :param amount: The amount to charge in the currency’s base unit.
        :param ip_address: The IP address of the person submitting the payment.
        :param currency: The three-character ISO 4217 currency code (optional).
        :param capture: Whether to immediately capture the charge (optional).
        :param reference: A custom text string for the customer's bank statement (optional).
        :param metadata: Arbitrary key-value data associated with the charge (optional).
        :param three_d_secure: Information required to enable 3D Secure on payments (optional).
        :param platform_adjustment: Specify an amount to withhold from the merchant entitlement (optional).
        :param card: The full details of the payment card to be charged (optional).
        :param card_token: The token of the card to be charged (optional).
        :param payment_source_token: The token of the payment source to be charged (optional).
        :param customer_token: The token of the customer to be charged (optional).
        :return: A dictionary containing the response details or an error message.
        :raises ValueError: If more than one payment detail parameter is provided.
        """
        payment_details = [card, card_token, payment_source_token, customer_token]
        if sum(detail is not None for detail in payment_details) != 1:
            raise ValueError(
                'Only one of the parameters is required '
                '[card, card_token, payment_source_token, customer_token]')

        data = {
            "email": email,
            "description": description,
            "amount": amount,
            "ip_address": ip_address,
            "currency": currency,
            "capture": capture,
            "reference": reference
        }

        if card:
            for key, value in card.items():
                data[f'card[{key}]'] = value
        elif card_token:
            data['card_token'] = card_token
        elif payment_source_token:
            data['payment_source_token'] = payment_source_token
        elif customer_token:
            data['customer_token'] = customer_token

        if metadata:
            for key, value in metadata.items():
                data[f'metadata[{key}]'] = value
        if three_d_secure:
            data['three_d_secure'] = three_d_secure
        if platform_adjustment:
            data['platform_adjustment'] = platform_adjustment

        data = {k: v for k, v in data.items() if v is not None}

        response = requests.post(self._base_url, auth=self._auth, data=data)

        if response.status_code in [201, 202]:
            return response.json()
        error_message = f"Error in Charges.create: {response.status_code}, {response.text}"
        logging.error(error_message)
        return {"error": error_message}

    def void(
            self,
            charge_token: str
    ) -> dict:
        """
        Voids a previously authorized charge
        :param charge_token: The token of the charge to be voided.
        :return: A dictionary containing the void details.
        """
        url = f"{self._base_url}{charge_token}/void"
        response = requests.put(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Charges.void',
            required_status_code=200
        )

    def capture(
            self,
            charge_token: str
    ) -> dict:
        """
        Captures a previously authorized charge
        :param charge_token: The token of the charge to be captured.
        :return: A dictionary containing the capture details.
        """
        url = f"{self._base_url}{charge_token}/capture"
        response = requests.put(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Charges.capture',
            required_status_code=201
        )

    def list(self) -> dict:
        """
        Returns a paginated list of all charges
        :return: A dictionary containing the list of charges.
        """
        response = requests.get(self._base_url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Charges.list',
            required_status_code=200
        )

    def search(
            self,
            query: Optional[str] = None,
            start_date: Optional[str] = None,
            end_date: Optional[str] = None,
            sort: Optional[str] = None,
            direction: Optional[int] = None,
    ) -> dict:
        """
        Searches for charges based on the provided criteria
        :param query: Return only charges whose fields match the query (optional).
        :param start_date: Return only charges created on or after this date (optional).
        :param end_date: Return only charges created before this date (optional).
        :param sort: The field used to sort the charges (optional).
        :param direction: The direction in which to sort the charges (optional).
        :return: A dictionary containing the search results.
        """
        params = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "sort": sort,
            "direction": direction
        }

        filtered_params = {k: v for k, v in params.items() if v is not None}
        url = f"{self._base_url}search?" + urlencode(filtered_params)
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Charges.search',
            required_status_code=200
        )

    def charge(
            self,
            charge_token: str
    ) -> dict:
        """
        Retrieves the details of a specific charge
        :param charge_token: The token of the charge to retrieve.
        :return: A dictionary containing the charge details.
        """
        url = f"{self._base_url}{charge_token}/"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Charges.charge',
            required_status_code=200
        )

    def verify(
            self,
            session_token: str
    ) -> dict:
        """
        Verifies the result of a 3D Secure enabled charge
        :param session_token: The session token for verification.
        :return: A dictionary containing the verification details.
        """
        url = f"{self._base_url}verify?session_token={session_token}"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Charges.verify',
            required_status_code=200
        )


if __name__ == '__main__':
    charges_api = Charges(api_key=get_api_key(), mode='test')

    charge_creation_response = charges_api.create(
        email='test@gmail.com',
        description='Test Charge',
        amount=400,
        ip_address='192.0.2.1',
        card=get_test_card_dict()
    )
    print("Charge Creation Response:", charge_creation_response)

    charge_token = charge_creation_response['response']['token']

    charges_list = charges_api.list()
    print("Charges List:", charges_list)

    search_results = charges_api.search()
    print("Search Results:", search_results)

    charge_details = charges_api.charge(charge_token)
    print("Charge Details:", charge_details)

    void_response = charges_api.void(charge_token)
    print("Void Response:", void_response)

    capture_response = charges_api.capture(charge_token)
    print("Capture Response:", capture_response)

    # Assuming a 3D Secure session token is needed and available
    # Uncomment and modify the next lines according to your actual 3D Secure handling
    # secure_token = "YOUR_3D_SECURE_SESSION_TOKEN_HERE"
    # verify_response = charges_api.verify(charge_token, secure_token)
    # print("Verify Response:", verify_response)
