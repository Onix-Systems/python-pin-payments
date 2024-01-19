from typing import Optional

import requests
from pin_payments.base import Base


class Transfers(Base):
    """
    The transfers API allows you to send money to Australian bank accounts
    and retrieve details of previous transfers.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'transfers/'

    def create(
            self,
            description: str,
            amount: int,
            currency: str,
            recipient: str
    ) -> dict:
        """
        Creates a new transfer and returns its details.

        :param description: A description of the amount being transferred.
        :param amount: The amount to transfer in the currency’s base unit.
        :param currency: The currency to transfer.
        :param recipient: The recipient’s token or 'self' for an own account.
        :return: dict
        """
        data = {
            "description": description,
            "amount": amount,
            "currency": currency,
            "recipient": recipient
        }
        response = requests.post(
            self._base_url,
            auth=self._auth,
            data=data
        )
        return self._handle_response(
            response,
            'Transfers.create',
            201
        )

    def list(self) -> dict:
        """
        Returns a paginated list of all transfers.

        :return: dict
        """
        response = requests.get(self._base_url, auth=self._auth)
        return self._handle_response(
            response,
            'Transfers.list',
            200
        )

    def search(
            self,
            query: Optional[str] = None,
            start_date: Optional[str] = None,
            end_date: Optional[str] = None,
            sort: Optional[str] = None,
            direction: Optional[int] = None
    ) -> dict:
        """
        Returns a paginated list of transfers matching the search criteria.

        :param query: Search query.
        :param start_date: Start date for filtering.
        :param end_date: End date for filtering.
        :param sort: Field to sort by.
        :param direction: Sort direction.
        :return: dict
        """
        params = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "sort": sort,
            "direction": direction
        }
        response = requests.get(
            f"{self._base_url}search",
            auth=self._auth, params=params
        )
        return self._handle_response(
            response,
            'Transfers.search',
            200
        )

    def details(self, transfer_token: str) -> dict:
        """
        Returns the details of the specified transfer.

        :param transfer_token: Token of the transfer.
        :return: dict
        """
        url = f"{self._base_url}{transfer_token}"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'Transfers.details',
            200
        )

    def line_items(self, transfer_token: str) -> dict:
        """
        Returns a paginated list of line items associated with the specified transfer.

        :param transfer_token: Token of the transfer.
        :return: dict
        """
        url = f"{self._base_url}{transfer_token}/line_items"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'Transfers.line_items',
            200
        )


if __name__ == '__main__':
    transfers_api = Transfers()
    transfers_api.create()
    transfers_api.list()
    transfers_api.search()
    transfers_api.details()
    transfers_api.line_items()
