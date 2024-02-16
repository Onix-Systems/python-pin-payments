import requests

from config import get_api_key
from pin_payments.base import Base


class ApplePayAPI(Base):
    """
    The Apple Pay API supports Apple Pay integrations via Pin Payments,
    including managing Apple Pay merchant domains and sessions.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        """
        Initializes the Apple Pay API with an API key and mode.
        Inherits initialization from Base, setting up authentication, and the base URL.
        """
        super().__init__(api_key, mode)
        self._base_url += 'apple_pay/'

    def create_domain(self, domain_name: str) -> dict:
        """
        Registers a new domain for Apple Pay.
        :param domain_name: The fully-qualified domain name to register.
        :return: A dictionary with the domain details.
        """
        data = {'domain_name': domain_name}
        response = requests.post(f"{self._base_url}domains", auth=self._auth, json=data)
        return self._handle_response(
            response,
            'create_domain',
            201
        )

    def list_domains(self) -> dict:
        """
        Retrieves a list of all registered Apple Pay domains.
        :return: A dictionary containing a list of domains.
        """
        response = requests.get(f"{self._base_url}domains", auth=self._auth)
        return self._handle_response(
            response,
            'list_domains',
            200
        )

    def delete_domain(self, domain_token: str) -> dict:
        """
        Deletes a registered Apple Pay domain.
        :param domain_token: The token of the domain to delete.
        :return: A dictionary confirming the deletion.
        """
        response = requests.delete(
            f"{self._base_url}domains/{domain_token}",
            auth=self._auth
        )
        return self._handle_response(
            response,
            'delete_domain',
            204
        )

    def check_host(self, domain_name: str) -> dict:
        """
        Checks if an Apple Pay domain is registered.
        :param domain_name: The domain name to check.
        :return: A dictionary with the domain registration status.
        """
        params = {'domain_name': domain_name}
        response = requests.get(
            f"{self._base_url}host_check",
            auth=self._auth,
            params=params
        )
        return self._handle_response(
            response,
            'check_host',
            200
        )

    def create_session(
            self,
            validation_url: str,
            initiative: str,
            initiative_context: str
    ) -> dict:
        """
        Creates an Apple Pay session.
        :param validation_url: The URL provided by the Apple Pay JS API during a payment session.
        :param initiative: The initiative type (e.g., 'web' for web payments).
        :param initiative_context: The domain name initiating the session.
        :return: A dictionary with session details.
        """
        data = {
            'validation_url': validation_url,
            'initiative': initiative,
            'initiative_context': initiative_context
        }
        response = requests.post(
            f"{self._base_url}sessions",
            auth=self._auth,
            json=data
        )
        return self._handle_response(
            response,
            'create_session',
            201
        )

    def create_certificate(self) -> dict:
        """
        Creates a new Apple Pay certificate.
        :return: A dictionary with the certificate details.
        """
        response = requests.post(f"{self._base_url}certificates", auth=self._auth)
        return self._handle_response(
            response,
            'create_certificate',
            201
        )

    def list_certificates(self) -> dict:
        """
        Retrieves a list of all Apple Pay certificates.
        :return: A dictionary containing a list of certificates.
        """
        response = requests.get(f"{self._base_url}certificates", auth=self._auth)
        return self._handle_response(
            response,
            'list_certificates',
            200
        )

    def get_certificate(self, certificate_token: str) -> dict:
        """
        Retrieves details of a specific Apple Pay certificate.
        :param certificate_token: The token of the certificate to retrieve.
        :return: A dictionary with the certificate details.
        """
        response = requests.get(
            f"{self._base_url}certificates/{certificate_token}",
            auth=self._auth
        )
        return self._handle_response(
            response,
            'get_certificate',
            200
        )

    def upload_certificate(self, certificate_pem: str) -> dict:
        """
        Uploads an Apple Pay payment processing certificate.
        :param certificate_pem: The payment processing certificate in PEM format.
        :return: A dictionary confirming the upload.
        """
        data = {'pem': certificate_pem}
        response = requests.put(
            f"{self._base_url}certificates",
            auth=self._auth,
            json=data
        )
        return self._handle_response(
            response,
            'upload_certificate',
            200
        )

    def delete_certificate(self, certificate_token: str) -> dict:
        """
        Deletes an Apple Pay certificate.
        :param certificate_token: The token of the certificate to delete.
        :return: A dictionary confirming the deletion.
        """
        response = requests.delete(
            f"{self._base_url}certificates/{certificate_token}",
            auth=self._auth
        )
        return self._handle_response(
            response,
            'delete_certificate',
            204
        )


if __name__ == '__main__':
    apple_pay_api = ApplePayAPI(api_key=get_api_key(), mode='test')

    domain_name = 'example.com'
    domain_registration_response = apple_pay_api.create_domain(domain_name=domain_name)
    print("Domain Registration Response:", domain_registration_response)

    domains_list_response = apple_pay_api.list_domains()
    print("Domains List Response:", domains_list_response)

    domain_token = 'domain_token_example'

    delete_domain_response = apple_pay_api.delete_domain(domain_token=domain_token)
    print("Delete Domain Response:", delete_domain_response)

    validation_url = 'https://example.com'
    initiative = 'web'
    initiative_context = 'example.com'
    session_response = apple_pay_api.create_session(
        validation_url=validation_url,
        initiative=initiative,
        initiative_context=initiative_context
    )
    print("Session Response:", session_response)

    certificate_response = apple_pay_api.create_certificate()
    print("Certificate Response:", certificate_response)

    certificates_list_response = apple_pay_api.list_certificates()
    print("Certificates List Response:", certificates_list_response)

    certificate_token = certificates_list_response.get('response')[0].get('token')

    certificate_details_response = apple_pay_api.get_certificate(
        certificate_token=certificate_token)
    print("Certificate Details Response:", certificate_details_response
          )

    delete_certificate_response = apple_pay_api.delete_certificate(
        certificate_token=certificate_token
    )
    print("Delete Certificate Response:", delete_certificate_response)
