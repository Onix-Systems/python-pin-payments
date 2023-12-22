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
