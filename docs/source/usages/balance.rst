Balance API
===========

The `Balance` API allows you to retrieve the current balance of funds in your Pin Payments account.


To initialize the `Balance` API, use the following:

.. code-block:: python

    from balance import Balance
    from config import get_api_key

    # Initialize the API with your API key and mode
    balance_api = Balance(api_key=get_api_key(), mode='test')

Detail
------
Retrieves the current balance of the Pin Payments account.

**Usage Example**

.. code-block:: python

    response = balance_api.detail()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "available": [
                {
                    "currency": "AUD",
                    "amount": "100000"
                }
            ]
        },
        "status": 200
    }

.. tip:: Learn More

    To learn more about balance functionality, refer to: :mod:`pin_payments.balance`
