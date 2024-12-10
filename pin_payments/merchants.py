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
    # Access requires a partner API key
    PARTNER_API_KEY = ...
    merchants_api = Merchants(api_key=PARTNER_API_KEY, mode='test')

    contact = {
        "first_name": "Roland",
        "last_name": "Robot",
        "phone_number": "02 9876 5432",
        "email": "roland@pinpayments.com",
        "password": "new-user-password"
    }
    entity = {
        "business_registration_number": "11223491505",
        "full_legal_name": "Roland Robot's coffee robots",
        "address_line_1": "58 Durham Rd",
        "address_line_2": "",
        "address_locality": "Kilsyth",
        "address_region": "VIC",
        "address_postal_code": "3137",
        "address_country_code": "AU"
    }
    business = {
        "trading_name": "Roland Robot's coffee robots",
        "description": "We sell robots that make coffee",
        "typical_product_price": "1000",
        "transactions_per_month": "100",
        "annual_transaction_volume": "1000000",
        "sells_physical_goods": True,
        "average_delivery_days": "14",
        "url": "https://rrcr.net.au"
    }
    bank_account = {
        "name": "RRCR",
        "bsb": "182222",
        "number": "000111111"
    }
    director = {
        "full_name": "Roland Robot",
        "contact_number": "02 9876 5432",
        "date_of_birth": "1984-06-12"
    }
    notes = "This is a test merchant created via API."

    create_response = merchants_api.create(
        contact=contact,
        entity=entity,
        business=business,
        bank_account=bank_account,
        director=director,
        notes=notes
    )
    print("Create Merchant Response:", create_response)

    list_response = merchants_api.list()
    print("List Merchants Response:", list_response)

    merchant_token = 'example-merchant-token'

    details_response = merchants_api.details(merchant_token=merchant_token)
    print("Merchant Details Response:", details_response)

    default_settings_response = merchants_api.default_settings()
    print("Default Settings Response:", default_settings_response)
