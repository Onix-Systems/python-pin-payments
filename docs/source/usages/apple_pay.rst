Apple Pay API
=============

The `ApplePayAPI` class provides methods for managing Apple Pay integrations, including handling merchant domains, sessions, and certificates.


To initialize the `ApplePayAPI`, use the following:

.. code-block:: python

    from apple_pay import ApplePayAPI
    from config import get_api_key

    # Initialize the API with your API key and mode
    apple_pay_api = ApplePayAPI(api_key=get_api_key(), mode='live')



Create Domain
-------------

Registers a fully-qualified domain for Apple Pay.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.create_domain(domain_name='example.com')
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "domain_name": "example.com",
            "created_at": "2023-10-01T12:00:00Z"
        },
        "status": 201
    }

List Domains
------------

Retrieves all registered Apple Pay domains.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.list_domains()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {"domain_name": "example.com", "created_at": "2023-10-01T12:00:00Z"}
        ],
        "status": 200
    }

Delete Domain
-------------

Deletes a registered Apple Pay domain.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.delete_domain(domain_token='domain_token_example')
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": null,
        "status": 204
    }

Check Host
----------

Checks whether a domain is registered with Apple Pay.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.check_host(domain_name='example.com')
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "domain_name": "example.com",
            "status": "registered"
        },
        "status": 200
    }

Create Session
--------------

Creates an Apple Pay session.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.create_session(
        validation_url='https://apple-pay-session.com',
        initiative='web',
        initiative_context='example.com'
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "session_id": "session_12345",
            "expires_at": "2023-10-01T13:00:00Z"
        },
        "status": 201
    }

Create Certificate
-------------------

Creates a new Apple Pay certificate.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.create_certificate()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "certificate_id": "cert_123",
            "created_at": "2023-10-01T12:00:00Z"
        },
        "status": 201
    }

List Certificates
------------------

Retrieves all Apple Pay certificates.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.list_certificates()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {"certificate_id": "cert_123", "created_at": "2023-10-01T12:00:00Z"}
        ],
        "status": 200
    }


Get Certificate
---------------

Retrieves details of a specific Apple Pay certificate.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.get_certificate(certificate_token='cert_123')
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "certificate_id": "cert_123",
            "details": "Certificate details here"
        },
        "status": 200
    }

Upload Certificate
-------------------

Uploads an Apple Pay payment processing certificate.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.upload_certificate(certificate_pem='PEM_CONTENT_HERE')
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "message": "Certificate uploaded successfully"
        },
        "status": 200
    }


Delete Certificate
-------------------

Deletes an Apple Pay certificate.

**Usage Example**

.. code-block:: python

    response = apple_pay_api.delete_certificate(certificate_token='cert_123')
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": null,
        "status": 204
    }

.. tip:: Learn More

    To learn more about Apple pay functionality, refer to: :mod:`pin_payments.apple_pay`