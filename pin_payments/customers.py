import logging
from typing import Optional

import requests

from pin_payments.base import Base


class Customers(Base):
    """
    The customers API allows you to store a customer’s email address and payment card details.
    A customer can then be used with the charges API to create multiple charges over time.
    A customer can have multiple cards.
    At any given time, one will be considered the customer’s primary card.
    The card property of a customer object represents this primary card.
    Each card object has a primary property, which is true for a customer’s primary card and false for its other cards.
    """

    def __init__(
            self,
            api_key: str,
            mode: str = 'live'
    ):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'customers/'

    def post_customers(
            self,
            email: str,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            phone_number: Optional[str] = None,
            company: Optional[str] = None,
            notes: Optional[str] = None,
            # need to use one of the following
            card: Optional[dict] = None,
            card_token: Optional[str] = None
    ) -> dict:
        """
        Creates a new customer and returns its details.

        POST /customers

        Example:
        curl https://test-api.pinpayments.com/1/customers -u your-secret-api-key: \
         -d "email=roland@pinpayments.com" \
         -d "first_name=Roland" \
         -d "last_name=Robot" \
         -d "phone_number=1300 364 800" \
         -d "company=Pin Payments" \
         -d "notes=Account manager at Pin Payments" \
         -d "card[number]=5520000000000000" \
         -d "card[expiry_month]=05" \
         -d "card[expiry_year]=2024" \
         -d "card[cvc]=123" \
         -d "card[name]=Roland Robot" \
         -d "card[address_line1]=42 Sevenoaks St" \
         -d "card[address_line2]=" \
         -d "card[address_city]=Lathlain" \
         -d "card[address_postcode]=6454" \
         -d "card[address_state]=WA" \
         -d "card[address_country]=Australia"

        :param email: The email address of the customer.
        :param first_name: The customer’s first name.
        :param last_name: The customer’s surname.
        :param phone_number: The customer’s contact number.
        :param company: The company associated with the customer.
        :param notes: Internal notes for the customer.
        :param card: The full details of the payment card to be stored
        :param card_token: The token of the card to be stored, as returned from the cards API or customers API.
        :return: None
        """
        if (
                card is not None and card_token is not None
        ):
            raise ValueError('Use only one of [card, card_token]')
        url = self._base_url
        data = {'email': email}

        # Optional parameters
        if first_name:
            data['first_name'] = first_name
        if last_name:
            data['last_name'] = last_name
        if phone_number:
            data['phone_number'] = phone_number
        if company:
            data['company'] = company
        if notes:
            data['notes'] = notes

        # Card details
        if card:
            for key, value in card.items():
                data[f'card[{key}]'] = value
        elif card_token:
            data['card_token'] = card_token

        response = requests.post(url, auth=self._auth, data=data)

        if response.status_code == 201:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def get_customers(
            self
    ) -> dict:
        """
        Returns a paginated list of all customers.

        GET /customers

        Example:
        curl https://test-api.pinpayments.com/1/customers -u your-secret-api-key:

        :return: None
        """
        url = self._base_url
        response = requests.get(url, auth=self._auth)

        if response.status_code == 200:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def get_customers_customer_token(
            self,
            customer_token: str
    ) -> dict:
        """
        Returns the details of a customer.

        GET /customers/customer-token

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ -u your-secret-api-key:

        :param customer_token: Token of the customer
        :return: None
        """
        url = f"{self._base_url}{customer_token}"
        response = requests.get(url, auth=self._auth)

        if response.status_code == 200:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def put_customers_customer_token(
            self,
            customer_token: str,
            email: Optional[str] = None,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            phone_number: Optional[str] = None,
            company: Optional[str] = None,
            notes: Optional[str] = None,
            # need to use one of the following
            card: Optional[dict] = None,
            card_token: Optional[str] = None,
            primary_card_token: Optional[str] = None,
    ) -> dict:
        """
        Updates the details of a customer and returns the updated details.
        You can update the customer’s cards in one of four ways:
        You can use the card[...] parameters to store a new card that will replace the
        customer’s primary card. The customer’s current primary card will be removed from
        storage and you will not be able to recover it.
        You can use the card_token parameter to replace the customer’s primary card
        with a previously stored card. The card token must either be already associated
        with this customer record or unused. The customer’s current primary card will be
        removed from storage and you will not be able to recover it.
        You can use the primary_card_token parameter to switch the customer’s
        primary card to a previously stored card.
        The card token must either be already associated with this customer
        record or unused. The current primary card will become a non-primary card
        of the customer.
        You can use none of the above parameters. The customer’s cards will not change.
        In addition, you can update the customer’s email address and contact details.

        PUT /customers/customer-token

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ -u your-secret-api-key: -X PUT \
         -d "email=roland@pinpayments.com" \
         -d "first_name=Roland" \
         -d "last_name=Robot" \
         -d "phone_number=1300 364 800" \
         -d "company=Pin Payments" \
         -d "notes=Account manager at Pin Payments" \
         -d "card[number]=5520000000000000" \
         -d "card[expiry_month]=05" \
         -d "card[expiry_year]=2024" \
         -d "card[cvc]=123" \
         -d "card[name]=Roland Robot" \
         -d "card[address_line1]=42 Sevenoaks St" \
         -d "card[address_line2]=" \
         -d "card[address_city]=Lathlain" \
         -d "card[address_postcode]=6454" \
         -d "card[address_state]=WA" \
         -d "card[address_country]=Australia"

        :param customer_token: Token of the customer.
        :param email: The email address of the customer.
        :param first_name: The customer’s first name.
        :param last_name: The customer’s surname.
        :param phone_number: The customer’s contact number.
        :param company: The company associated with the customer.
        :param notes: Internal notes for the customer.
        :param card: The full details of the payment card to be stored
        :param card_token: The token of the card to be stored, as returned from the cards API or customers API.
        :param primary_card_token: The token of the card to become the customer’s
        primary card, as returned from the cards API or customers API.
        :return: None
        """
        if (
                card is not None and card_token is not None and primary_card_token is not None
        ):
            raise ValueError('Use only one of [card, card_token, primary_card_token]')
        url = f"{self._base_url}{customer_token}"
        data = {}

        if email:
            data['email'] = email
        if first_name:
            data['first_name'] = first_name
        if last_name:
            data['last_name'] = last_name
        if phone_number:
            data['phone_number'] = phone_number
        if company:
            data['company'] = company
        if notes:
            data['notes'] = notes

        if card:
            for key, value in card.items():
                data[f'card[{key}]'] = value
        if card_token:
            data['card_token'] = card_token
        if primary_card_token:
            data['primary_card_token'] = primary_card_token

        response = requests.put(url, auth=self._auth, data=data)

        if response.status_code == 200:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def delete_customers_customer_token(
            self,
            customer_token: str
    ) -> dict:
        """
        Deletes a customer and all of its cards. You will not be able to recover them.

        DELETE /customers/customer-token

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ -u your-secret-api-key: -X DELETE

        :param customer_token: Token of the customer.
        :return: None
        """
        url = f"{self._base_url}{customer_token}"
        response = requests.delete(url, auth=self._auth)

        if response.status_code == 204:
            return {"message": "Customer deleted successfully."}
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def get_customers_customer_token_charges(
            self,
            customer_token: str
    ) -> dict:
        """
        Returns a paginated list of a customer’s charges.

        GET /customers/customer-token/charges

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ/charges -u your-secret-api-key:

        :param customer_token: Token of the customer.
        :return: None
        """
        url = f"{self._base_url}{customer_token}/charges"
        response = requests.get(url, auth=self._auth)

        if response.status_code == 200:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def get_customers_customer_token_cards(
            self,
            customer_token: str
    ) -> dict:
        """
        Returns a paginated list of a customer’s cards.

        GET /customers/customer-token/charges

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ/cards -u your-secret-api-key:

        :param customer_token: Token of the customer.
        :return: None
        """
        url = f"{self._base_url}{customer_token}/cards"
        response = requests.get(url, auth=self._auth)

        if response.status_code == 200:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def post_customers_customer_token_cards(
            self,
            customer_token: str,
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
            # The other way, if you’ve already created a card through the cards API,
            # is to send the card token using this parameter:
            card_token: Optional[str] = None
    ) -> dict:
        """
        Creates an additional card for the specified customer and returns its details.
        The customer’s primary card will not be changed by this operation.
        There are two ways to call this.
        One way is to specify the card details directly using these parameters:

        POST /customers/customer-token/cards

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ/cards -u your-secret-api-key: \
         -d "number=5520000000000000" \
         -d "expiry_month=05" \
         -d "expiry_year=2024" \
         -d "cvc=123" \
         -d "name=Roland Robot" \
         -d "address_line1=42 Sevenoaks St" \
         -d "address_line2=" \
         -d "address_city=Lathlain" \
         -d "address_postcode=6454" \
         -d "address_state=WA" \
         -d "address_country=Australia"

        :param customer_token: Token of the customer.
        :param number: The card number (e.g. 5520000000000000).
        :param expiry_month: The month of expiry (e.g. 12).
        :param expiry_year: The year of expiry (e.g. 2024).
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
        :param card_token: The token of the card to be associated with the customer,
        as returned from the cards API or customers API.
        :return: None
        """
        url = f"{self._base_url}{customer_token}/cards"
        data = {
            "number": number,
            "expiry_month": expiry_month,
            "expiry_year": expiry_year,
            "cvc": cvc,
            "name": name,
            "address_line1": address_line1,
            "address_city": address_city,
            "address_country": address_country
        }

        if publishable_api_key:
            data['publishable_api_key'] = publishable_api_key
        if address_line2:
            data['address_line2'] = address_line2
        if address_postcode:
            data['address_postcode'] = address_postcode
        if address_state:
            data['address_state'] = address_state
        if card_token:
            data['card_token'] = card_token

        response = requests.post(url, auth=self._auth, data=data)

        if response.status_code == 201:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def delete_customers_customer_token_cards_card_token(
            self,
            customer_token: str,
            card_token: str,
    ) -> dict:
        """
        Deletes a customer’s non-primary card. You will not be able to recover it.

        DELETE /customers/customer-token/cards/card-token

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ/
        cards/card_ZFThCjFi7wCNkopytxQVKA -u your-secret-api-key: -X DELETE

        :param customer_token: Token of the customer.
        :param card_token: Card token of the customer.
        :return: None
        """
        url = f"{self._base_url}{customer_token}/cards/{card_token}"
        response = requests.delete(url, auth=self._auth)

        if response.status_code == 204:
            return {"message": "Card deleted successfully."}
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def get_customers_customer_token_subscriptions(
            self,
            customer_token: str
    ) -> dict:
        """
        Retrieves the specified customer's subscriptions.

        GET /customers/customer-token/subscriptions

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ/
        subscriptions -u your-secret-api-key:

        :param customer_token: Token of the customer.
        :return: None
        """
        url = f"{self._base_url}{customer_token}/subscriptions"
        response = requests.get(url, auth=self._auth)

        if response.status_code == 200:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}

    def delete_customers_customer_token_subscriptions_sub_token(
            self,
            customer_token: str,
            subscription_token: str
    ) -> dict:
        """
        Cancels the subscription identified by subscription token.
        Subscriptions can only be cancelled if they are in trial or active state.

        DELETE /customers/customer-token/subscriptions/sub-token

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ/
        subscriptions/sub_bZWXhTzHooKpk9FZjQfzqQ -u your-secret-api-key: -X DELETE

        :param customer_token: Token of the customer.
        :param subscription_token: Subscription token of the customer.
        :return: None
        """
        url = f"{self._base_url}{customer_token}/subscriptions/{subscription_token}"
        response = requests.delete(url, auth=self._auth)

        if response.status_code == 200:
            return response.json()
        logging.error(f"Error: {response.status_code}, {response.text}")
        return {"error": f"Error: {response.status_code}, {response.text}"}


if __name__ == '__main__':
    customers_api = Customers()
