Transfers API
=============

The `Transfers` API allows you to manage fund transfers to Australian bank accounts and retrieve transfer details.



To initialize the `Transfers` class, use the following:

.. code-block:: python

    from transfers import Transfers
    from config import get_api_key

    transfers_api = Transfers(api_key=get_api_key(), mode='test')



Create a Transfer
------------------

Creates a new transfer to a recipient.

**Usage Example**

.. code-block:: python

    response = transfers_api.create(
        description="Test Transfer",
        amount=1000,
        currency="AUD",
        recipient="recipient_token"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "transfer_token_1",
            "amount": 1000,
            "currency": "AUD",
            "status": "pending"
        },
        "status": 201
    }



List All Transfers
-------------------

Retrieves a paginated list of all transfers.

**Usage Example**

.. code-block:: python

    response = transfers_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "transfer_token_1",
                "amount": 1000,
                "currency": "AUD"
            }
        ],
        "status": 200
    }



Search Transfers
-----------------

Searches transfers based on query parameters.

**Usage Example**

.. code-block:: python

    response = transfers_api.search(query="recipient_token")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "transfer_token_1",
                "amount": 1000,
                "currency": "AUD"
            }
        ],
        "status": 200
    }



Get Transfer Details
---------------------

Fetches the details of a transfer by its token.

**Usage Example**

.. code-block:: python

    response = transfers_api.details(transfer_token="transfer_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "transfer_token_1",
            "amount": 1000,
            "status": "pending"
        },
        "status": 200
    }



Retrieve Transfer Line Items
-----------------------------

Retrieves line items associated with a transfer.

**Usage Example**

.. code-block:: python

    response = transfers_api.line_items(transfer_token="transfer_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "amount": 500,
                "description": "Line Item Description"
            }
        ],
        "status": 200
    }

.. tip:: Learn More

    To learn more about transfers functionality, refer to: :mod:`pin_payments.transfers`