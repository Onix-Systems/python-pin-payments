Refunds API
===========

The `Refunds` API allows you to manage refunds for charges, including creating, retrieving details, and listing refunds.


To initialize the `Refunds` class, use the following:

.. code-block:: python

    from refunds import Refunds
    from config import get_api_key

    refunds_api = Refunds(api_key=get_api_key(), mode='test')


List All Refunds
-----------------

Fetches a paginated list of all refunds.

**Usage Example**

.. code-block:: python

    response = refunds_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "refund_token_1",
                "amount": 1000,
                "currency": "AUD",
                "status": "success"
            },
            {
                "token": "refund_token_2",
                "amount": 500,
                "currency": "AUD",
                "status": "success"
            }
        ],
        "status": 200
    }


Get Refund Details
-------------------

Fetches details of a specific refund by its token.

**Usage Example**

.. code-block:: python

    response = refunds_api.details(refund_token="refund_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "refund_token_1",
            "amount": 1000,
            "currency": "AUD",
            "status": "success"
        },
        "status": 200
    }

Create a Refund
---------------

Creates a refund for a specific charge.

**Usage Example**

.. code-block:: python

    response = refunds_api.create_refund(charge_token="charge_token_1", amount=1000)
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "refund_token_1",
            "amount": 1000,
            "currency": "AUD",
            "status": "pending"
        },
        "status": 201
    }


List Refunds for a Specific Charge
-----------------------------------

Fetches a list of refunds associated with a specific charge token.

**Usage Example**

.. code-block:: python

    response = refunds_api.list_charge(charge_token="charge_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "refund_token_1",
                "amount": 1000,
                "currency": "AUD",
                "status": "success"
            }
        ],
        "status": 200
    }

.. tip:: Learn More

    To learn more about refunds functionality, refer to: :mod:`pin_payments.refunds`