from typing import Optional


# TODO write the module like charges.py

class CustomersAPI:
    def __init__(
            self,
            api_key: str,
    ):
        self.__api_key = api_key

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
    ) -> None:
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
        ...

    def get_customers(
            self
    ) -> None:
        """
        Returns a paginated list of all customers.

        GET /customers

        Example:
        curl https://test-api.pinpayments.com/1/customers -u your-secret-api-key:

        :return: None
        """
        ...

    def get_customers_customer_token(
            self
    ) -> None:
        """
        Returns the details of a customer.

        GET /customers/customer-token

        Example:
        curl https://test-api.pinpayments.com/1/customers/cus_XZg1ULpWaROQCOT5PdwLkQ -u your-secret-api-key:

        :return: None
        """
        ...

    def put_customers_customer_token(
            self,
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
    ) -> None:
        """
        Updates the details of a customer and returns the updated details. You can update the customer’s cards in one of four ways:
        You can use the card[...] parameters to store a new card that will replace the customer’s primary card. The customer’s current primary card will be removed from storage and you will not be able to recover it.
        You can use the card_token parameter to replace the customer’s primary card with a previously stored card. The card token must either be already associated with this customer record or unused. The customer’s current primary card will be removed from storage and you will not be able to recover it.
        You can use the primary_card_token parameter to switch the customer’s primary card to a previously stored card. The card token must either be already associated with this customer record or unused. The current primary card will become a non-primary card of the customer.
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

        :param email: The email address of the customer.
        :param first_name: The customer’s first name.
        :param last_name: The customer’s surname.
        :param phone_number: The customer’s contact number.
        :param company: The company associated with the customer.
        :param notes: Internal notes for the customer.
        :param card: The full details of the payment card to be stored
        :param card_token: The token of the card to be stored, as returned from the cards API or customers API.
        :param primary_card_token: The token of the card to become the customer’s primary card, as returned from the cards API or customers API.
        :return: None
        """
        ...





if __name__ == '__main__':
    customers_api = CustomersAPI()

    # customers_api.post_charges()
    # customers_api.put_charges_charge_token_void()
    # customers_api.put_charges_charge_token_capture()
    # customers_api.get_charges()
    # customers_api.get_charges_search()
    # customers_api.get_charges_charge_token()
    # customers_api.get_charges_verify()
