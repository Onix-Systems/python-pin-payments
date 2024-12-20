Recipients API
---------------

The `Recipients` API allows you to securely store transfer recipient details and retrieve tokens for initiating fund transfers.

To initialize the `Recipients` class, use the following:

.. code-block:: python

    from recipients import Recipients
    from config import get_api_key

    recipients_api = Recipients(api_key=get_api_key(), mode='test')

Create a Recipient
-------------------

Creates a new recipient and returns its details.

**Usage Example**

.. code-block:: python

    response = recipients_api.create(
        email="recipient@example.com",
        name="Recipient Name",
        bank_account={
            "name": "Recipient Name",
            "bsb": "123456",
            "number": "987654321"
        }
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "recipient_token_1",
            "email": "recipient@example.com",
            "bank_account": {
                "name": "Recipient Name",
                "bsb": "123456",
                "number": "987654321"
            }
        },
        "status": 201
    }

List Recipients
---------------

Retrieves a paginated list of all recipients.

**Usage Example**

.. code-block:: python

    response = recipients_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "recipient_token_1",
                "email": "recipient@example.com",
                "name": "Recipient Name"
            }
        ],
        "status": 200
    }



Get Recipient Details
----------------------

Retrieves the details of a specific recipient by its token.

**Usage Example**

.. code-block:: python

    response = recipients_api.get_details(recipient_token="recipient_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "recipient_token_1",
            "email": "recipient@example.com",
            "name": "Recipient Name",
            "bank_account": {
                "name": "Recipient Name",
                "bsb": "123456",
                "number": "987654321"
            }
        },
        "status": 200
    }

Update a Recipient
-------------------

Updates the details of an existing recipient.

**Usage Example**

.. code-block:: python

    response = recipients_api.update(
        recipient_token="recipient_token_1",
        email="updated_recipient@example.com"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "recipient_token_1",
            "email": "updated_recipient@example.com"
        },
        "status": 200
    }


List Transfers for a Recipient
------------------------------

Retrieves a list of all transfers for a specific recipient.

**Usage Example**

.. code-block:: python

    response = recipients_api.list_transfers(recipient_token="recipient_token_1")
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

.. tip:: Learn More

    To learn more about recipients functionality, refer to: :mod:`pin_payments.recipients`