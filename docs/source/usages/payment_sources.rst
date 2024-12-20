Payment Sources API
===================

The `Payment Sources` API enables secure storage of payment source information, returning a token that can be used for creating charges.


To initialize the `PaymentSources` class, use the following:

.. code-block:: python

    from payment_sources import PaymentSources
    from config import get_api_key

    payment_sources_api = PaymentSources(api_key=get_api_key(), mode='test')

Create Payment Source
---------------------
Creates a new payment source (e.g., card) and retrieves its token.

**Usage Example**

.. code-block:: python

    response = payment_sources_api.create_payment_source(
        source_type='card',
        source={
            "number": "4200000000000000",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvc": "123",
            "name": "John Doe"
        }
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "payment_source_token_1",
            "type": "card",
            "display_number": "XXXX-XXXX-XXXX-0000",
            "expiry_month": "12",
            "expiry_year": "2025"
        },
        "status": 201
    }

.. tip:: Learn More

    To learn more about payment sources functionality, refer to: :mod:`pin_payments.payment_sources`