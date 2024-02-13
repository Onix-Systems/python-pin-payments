import logging

from requests.auth import HTTPBasicAuth


class Base:
    def __init__(
            self,
            api_key: str,
            mode: str = 'live'
    ):
        self._api_key = api_key
        self._modes = ['live', 'test']
        if mode == 'live':
            self._base_url = 'https://api.pinpayments.com/1/'
        elif mode == 'test':
            self._base_url = 'https://test-api.pinpayments.com/1/'
        else:
            raise ValueError(f'"mode" can be only one of {self._modes}')
        self._auth = HTTPBasicAuth(self._api_key, '')

    @staticmethod
    def _handle_response(
            response,
            function_name: str,
            required_status_code: int,
    ) -> dict:
        """
        Processes responses from the API, logs errors and returns the result.

        :param response: The response object from requests.
        :param function_name: The name of the function that calls the handler.
        :return: Dictionary with response or error data.
        """
        if response.status_code == required_status_code:
            return response.json() if response.text else ""
        error_message = f"Error in {function_name}: {response.status_code}, {response.text}"
        logging.error(error_message)
        return {"error": error_message}
