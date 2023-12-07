from typing import Optional


# TODO write the module like charges.py

class RefundsAPI:
    def __init__(
            self,
            api_key: str,
    ):
        self.__api_key = api_key

    def post_charges(
            self,
            email: str,
            description: str,
            amount: int,
            ip_address: str,
            currency: Optional[str] = None,
            capture: Optional[bool] = None,
            reference: Optional[str] = None,
            metadata: Optional[dict] = None,
            three_d_secure: Optional[dict] = None,
            platform_adjustment: Optional[dict] = None,
            # need to use one of the following
            card: Optional[dict] = None,
            card_token: Optional[str] = None,
            payment_source_token: Optional[str] = None,
            customer_token: Optional[str] = None,
    ) -> None:
        """
        Creates a new charge and returns its details. This may be a long-running request.

        POST /charges

        Example:
        curl https://test-api.pinpayments.com/1/charges -u your-secret-api-key: \
        -d "amount=400" \
        -d "currency=AUD" \
        -d "description=test charge" \
        -d "email=roland@pinpayments.com" \
        -d "ip_address=203.192.1.172" \
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
        -d "card[address_country]=Australia" \
        -d "metadata[OrderNumber]=123456" \
        -d "metadata[CustomerName]=Roland Robot"

        :param email: The email address of the purchaser.
        :param description: A description of the item purchased (e.g. 500g of single origin beans).
        :param amount: The amount to charge in the currency’s base unit (e.g. cents for AUD, yen for JPY). There is a minimum charge amount for each currency; refer to the documentation on supported currencies.
        :param ip_address: The IP address of the person submitting the payment.
        :param currency: The three-character ISO 4217 currency code of one of our supported currencies, e.g. AUD or USD. Default value is AUD.
        :param capture: Whether to immediately capture the charge (true or false). If false, we will attempt to create an authorisation; if this is successful, you can capture at a later time. Authorised charges automatically expire after seven days. Default value is true.
        :param reference: A custom text string which will be displayed in place of the default descriptor on the customer's bank statement.
        :param metadata: Arbitrary key-value data to be associated with the charge.
        :param three_d_secure: Information required to enable 3D Secure on payments.
        :param platform_adjustment: Specify an amount to withhold from the merchant entitlement to collect as revenue for your platform.
        :param card: The full details of the payment card to be charged
        :param card_token: The token of the card to be charged, as returned from the cards API or customers API.
        :param payment_source_token: The token of the payment source to be charged, as returned from the payment_sources API.
        :param customer_token: The token of the customer to be charged, as returned from the customers API.
        :return: None
        """
        ...

    def put_charges_charge_token_void(self) -> None:
        """
        Voids a previously authorised charge and returns its details.
        This will return the reserved funds to the cardholder, and capture will no longer be possible.

        PUT /charges/charge-token/void

        Example:
        curl https://test-api.pinpayments.com/1/charges/ch_lfUYEBK14zotCTykezJkfg/void -u your-secret-api-key: -X PUT

        :return: None
        """
        ...

    def put_charges_charge_token_capture(self) -> None:
        """
        Captures a previously authorised charge and returns its details.
        Currently, you can only capture the full amount that was originally authorised.

        PUT /charges/charge-token/capture

        Example:
        curl https://test-api.pinpayments.com/1/charges/ch_lfUYEBK14zotCTykezJkfg/capture -u your-secret-api-key: -X PUT

        :return: None
        """
        ...

    def get_charges(self) -> None:
        """
        Returns a paginated list of all charges.

        GET /charges

        Example:
        curl https://test-api.pinpayments.com/1/charges -u your-secret-api-key:

        :return: None
        """
        ...

    def get_charges_search(
            self,
            query: Optional[str] = None,
            start_date: Optional[str] = None,
            end_date: Optional[str] = None,
            sort: Optional[str] = None,
            direction: Optional[int] = None,
    ) -> None:
        """
        Returns a paginated list of charges matching the search criteria.

        GET /charges/search

        Example:
        curl https://test-api.pinpayments.com/1/charges/search -u your-secret-api-key: -X GET -d "query=test%20charge"

        :param query: Return only charges whose fields match the query. Fields covered include description, email, metadata, cardholder name, currency, amount (exact), charge token (exact), card token (exact), refund token (exact), and customer token (exact).
        :param start_date: Return only charges created on or after this date (e.g. 2012/12/25).
        :param end_date: Return only charges created before this date (e.g. 2013/12/25).
        :param sort: The field used to sort the charges (created_at or amount). Default value is created_at.
        :param direction: The direction in which to sort the charges (1 for ascending or -1 for descending). Default value is 1.
        :return: None
        """
        ...

    def get_charges_charge_token(self) -> None:
        """
        Returns the details of a charge.

        GET /charges/charge-token

        Example:
        curl https://test-api.pinpayments.com/1/charges/ch_lfUYEBK14zotCTykezJkfg -u your-secret-api-key:

        :return: None
        """
        ...

    def get_charges_verify(self) -> None:
        """
        Verify the result of a 3D Secure enabled charge.
        For more information about 3D Secure, see the 3D Secure integration guide.

        GET /charges/verify?session_token=session-token

        Example:
        curl https://api.pinpayments.com/1/charges/verify -u your-secret-api-key: -X GET -d "session_token=se_sGt9PuNYfVzJqTSLP2CV8g"

        :return: None
        """
        ...


if __name__ == '__main__':
    refunds_api = RefundsAPI()

    # refunds_api.post_charges()
    # refunds_api.put_charges_charge_token_void()
    # refunds_api.put_charges_charge_token_capture()
    # refunds_api.get_charges()
    # refunds_api.get_charges_search()
    # refunds_api.get_charges_charge_token()
    # refunds_api.get_charges_verify()
