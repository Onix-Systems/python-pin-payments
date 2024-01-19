import requests
from pin_payments.base import Base


class Balance(Base):
    """
    The Balance API allows you to see the current balance of funds in your Pin Payments account.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'balance/'

    def detail(self) -> dict:
        """
        Returns the current balance of the Pin Payments account.

        :return: dict
        """
        response = requests.get(self._base_url, auth=self._auth)
        return self._handle_response(
            response,
            'Balance.get_balance',
            200
        )


if __name__ == '__main__':
    balance_api = Balance()
    balance_api.detail()
