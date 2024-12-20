Deposits API
============

The `Deposits` API provides methods for listing and retrieving details of deposits.


To initialize the `Deposits` API, use the following:

.. code-block:: python

    from deposits import Deposits
    from config import get_api_key

    # Initialize the API with your API key and mode
    deposits_api = Deposits(api_key=get_api_key(), mode='test')

List Deposits
-------------

Retrieves a paginated list of all deposits.

**Usage Example**

.. code-block:: python

    response = deposits_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "deposit_token_1",
                "amount": 10000,
                "currency": "AUD",
                "status": "pending"
            },
            {
                "token": "deposit_token_2",
                "amount": 5000,
                "currency": "AUD",
                "status": "processed"
            }
        ],
        "status": 200
    }


Retrieve Deposit Details
------------------------

Retrieves the details of a specific deposit.

**Usage Example**

.. code-block:: python

    response = deposits_api.details(deposit_token="deposit_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "deposit_token_1",
            "amount": 10000,
            "currency": "AUD",
            "status": "processed",
            "created_at": "2023-10-01T10:00:00Z"
        },
        "status": 200
    }

.. tip:: Learn More

    To learn more about deposits functionality, refer to: :mod:`pin_payments.deposits`