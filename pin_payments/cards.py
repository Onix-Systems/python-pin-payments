import logging
from typing import Optional

import requests

from pin_payments.base import Base


class Cards(Base):
    """
    The cards API allows you to securely store payment card details in exchange for a card token.
    """

    def __init__(
            self,
            api_key: str,
            mode: str = 'live'
    ):
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
        Securely stores a card’s details and returns its token and other information.

        POST /cards

        Example:
        curl https://test-api.pinpayments.com/1/cards -d "publishable_api_key=your-publishable-api-key" \
         -d "number=5520000000000000" \
         -d "expiry_month=05" \
         -d "expiry_year=2025" \
         -d "cvc=123" \
         -d "name=Roland Robot" \
         -d "address_line1=42 Sevenoaks St" \
         -d "address_line2=" \
         -d "address_city=Lathlain" \
         -d "address_postcode=6454" \
         -d "address_state=WA" \
         -d "address_country=Australia"

        :param number: The card number (e.g. 5520000000000000).
        :param expiry_month: The month of expiry (e.g. 12).
        :param expiry_year: The year of expiry (e.g. 2025).
        :param cvc: The card security code (e.g. 123).
        :param name: The name on the card (e.g. Roland Robot).
        :param address_line1: Line 1 of the card’s billing address (e.g. 42 Sevenoaks St).
        :param address_city: The city of the card’s billing address (e.g. Lathlain).
        :param address_country: The country of the card’s billing address.
        Either the full name (e.g. Australia) or the ISO 3166-1 two-letter country code (e.g. AU).
        :param publishable_api_key: Your publishable API key, if requesting from an insecure environment.
        :param address_line2: Line 2 of the card’s billing address (e.g. Apt 1).
        :param address_postcode: The postcode of the card’s billing address (e.g. 6454).
        :param address_state: The state of the card’s billing address (e.g. WA).
        :return: dict
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

        if response.status_code == 201:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}


if __name__ == '__main__':
    charges_api = Cards()
    charges_api.create()
