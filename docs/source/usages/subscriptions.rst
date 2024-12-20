Subscriptions API
=================

The `Subscriptions` API enables you to manage recurring subscriptions, including creating, updating, canceling, and reactivating subscriptions.


To initialize the `Subscriptions` class, use the following:

.. code-block:: python

    from subscriptions import Subscriptions
    from config import get_api_key

    subscriptions_api = Subscriptions(api_key=get_api_key(), mode='test')

Create a Subscription
----------------------

Activates a new subscription for a customer to a specific plan.

**Usage Example**

.. code-block:: python

    response = subscriptions_api.create_subscription(
        plan_token="plan_token_1",
        customer_token="customer_token_1",
        include_setup_fee=True
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "subscription_token",
            "plan_token": "plan_token_1",
            "customer_token": "customer_token_1",
            "status": "active"
        },
        "status": 201
    }


List All Subscriptions
-----------------------

Fetches a paginated list of all subscriptions.

**Usage Example**

.. code-block:: python

    response = subscriptions_api.list_subscriptions()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "subscription_token_1",
                "plan_token": "plan_token_1",
                "customer_token": "customer_token_1",
                "status": "active"
            }
        ],
        "status": 200
    }


Get Subscription Details
-------------------------

Fetches details for a specific subscription by its token.

**Usage Example**

.. code-block:: python

    response = subscriptions_api.get_subscription_details(sub_token="subscription_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "subscription_token_1",
            "status": "active",
            "plan_token": "plan_token_1"
        },
        "status": 200
    }


Update a Subscription
----------------------

Updates the card for an existing subscription.

**Usage Example**

.. code-block:: python

    response = subscriptions_api.update_subscription(sub_token="subscription_token_1", card_token="new_card_token")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "subscription_token_1",
            "status": "active"
        },
        "status": 200
    }


Cancel a Subscription
----------------------

Cancels a subscription by its token.

**Usage Example**

.. code-block:: python

    response = subscriptions_api.cancel_subscription(sub_token="subscription_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "subscription_token_1",
            "status": "canceled"
        },
        "status": 200
    }


Reactivate a Subscription
--------------------------

Reactivates a canceled subscription.

**Usage Example**

.. code-block:: python

    response = subscriptions_api.reactivate_subscription(sub_token="subscription_token_1", include_setup_fee=False)
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "subscription_token_1",
            "status": "active"
        },
        "status": 200
    }


Fetch Subscription Ledger
--------------------------

Fetches ledger entries related to a subscription.

**Usage Example**

.. code-block:: python

    response = subscriptions_api.fetch_subscription_ledger(sub_token="subscription_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "amount": 1000,
                "status": "paid"
            }
        ],
        "status": 200
    }

.. tip:: Learn More

    To learn more about subscriptions functionality, refer to: :mod:`pin_payments.subscriptions`