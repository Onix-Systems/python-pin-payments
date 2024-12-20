Plans API
=========

The `Plans` API enables you to create, modify, and manage recurring billing plans.


To initialize the `Plans` class, use the following:

.. code-block:: python

    from plans import Plans
    from config import get_api_key

    plans_api = Plans(api_key=get_api_key(), mode='test')

Create a Plan
-------------

Creates a new recurring billing plan.

**Usage Example**

.. code-block:: python

    response = plans_api.create(
        name='Monthly Plan',
        amount=1000,
        interval=1,
        interval_unit='month',
        currency='AUD',
        setup_amount=500,
        customer_permissions=["update", "cancel"]
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "plan_token_1",
            "name": "Monthly Plan",
            "amount": 1000,
            "interval": 1,
            "interval_unit": "month",
            "currency": "AUD",
            "setup_amount": 500
        },
        "status": 201
    }

List Plans
----------

Retrieves a paginated list of all plans.

**Usage Example**

.. code-block:: python

    response = plans_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "plan_token_1",
                "name": "Monthly Plan",
                "amount": 1000,
                "interval": 1,
                "interval_unit": "month",
                "currency": "AUD"
            }
        ],
        "status": 200
    }

Retrieve Plan Details
----------------------

Gets details of a specific plan by its token.

**Usage Example**

.. code-block:: python

    response = plans_api.details(plan_token="plan_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "plan_token_1",
            "name": "Monthly Plan",
            "amount": 1000,
            "interval": 1,
            "interval_unit": "month",
            "currency": "AUD"
        },
        "status": 200
    }


Update a Plan
--------------

Updates details of an existing plan.

**Usage Example**

.. code-block:: python

    response = plans_api.update(
        plan_token="plan_token_1",
        name="Updated Plan Name",
        customer_permissions=["cancel"]
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "plan_token_1",
            "name": "Updated Plan Name",
            "customer_permissions": ["cancel"]
        },
        "status": 200
    }

---

Delete a Plan
--------------

Deletes a plan along with its subscriptions.

**Usage Example**

.. code-block:: python

    response = plans_api.delete(plan_token="plan_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "status": 204
    }


Create a Subscription
-----------------------

Creates a new subscription under a specific plan.

**Usage Example**

.. code-block:: python

    response = plans_api.create_subscription(
        plan_token="plan_token_1",
        customer_token="customer_token_1",
        card_token="card_token_1"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "subscription_token_1",
            "status": "active",
            "plan_token": "plan_token_1",
            "customer_token": "customer_token_1"
        },
        "status": 200
    }


List Subscriptions
--------------------

Lists all subscriptions under a specific plan.

**Usage Example**

.. code-block:: python

    response = plans_api.list_subscriptions(plan_token="plan_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "subscription_token_1",
                "status": "active",
                "plan_token": "plan_token_1",
                "customer_token": "customer_token_1"
            }
        ],
        "status": 200
    }

.. tip:: Learn More

    To learn more about plans functionality, refer to: :mod:`pin_payments.plans`