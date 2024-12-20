Customers API
=============

The `Customers` API provides functionality to manage customers, including creating, updating, retrieving details, listing, and managing customer-related operations like cards, subscriptions, and charges.


To initialize the `Customers` API, use the following:

.. code-block:: python

    from customers import Customers
    from config import get_api_key

    # Initialize the API with your API key and mode
    customers_api = Customers(api_key=get_api_key(), mode='test')




Create Customer
---------------
Creates a new customer.

**Usage Example**

.. code-block:: python

    response = customers_api.create(
        email="customer@example.com",
        first_name="John",
        last_name="Doe",
        card={
            "number": "4200000000000000",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvc": "123"
        }
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "cust_token_example",
            "email": "customer@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "created_at": "2023-10-23T00:00:00Z"
        },
        "status": 201
    }



List Customers
--------------
Retrieves a paginated list of all customers.

**Usage Example**

.. code-block:: python

    response = customers_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "cust_token_example",
                "email": "customer@example.com"
            },
            {
                "token": "cust_token_example_2",
                "email": "another@example.com"
            }
        ],
        "status": 200
    }



Retrieve Customer Details
-------------------------
Retrieves details for a specific customer.
**Usage Example**

.. code-block:: python

    response = customers_api.details(customer_token="cust_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "cust_token_example",
            "email": "customer@example.com",
            "first_name": "John",
            "last_name": "Doe"
        },
        "status": 200
    }



Update Customer
---------------
Updates the details of an existing customer.

**Usage Example**

.. code-block:: python

    response = customers_api.update(
        customer_token="cust_token_example",
        first_name="Jane",
        last_name="Doe"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "cust_token_example",
            "email": "customer@example.com",
            "first_name": "Jane",
            "last_name": "Doe"
        },
        "status": 200
    }



Delete Customer
---------------
Deletes a customer.

**Usage Example**

.. code-block:: python

    response = customers_api.delete(customer_token="cust_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "status": 204
    }



List Customer's Charges
-----------------------
Lists all charges for a specific customer.

.. code-block:: python

    response = customers_api.list_charges(customer_token="cust_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "charge_token_example",
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


List Customer's Cards
---------------------
Lists all cards associated with a specific customer.
**Usage Example**

.. code-block:: python

    response = customers_api.list_cards(customer_token="cust_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "card_token_example",
                "display_number": "XXXX-XXXX-XXXX-0000",
                "expiry_month": "12",
                "expiry_year": "2025"
            }
        ],
        "status": 200
    }


Create a New Card for a Customer
--------------------------------
Creates and associates a new card to a customer.

**Usage Example**

.. code-block:: python

    response = customers_api.create_card(
        customer_token="cust_token_example",
        number="4200000000000000",
        expiry_month="12",
        expiry_year="2025",
        cvc="123",
        name="John Doe",
        address_line1="123 Test St",
        address_city="Test City",
        address_country="Australia"
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
            "expiry_year": "2025"
        },
        "status": 201
    }



Delete Customer's Card
----------------------
Deletes a specific card associated with a customer.

**Usage Example**

.. code-block:: python

    response = customers_api.delete_card(
        customer_token="cust_token_example",
        card_token="card_token_example"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "status": 204
    }


List Customer's Subscriptions
-----------------------------
Lists all subscriptions associated with a specific customer.

**Usage Example**

.. code-block:: python

    response = customers_api.list_subscriptions(customer_token="cust_token_example")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "sub_token_example",
                "plan": "premium_plan",
                "status": "active"
            }
        ],
        "status": 200
    }

Delete Customer's Subscription
------------------------------
Deletes a specific subscription associated with a customer.

**Usage Example**

.. code-block:: python

    response = customers_api.delete_subscriptions(
        customer_token="cust_token_example",
        subscription_token="sub_token_example"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "status": 200
    }

.. tip:: Learn More

    To learn more about customers functionality, refer to: :mod:`pin_payments.customers`