from typing import Optional

import requests

from config import get_api_key, get_test_card_dict
from pin_payments.base import Base


class Customers(Base):
    """
    Initializes the Customers object with API key and mode
    :param api_key: The API key for authenticating with the service.
    :param mode: The mode in which the API operates. Default is 'live'.
    """
    def __init__(
            self,
            api_key: str,
            mode: str = 'live'
    ):

        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'customers/'

    def create(
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
        Creates a new customer
        :param email: The customer's email address.
        :param first_name: The customer's first name (optional).
        :param last_name: The customer's last name (optional).
        :param phone_number: The customer's phone number (optional).
        :param company: The customer's company (optional).
        :param notes: Notes related to the customer (optional).
        :param card: Card details to associate with the customer (optional).
        :param card_token: A token representing a pre-existing card to associate with the customer (optional).
        :return: A dictionary containing the customer details.
        :raises ValueError: If both card and card_token are provided.
        """
        if (
                card is not None and card_token is not None
        ):
            raise ValueError('Use only one of [card, card_token]')
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

        response = requests.post(self._base_url, auth=self._auth, data=data)

        return self._handle_response(
            response=response,
            function_name='Customers.create',
            required_status_code=201
        )

    def list(
            self
    ) -> dict:
        """
        Lists all customers
        :return: A dictionary containing the list of customers.
        """
        response = requests.get(self._base_url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Customers.list',
            required_status_code=200
        )

    def details(
            self,
            customer_token: str
    ) -> dict:
        """
        Retrieves the details of a specific customer
        :param customer_token: The unique identifier of the customer.
        :return: A dictionary containing the customer details.
        """
        url = f"{self._base_url}{customer_token}"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Customers.details',
            required_status_code=200
        )

    def update(
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
        Updates the details of an existing customer
        :param customer_token: The unique identifier of the customer to update.
        :param email: The updated email address (optional).
        :param first_name: The updated first name (optional).
        :param last_name: The updated last name (optional).
        :param phone_number: The updated phone number (optional).
        :param company: The updated company (optional).
        :param notes: Updated notes (optional).
        :param card: Updated card details (optional).
        :param card_token: The card token to use (optional).
        :param primary_card_token: The primary card token to update the customer (optional).
        :return: A dictionary containing the updated customer details.
        :raises ValueError: If more than one card-related parameter is provided.
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

        return self._handle_response(
            response=response,
            function_name='Customers.update',
            required_status_code=200
        )

    def delete(
            self,
            customer_token: str
    ) -> dict:
        """
        Deletes a customer
        :param customer_token: The unique identifier of the customer to delete.
        :return: An empty dictionary if the deletion was successful.
        """
        url = f"{self._base_url}{customer_token}"
        response = requests.delete(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Customers.delete',
            required_status_code=204
        )

    def list_charges(
            self,
            customer_token: str
    ) -> dict:
        """
        Lists all cards associated with a specific customer
        :param customer_token: The unique identifier of the customer.
        :return: A dictionary containing the list of cards for the customer.
        """
        url = f"{self._base_url}{customer_token}/charges.rst"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Customers.list_charges',
            required_status_code=200
        )

    def list_cards(
            self,
            customer_token: str
    ) -> dict:

        url = f"{self._base_url}{customer_token}/cards"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Customers.list_cards',
            required_status_code=200
        )

    def create_card(
            self,
            customer_token: str,
            number: Optional[int] = None,
            expiry_month: Optional[int] = None,
            expiry_year: Optional[int] = None,
            cvc: Optional[int] = None,
            name: Optional[str] = None,
            address_line1: Optional[str] = None,
            address_city: Optional[str] = None,
            address_country: Optional[str] = None,
            # true optional values
            publishable_api_key: Optional[str] = None,
            address_line2: Optional[str] = None,
            address_postcode: Optional[int] = None,
            address_state: Optional[str] = None,
            # The other way, if you’ve already created a card through the cards API,
            # is to send the card token using this parameter:
            card_token: Optional[str] = None
    ) -> dict:
        """
        Creates a new card for a customer
        :param customer_token: The unique identifier of the customer.
        :param number: The card number (optional).
        :param expiry_month: The expiry month of the card (optional).
        :param expiry_year: The expiry year of the card (optional).
        :param cvc: The card's CVC code (optional).
        :param name: The name on the card (optional).
        :param address_line1: The first line of the address (optional).
        :param address_city: The city of the address (optional).
        :param address_country: The country of the address (optional).
        :param publishable_api_key: The publishable API key (optional).
        :param address_line2: The second line of the address (optional).
        :param address_postcode: The postcode of the address (optional).
        :param address_state: The state of the address (optional).
        :param card_token: A token for an existing card to associate (optional).
        :return: A dictionary containing the card details.
        :raises ValueError: If both card_token and card parameters are provided.
        :raises ValueError: If required card details are missing.
        """
        url = f"{self._base_url}/{customer_token}/cards"

        if card_token and any(
                [number, expiry_month, expiry_year, cvc, name, address_line1, address_city, address_country]
        ):
            raise ValueError("If card_token is passed, other card parameters cannot be passed.")

        if card_token:
            data = {"card_token": card_token}
        elif None in [number, expiry_month, expiry_year, cvc, name, address_line1, address_city, address_country]:
            raise ValueError(
                "You should pass every parameter "
                "[number, expiry_month, expiry_year, cvc, name, address_line1, address_city, address_country]."
            )
        else:
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
            if address_line2:
                data['address_line2'] = address_line2
            if address_postcode:
                data['address_postcode'] = address_postcode
            if address_state:
                data['address_state'] = address_state
            if publishable_api_key:
                data['publishable_api_key'] = publishable_api_key

        response = requests.post(url, auth=self._auth, data=data)

        return self._handle_response(
            response=response,
            function_name='Customers.create_card',
            required_status_code=201
        )

    def delete_card(
            self,
            customer_token: str,
            card_token: str,
    ) -> dict:
        """
        Deletes a card associated with a customer
        :param customer_token: The unique identifier of the customer.
        :param card_token: The token of the card to delete.
        :return: An empty dictionary if the deletion was successful.
        """
        url = f"{self._base_url}{customer_token}/cards/{card_token}"
        response = requests.delete(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Customers.delete_card',
            required_status_code=204
        )

    def list_subscriptions(
            self,
            customer_token: str
    ) -> dict:
        """
        Lists all subscriptions for a specific customer
        :param customer_token: The unique identifier of the customer.
        :return: A dictionary containing the list of subscriptions for the customer.
        """
        url = f"{self._base_url}{customer_token}/subscriptions"
        response = requests.get(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Customers.list_subscriptions',
            required_status_code=200
        )

    def delete_subscriptions(
            self,
            customer_token: str,
            subscription_token: str
    ) -> dict:
        """
        Deletes a subscription for a specific customer
        :param customer_token: The unique identifier of the customer.
        :param subscription_token: The unique identifier of the subscription to delete.
        :return: An empty dictionary if the deletion was successful.
        """
        url = f"{self._base_url}{customer_token}/subscriptions/{subscription_token}"
        response = requests.delete(url, auth=self._auth)

        return self._handle_response(
            response=response,
            function_name='Customers.delete_subscriptions',
            required_status_code=200
        )


if __name__ == '__main__':
    customers_api = Customers(api_key=get_api_key(), mode='test')

    email = 'test@gmail.com'
    card_details = get_test_card_dict()
    customer_creation_response = customers_api.create(email=email, card=card_details)
    print("Customer Creation Response:", customer_creation_response)

    customer_token = customer_creation_response['response']['token']

    customers_list = customers_api.list()
    print("Customers List:", customers_list)

    customer_details = customers_api.details(customer_token)
    print("Customer Details:", customer_details)

    update_response = customers_api.update(customer_token=customer_token, card=card_details)
    print("Update Response:", update_response)

    charges_list = customers_api.list_charges(customer_token)
    print("Charges List:", charges_list)

    cards_list = customers_api.list_cards(customer_token)
    print("Cards List:", cards_list)

    additional_card_response = customers_api.create_card(customer_token=customer_token, **card_details)
    print("Additional Card Creation Response:", additional_card_response)
    additional_card_token = additional_card_response['response']['token']

    subscriptions_list = customers_api.list_subscriptions(customer_token)
    print("Subscriptions List:", subscriptions_list)

    delete_subscription_response = customers_api.delete_subscriptions(customer_token, 'subscription_token')
    print("Delete Subscription Response:", delete_subscription_response)

    delete_customer_response = customers_api.delete(customer_token)
    print("Delete Customer Response:", delete_customer_response)

    delete_card_response = customers_api.delete_card(customer_token, additional_card_token)
    print("Delete Card Response:", delete_card_response)
