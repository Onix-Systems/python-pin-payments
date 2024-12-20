Events API
==========

The `Events` API enables you to view all activities happening on your account.


.. code-block:: python

    from events import Events
    from config import get_api_key

    events_api = Events(api_key=get_api_key(), mode='test')


List Events
-----------

Retrieves a paginated list of all events.

**Usage Example**

.. code-block:: python

    response = events_api.list()
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "event_token_1",
                "type": "charge.authorised",
                "created_at": "2023-10-01T10:00:00Z"
            },
            {
                "token": "event_token_2",
                "type": "customer.created",
                "created_at": "2023-10-02T11:00:00Z"
            }
        ],
        "status": 200
    }


Retrieve Event Details
-----------------------

Retrieves details for a specific event by its token.

**Usage Example**

.. code-block:: python

    response = events_api.details(event_token="event_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "event_token_1",
            "type": "charge.authorised",
            "data": {
                "charge_token": "charge_token_123",
                "customer_token": "customer_token_456"
            },
            "created_at": "2023-10-01T10:00:00Z"
        },
        "status": 200
    }

Learn More
----------
To learn more about events functionality, refer to: :mod:`pin_payments.events`
