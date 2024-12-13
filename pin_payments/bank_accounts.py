from typing import Optional

import requests

from config import get_api_key
from pin_payments.base import Base


class BankAccounts(Base):
    """
    The Bank Accounts API allows for securely storing bank account
    details in exchange for a bank account token.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'bank_accounts/'

    def create(
            self,
            name: str,
            bsb: str,
            number: str,
            publishable_api_key: Optional[str] = None
    ) -> dict:
        """
        Creates a bank account token and returns its details.
        :param name: The account holder's name.
        :param bsb: The BSB code of the bank account.
        :param number: The account number of the bank account.
        :param publishable_api_key: Publishable API key for insecure environments.
        :return: dict
        """
        data = {
            "name": name,
            "bsb": bsb,
            "number": number
        }
        if publishable_api_key:
            data['publishable_api_key'] = publishable_api_key

        response = requests.post(
            self._base_url,
            auth=self._auth,
            data=data
        )
        return self._handle_response(
            response,
            'BankAccounts.create',
            201
        )


if __name__ == '__main__':
    bank_accounts_api = BankAccounts(api_key=get_api_key(), mode='test')

    bank_account_response = bank_accounts_api.create(
        name="John Doe",
        bsb="123-456",
        number="123456789"
    )

    print("Bank Account Token Creation Response:", bank_account_response)
