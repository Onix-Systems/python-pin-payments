import requests

from config import get_api_key
from pin_payments.base import Base


class Deposits(Base):
    """
    A class for interacting with the deposits API.
    This class provides methods for listing deposits and retrieving details
    for a specific deposit.
    :param api_key: The API key to authenticate the requests.
    :param mode: The environment mode to use (default is 'live'). Can be 'live' or 'test'.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        """
        Initializes the Deposits class with the provided API key and mode
        :param api_key: The API key to authenticate the requests.
        :param mode: The environment mode to use (default is 'live'). Can be 'live' or 'test'.
        """
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'deposits/'

    def list(self) -> dict:
        """
        Lists all deposits
        This method sends a GET request to retrieve all deposits
        :returns: A dictionary containing the list of deposits.
        :raises: Raises an exception if the response code is not 200.
        """
        response = requests.get(self._base_url, auth=self._auth)
        return self._handle_response(
            response,
            'Deposits.list',
            200
        )

    def details(self, deposit_token: str) -> dict:
        """
        Retrieves the details of a specific deposit
        This method sends a GET request to retrieve details for a deposit based
        on the provided deposit token
        :param deposit_token: The unique identifier of the deposit.
        :returns: A dictionary containing the details of the deposit.
        :raises: Raises an exception if the response code is not 200.
        """
        url = f"{self._base_url}{deposit_token}"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'Deposits.details',
            200
        )


if __name__ == '__main__':
    deposits_api = Deposits(api_key=get_api_key(), mode='test')

    deposits_list_response = deposits_api.list()
    print("List of Deposits Response:", deposits_list_response)

    deposit_token = 'example-deposit-token'

    deposit_details_response = deposits_api.details(deposit_token=deposit_token)
    print("Deposit Details Response:", deposit_details_response)
