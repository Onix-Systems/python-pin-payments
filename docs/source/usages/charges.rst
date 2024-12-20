Charges API
===========

The `Charges` API provides functionality to process payment card charges. It includes methods to create, void, capture, list, search, and verify charges.


Create Charge
-------------

Creates a new payment card charge.

**Usage Example**

.. code-block:: python

    response = charges_api.create(
        email="customer@example.com",
        description="Test Charge",
        amount=1000,
        ip_address="192.0.2.1",
        currency="AUD",
        card={
            'number': '4200000000000000',
            'expiry_month': '12',
            'expiry_year': '2025',
            'cvc': '123'
        }
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "charge_token_example",
            "amount": 1000,
            "currency": "AUD",
            "description": "Test Charge",
            "status": "captured"
        },
        "status": 201
    }



Void Charge
-----------

Voids a previously authorized charge.

**Usage Example**

.. code-block:: python

    response = charges_api.void(charge_token="charge_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "charge_token_example",
            "status": "voided"
        },
        "status": 200
    }



Capture Charge
--------------

Captures a previously authorized charge.

**Usage Example**

.. code-block:: python

    response = charges_api.capture(charge_token="charge_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "charge_token_example",
            "status": "captured",
            "amount": 1000
        },
        "status": 201
    }



List Charges
------------

Retrieves a paginated list of all charges.

**Usage Example**

.. code-block:: python

    response = charges_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "charge_token_example_1",
                "amount": 1000,
                "status": "captured"
            },
            {
                "token": "charge_token_example_2",
                "amount": 500,
                "status": "authorized"
            }
        ],
        "status": 200
    }



Search Charges
--------------

Searches for charges based on the provided criteria.

**Usage Example**

.. code-block:: python

    response = charges_api.search(query="customer@example.com", start_date="2023-01-01", end_date="2023-12-31")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "charge_token_example",
                "amount": 1000,
                "description": "Test Charge",
                "status": "captured"
            }
        ],
        "status": 200
    }



Retrieve Charge Details
------------------------

Retrieves the details of a specific charge.

**Usage Example**

.. code-block:: python

    response = charges_api.charge(charge_token="charge_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "charge_token_example",
            "amount": 1000,
            "description": "Test Charge",
            "status": "captured",
            "email": "customer@example.com"
        },
        "status": 200
    }


Verify 3D Secure Charge
------------------------

Verifies the result of a 3D Secure-enabled charge.

**Usage Example**

.. code-block:: python

    response = charges_api.verify(session_token="3d_secure_session_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "3d_secure_charge_token_example",
            "status": "verified"
        },
        "status": 200
    }

.. tip:: Learn More

    To learn more about charges functionality, refer to: :mod:`pin_payments.charges`