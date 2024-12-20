Authorisations API
==================

The `Authorisations` class provides methods for managing payment card authorisations, including creating, voiding, capturing funds, and retrieving authorisation details.


To initialize the `Authorisations` API, use the following:

.. code-block:: python

    from authorisations import Authorisations
    from config import get_api_key

    # Initialize the API with your API key and mode
    authorisations_api = Authorisations(api_key=get_api_key(), mode='test')

Create Authorisation
---------------------

Creates a new payment card authorisation.

**Usage Example**

.. code-block:: python

    response = authorisations_api.create_authorisation(
        email="customer@example.com",
        description="Test Authorisation",
        amount=1000,
        ip_address="127.0.0.1",
        card={
            'number': '4200000000000000',
            'expiry_month': '12',
            'expiry_year': '2025',
            'cvc': '123'
        },
        currency="AUD"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "auth_token_example",
            "amount": 1000,
            "currency": "AUD",
            "description": "Test Authorisation",
            "status": "authorised"
        },
        "status": 201
    }


Void Authorisation
-------------------

Voids a previously created authorisation.

**Usage Example**

.. code-block:: python

    response = authorisations_api.void_authorisation(auth_token="auth_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "auth_token_example",
            "status": "voided"
        },
        "status": 200
    }


Capture Authorisation
-----------------------

Captures funds from an authorised payment card.

**Usage Example**

.. code-block:: python

    response = authorisations_api.capture_authorisation(auth_token="auth_token_example", amount=1000)
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "auth_token_example",
            "status": "captured",
            "amount": 1000
        },
        "status": 200
    }


List Authorisations
---------------------

Retrieves a paginated list of all authorisations.

**Usage Example**

.. code-block:: python

    response = authorisations_api.list_authorisations()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "auth_token_example_1",
                "amount": 1000,
                "status": "authorised"
            },
            {
                "token": "auth_token_example_2",
                "amount": 500,
                "status": "captured"
            }
        ],
        "status": 200
    }


Get Authorisation Details
--------------------------

Retrieves the details of a specific authorisation.

**Usage Example**

.. code-block:: python

    response = authorisations_api.get_authorisation_details(auth_token="auth_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "auth_token_example",
            "amount": 1000,
            "currency": "AUD",
            "description": "Test Authorisation",
            "status": "authorised"
        },
        "status": 200
    }

.. tip:: Learn More

    To learn more about authorization functionality, refer to: :mod:`pin_payments.authorisations`