from typing import Optional


class RefundsAPI:
    """
    The refunds API allows you to refund charges and retrieve the details of previous refunds.
    """

    def __init__(
            self,
            api_key: str,
    ):
        self.__api_key = api_key

    def get_refunds(
            self
    ) -> dict:
        """
        Returns a paginated list of all refunds.

        GET /refunds

        Example:
        curl https://test-api.pinpayments.com/1/refunds -u your-secret-api-key:

        :return: None
        """
        ...

    def get_refunds_refund_token(
            self
    ) -> dict:
        """
        Returns the details of the specified refund.

        GET /refunds/refund-token

        Example:
        curl https://test-api.pinpayments.com/1/refunds/rf_ERCQy--Ay6o-NKGiUVcKKA -u your-secret-api-key: -X GET

        :return: None
        """
        ...

    def post_charges_charge_token_refunds(
            self,
            amount: Optional[int] = None
    ) -> dict:
        """
        Creates a new refund and returns its details.

        POST /charges/charge-token/refunds

        Example:
        curl https://test-api.pinpayments.com/1/charges/ch_bZ3RhJnIUZ8HhfvH8CCvfA/refunds -u your-secret-api-key: -X POST

        :param amount: The amount to refund in the currency’s base unit (e.g. cents for AUD, yen for JPY). Default value is the full amount of the charge.
        :return: None
        """
        ...

    def get_charges_charge_token_refunds(
            self
    ) -> dict:
        """
        Returns a list of all refunds for the specified charge.

        GET /charges/charge-token/refunds

        Example:
        curl https://test-api.pinpayments.com/1/charges/ch_bZ3RhJnIUZ8HhfvH8CCvfA/refunds -u your-secret-api-key:

        :return: None
        """
        ...


if __name__ == '__main__':
    refunds_api = RefundsAPI()
