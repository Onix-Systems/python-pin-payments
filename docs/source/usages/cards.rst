Cards API
=========

The `Cards` API allows you to securely store payment card details in exchange for a card token. This class includes features for creating and managing cards.


To initialize the `Cards` API, use the following:

.. code-block:: python

    from cards import Cards
    from config import get_api_key

    # Initialize the API with your API key and mode
    cards_api = Cards(api_key=get_api_key(), mode='test')



Create
------

Stores payment card details securely and returns a card token.

**Usage Example**

.. code-block:: python

    card_details = {
        "number": "4200000000000000",
        "expiry_month": "12",
        "expiry_year": "2025",
        "cvc": "123",
        "name": "John Doe",
        "address_line1": "123 Test St",
        "address_city": "Test City",
        "address_country": "Australia"
    }

    response = cards_api.create(
        number=card_details["number"],
        expiry_month=card_details["expiry_month"],
        expiry_year=card_details["expiry_year"],
        cvc=card_details["cvc"],
        name=card_details["name"],
        address_line1=card_details["address_line1"],
        address_city=card_details["address_city"],
        address_country=card_details["address_country"]
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "card_token_example",
            "scheme": "visa",
            "display_number": "XXXX-XXXX-XXXX-0000",
            "expiry_month": "12",
            "expiry_year": "2025",
            "name": "John Doe",
            "address_line1": "123 Test St",
            "address_city": "Test City",
            "address_country": "Australia"
        },
        "status": 201
    }

.. tip:: Learn More

    To learn more about cards functionality, refer to: :mod:`pin_payments.cards`