Merchants API
=============

The `Merchants` API allows approved partners to manage referred merchants. You can create new merchants, retrieve their details, and list merchants associated with your account.


To initialize the `Merchants` class, use the following:

.. code-block:: python

    from merchants import Merchants

    PARTNER_API_KEY = "your_partner_api_key"  # Should be provided by the approved partner
    merchants_api = Merchants(api_key=PARTNER_API_KEY, mode='test')



Create Merchant
---------------

Creates a new merchant referred to the system.

**Usage Example**

.. code-block:: python

    response = merchants_api.create(
        contact={
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "123456789",
            "email": "john.doe@example.com",
            "password": "example-password"
        },
        entity={
            "business_registration_number": "123456789",
            "full_legal_name": "John's Coffee Shop",
            "address_line_1": "123 Coffee St",
            "address_locality": "CoffeeTown",
            "address_region": "CO",
            "address_postal_code": "12345",
            "address_country_code": "AU"
        },
        business={
            "trading_name": "John's Coffee",
            "description": "Coffee retail shop",
            "url": "https://johncoffee.com"
        },
        bank_account={
            "name": "John's Coffee",
            "bsb": "182222",
            "number": "000111222"
        },
        director={
            "full_name": "John Doe",
            "contact_number": "123456789",
            "date_of_birth": "1970-01-01"
        },
        notes="New merchant"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "merchant_token_1",
            "status": "pending_activation",
            "created_at": "2023-10-01T10:00:00Z"
        },
        "status": 201
    }


List Merchants
--------------

Retrieves a list of all merchants referred by you.

**Usage Example**

.. code-block:: python

    response = merchants_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "merchant_token_1",
                "status": "active",
                "name": "John's Coffee Shop"
            },
            {
                "token": "merchant_token_2",
                "status": "pending_activation",
                "name": "Doe's Bakery"
            }
        ],
        "status": 200
    }


Retrieve Merchant Details
--------------------------

Retrieves details of a specific merchant by its token.

**Usage Example**

.. code-block:: python

    response = merchants_api.details(merchant_token="merchant_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "merchant_token_1",
            "status": "active",
            "name": "John's Coffee Shop",
            "created_at": "2023-10-01T10:00:00Z"
        },
        "status": 200
    }


Retrieve Default Settings
--------------------------

Retrieves the default settings that will be applied to new merchants referred by the partner.

**Usage Example**

.. code-block:: python

    response = merchants_api.default_settings()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "currency": "AUD",
            "transaction_limits": {
                "min": 1,
                "max": 100000
            }
        },
        "status": 200
    }

.. tip:: Learn More

    To learn more about merchants functionality, refer to: :mod:`pin_payments.merchants`