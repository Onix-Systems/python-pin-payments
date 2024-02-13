import os

from dotenv import load_dotenv


def get_api_key() -> str:
    load_dotenv()
    return os.getenv('API_KEY')


def get_test_card_dict() -> dict:
    return {
        'number': '5520000000000000',
        'expiry_month': '05',
        'expiry_year': '2025',
        'cvc': '123',
        'name': 'Roland Robot',
        'address_line1': '42 Sevenoaks St',
        'address_city': 'Lathlain',
        'address_postcode': '6454',
        'address_state': 'WA',
        'address_country': 'Australia',
    }
