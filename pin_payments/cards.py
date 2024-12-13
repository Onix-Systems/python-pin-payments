from typing import Optional

import requests

from config import get_api_key, get_test_card_dict
from pin_payments.base import Base


class Cards(Base):
    """
    The cards API allows you to securely store payment card details in exchange for a card token.
    This class provides functionality for interacting with the cards API, including storing
    payment card details, retrieving information about stored cards, and managing card-related
    operations.
    """

    def __init__(
            self,
            api_key: str,
            mode: str = 'live'
    ):
        """
        Initializes the Cards API client
        :param api_key: The API key used for authentication.
        :param mode: The mode of operation, either 'live' or 'test'. Defaults to 'live'.
        """
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'cards/'

    def create(
            self,
            number: int,
            expiry_month: int,
            expiry_year: int,
            cvc: int,
            name: str,
            address_line1: str,
            address_city: str,
            address_country: str,
            publishable_api_key: Optional[str] = None,
            address_line2: Optional[str] = None,
            address_postcode: Optional[int] = None,
            address_state: Optional[str] = None,
    ) -> dict:
        """
        Creates a new payment card and stores it securely
        This method securely stores the card details provided and returns a card token that can be
        used for future transactions
        :param number: The card number (16 digits).
        :param expiry_month: The expiry month of the card (1-12).
        :param expiry_year: The expiry year of the card (4 digits).
        :param cvc: The card's CVC (3 digits).
        :param name: The cardholder's name.
        :param address_line1: The first line of the cardholder's address.
        :param address_city: The city of the cardholder's address.
        :param address_country: The country of the cardholder's address.
        :param publishable_api_key: An optional publishable API key (if applicable).
        :param address_line2: An optional second line of the cardholder's address.
        :param address_postcode: An optional postcode of the cardholder's address.
        :param address_state: An optional state of the cardholder's address
        :return: A dictionary containing the response data from the API, including the card token
        :raises ValueError: If required parameters are missing or invalid.
        """
        data = {
            "number": number,
            "expiry_month": expiry_month,
            "expiry_year": expiry_year,
            "cvc": cvc,
            "name": name,
            "address_line1": address_line1,
            "address_city": address_city,
            "address_country": address_country,
            "publishable_api_key": publishable_api_key,
            "address_line2": address_line2,
            "address_postcode": address_postcode,
            "address_state": address_state
        }
        data = {k: v for k, v in data.items() if v is not None}

        response = requests.post(self._base_url, auth=self._auth, data=data)

        return self._handle_response(
            response=response,
            function_name='Cards.create',
            required_status_code=201
        )


if __name__ == '__main__':
    cards_api = Cards(api_key=get_api_key(), mode='test')
    card_details = get_test_card_dict()

    new_card_response = cards_api.create(
        number=card_details["number"],
        expiry_month=card_details["expiry_month"],
        expiry_year=card_details["expiry_year"],
        cvc=card_details["cvc"],
        name=card_details["name"],
        address_line1=card_details["address_line1"],
        address_city=card_details["address_city"],
        address_country=card_details["address_country"]
    )
    print("New card response:", new_card_response)
