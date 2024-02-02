from typing import Optional

import requests

from pin_payments.base import Base


class Merchants(Base):
    """
    The merchants API allows you to examine merchants you have referred to us.
    Access requires a partner API key, which is available to approved partners.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'merchants/'

    def create(
            self,
            contact: dict,
            entity: dict,
            business: dict,
            bank_account: dict,
            director: dict,
            notes: Optional[str] = None
    ) -> dict:
        """
        Creates a new referred merchant in the system and returns a confirmation.

        POST /merchants

        :param contact: Personal details of the user logging into the merchant entity account.
        :param entity: Legal operating details of the merchant entity.
        :param business: Business details of the merchant entity.
        :param bank_account: Full details of the bank account for fund settlement.
        :param director: Details of a person legally responsible for the merchant entity.
        :param notes: Additional information to support the merchant’s application.
        :return: dict
        """
        data = {
            'contact': contact,
            'entity': entity,
            'business': business,
            'bank_account': bank_account,
            'director': director
        }
        if notes is not None:
            data['notes'] = notes
        response = requests.post(self._base_url, auth=self._auth, json=data)
        return self._handle_response(
            response,
            'Merchants.create',
            201
        )

    def list(self) -> dict:
        """
        Returns a paginated list of all the merchants referred by you.

        GET /merchants

        :return: dict
        """
        response = requests.get(self._base_url, auth=self._auth)
        return self._handle_response(
            response,
            'Merchants.list',
            200
        )

    def details(self, merchant_token: str) -> dict:
        """
        Returns the details of a specified merchant referred by you.

        GET /merchants/merchant-token

        :param merchant_token: Token of the merchant
        :return: dict
        """
        url = f"{self._base_url}{merchant_token}"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'Merchants.details',
            200
        )

    def default_settings(self) -> dict:
        """
        Returns the default settings that will be applied to new merchants referred by you.

        GET /merchants/default_settings

        :return: dict
        """
        url = f"{self._base_url}default_settings"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'Merchants.default_settings',
            200
        )


if __name__ == '__main__':
    merchants_api = Merchants()
