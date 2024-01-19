from typing import Optional

import requests
from pin_payments.base import Base


class Recipients(Base):
    """
    The Recipients API allows you to store transfer recipient details and retrieve a token
    that you can safely store in your application. You can send funds to recipients using
    the transfer API.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'recipients/'

    def create(
            self,
            email: str,
            name: Optional[str] = None,
            bank_account: Optional[dict] = None,
            bank_account_token: Optional[str] = None
    ) -> dict:
        """
        Creates a new recipient and returns its details.

        :param email: The email address of the recipient.
        :param name: A name for this recipient.
        :param bank_account: The full details of the bank account to be stored.
        :param bank_account_token: The token of the bank account to be stored.
        :return: dict
        """
        if bank_account and bank_account_token:
            raise ValueError('Use only one of [bank_account, bank_account_token]')

        data = {
            "email": email,
            "name": name,
            "bank_account": bank_account,
            "bank_account_token": bank_account_token
        }

        data = {k: v for k, v in data.items() if v is not None}
        response = requests.post(self._base_url, auth=self._auth, data=data)
        return self._handle_response(
            response,
            'Recipients.create',
            201
        )

    def list(self) -> dict:
        """
        Returns a paginated list of all recipients.

        :return: dict
        """
        response = requests.get(self._base_url, auth=self._auth)
        return self._handle_response(
            response,
            'Recipients.list',
            200
        )

    def get_details(self, recipient_token: str) -> dict:
        """
        Returns the details of a recipient.

        :param recipient_token: Your recipient token.
        :return: dict
        """
        url = f"{self._base_url}{recipient_token}"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'Recipients.get_details',
            200
        )

    def update(
            self,
            recipient_token: str,
            email: Optional[str] = None,
            bank_account: Optional[dict] = None,
            bank_account_token: Optional[str] = None
    ) -> dict:
        """
        Updates the details of a recipient and returns its new details.

        :param recipient_token: Your recipient token.
        :param email: The email address of the recipient.
        :param bank_account: The full details of the bank account to be stored.
        :param bank_account_token: The token of the bank account to be stored.
        :return: dict
        """
        data = {
            "email": email,
            "bank_account": bank_account,
            "bank_account_token": bank_account_token
        }

        data = {k: v for k, v in data.items() if v is not None}
        url = f"{self._base_url}{recipient_token}"
        response = requests.put(url, auth=self._auth, data=data)
        return self._handle_response(
            response,
            'Recipients.update',
            200
        )

    def list_transfers(self, recipient_token: str) -> dict:
        """
        Returns a paginated list of a recipient’s transfers.

        :param recipient_token: Your recipient token.
        :return: dict
        """
        url = f"{self._base_url}{recipient_token}/transfers"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'Recipients.list_transfers',
            200
        )


if __name__ == '__main__':
    recipients_api = Recipients()
    recipients_api.create()
    recipients_api.list()
    recipients_api.get_details()
    recipients_api.update()
    recipients_api.list_transfers()
