from typing import Optional

import requests

from config import get_api_key
from pin_payments.base import Base


class Refunds(Base):
    """
    A class to handle refund operations for payments.
    This class interacts with an API to manage and retrieve information about refunds.
    :param api_key: The API key used for authentication.
    :type api_key: str
    :param mode: The mode of the API (either 'live' or 'test'). Defaults to 'live'.
    :type mode: str
    """

    def __init__(
            self,
            api_key: str,
            mode: str = 'live'
    ):
        """
        Initializes the Refunds class with the provided API key and mode
        :param api_key: The API key used for authentication.
        :type api_key: str
        :param mode: The mode of the API ('live' or 'test'). Defaults to 'live'.
        :type mode: str
        """
        super().__init__(api_key=api_key, mode=mode)

    def list(
            self
    ) -> dict:
        """
        Retrieves a list of all refunds
        Makes a GET request to the refunds endpoint of the API
        :return: A dictionary containing the list of refunds.
        :rtype: dic
        :raises Exception: If the request fails or returns an error response.
        """
        url = f"{self._base_url}refunds/"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Refunds.list',
            required_status_code=200
        )

    def details(
            self,
            refund_token: str
    ) -> dict:
        """
        Retrieves details of a specific refund using the refund token
        :param refund_token: The token of the refund to retrieve details for.
        :type refund_token: str
        :return: A dictionary containing the details of the specified refund.
        :rtype: dic
        :raises Exception: If the request fails or returns an error response.
        """
        url = f"{self._base_url}refunds/{refund_token}"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Refunds.details',
            required_status_code=200
        )

    def create_refund(
            self,
            charge_token: str,
            amount: Optional[int] = None
    ) -> dict:
        """
        Creates a refund for a given charge token
        :param charge_token: The charge token associated with the refund.
        :type charge_token: str
        :param amount: The amount to be refunded, if provided. Defaults to None.
        :type amount: Optional[int]
        :return: A dictionary containing the details of the created refund.
        :rtype: dict
        :raises Exception: If the request fails or returns an error response.
        """
        url = f"{self._base_url}charges/{charge_token}/refunds"
        data = {}

        if amount is not None:
            data['amount'] = amount

        response = requests.post(url, auth=self._auth, data=data)

        return self._handle_response(
            response=response,
            function_name='Refunds.create_refund',
            required_status_code=201
        )

    def list_charge(
            self,
            charge_token: str
    ) -> dict:
        """
        Retrieves a list of refunds for a specific charge
        :param charge_token: The charge token for which refunds are being retrieved.
        :type charge_token: str
        :return: A dictionary containing the list of refunds for the specified charge.
        :rtype: dic
        :raises Exception: If the request fails or returns an error response.
        """
        url = f"{self._base_url}charges/{charge_token}/refunds"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Refunds.list_charge',
            required_status_code=200
        )


if __name__ == '__main__':
    refunds_api = Refunds(api_key=get_api_key(), mode="test")

    all_refunds = refunds_api.list()
    print("All Refunds:", all_refunds)

    refund_token = 'refund_token_example'
    refund_details = refunds_api.details(refund_token=refund_token)
    print(f"Details of Refund {refund_token}:", refund_details)

    charge_token_for_refund = "your_charge_token"
    refund_amount = 100

    refund_creation_result = refunds_api.create_refund(charge_token=charge_token_for_refund, amount=refund_amount)
    print("Refund Creation Result:", refund_creation_result)

    refunds_for_charge = refunds_api.list_charge(charge_token=charge_token_for_refund)
    print(f"All Refunds for Charge {charge_token_for_refund}:", refunds_for_charge)
