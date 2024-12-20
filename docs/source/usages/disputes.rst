Disputes API
============

The `Disputes` API provides functionality to manage disputes raised against charges, including retrieving dispute details, managing evidence, and accepting disputes.


.. code-block:: python

    from disputes import Disputes
    from config import get_api_key

    # Initialize the API with your API key and mode
    disputes_api = Disputes(api_key=get_api_key(), mode='test')



List Disputes
-------------
Retrieves a paginated list of disputes.

**Usage Example**

.. code-block:: python

    response = disputes_api.list_disputes(sort="created_at", direction=-1)
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "dispute_token_1",
                "status": "open",
                "amount": 1000,
                "currency": "AUD"
            },
            {
                "token": "dispute_token_2",
                "status": "won",
                "amount": 2000,
                "currency": "AUD"
            }
        ],
        "status": 200
    }


Search Disputes
---------------
Searches disputes based on specific criteria.

**Usage Example**

.. code-block:: python

    response = disputes_api.search_disputes(query="unauthorized", status="open")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "token": "dispute_token_1",
                "status": "open",
                "reason": "unauthorized"
            }
        ],
        "status": 200
    }


Retrieve Dispute Details
-------------------------
Retrieves detailed information about a specific dispute.

**Usage Example**

.. code-block:: python

    response = disputes_api.get_dispute_details(dispute_token="dispute_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "dispute_token_1",
            "status": "open",
            "reason": "unauthorized",
            "amount": 1000,
            "currency": "AUD",
            "created_at": "2023-10-01T10:00:00Z"
        },
        "status": 200
    }


Retrieve Dispute Activity
--------------------------
Retrieves the activity feed for a specific dispute.

**Usage Example**

.. code-block:: python

    response = disputes_api.get_dispute_activity(dispute_token="dispute_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": [
            {
                "type": "message",
                "content": "Customer disputed the charge.",
                "created_at": "2023-10-01T11:00:00Z"
            },
            {
                "type": "update",
                "content": "Merchant submitted evidence.",
                "created_at": "2023-10-02T12:00:00Z"
            }
        ],
        "status": 200
    }


Retrieve Dispute Evidence
--------------------------
Displays the current evidence batch for a specific dispute.

**Usage Example**

.. code-block:: python

    response = disputes_api.get_dispute_evidence(dispute_token="dispute_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "customer_communication": "Chat logs with the customer.",
            "billing_agreement": "Signed billing agreement.",
            "shipping_documents": "Shipping receipt."
        },
        "status": 200
    }


Update Dispute Evidence
------------------------
Updates the evidence data for a specific dispute.

**Usage Example**

.. code-block:: python

    response = disputes_api.update_dispute_evidence(
        dispute_token="dispute_token_1",
        evidence_data={"customer_communication": "Updated chat logs"}
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "status": "updated"
        },
        "status": 200
    }


Submit Dispute Evidence
------------------------
Submits the current evidence batch for review.

**Usage Example**

.. code-block:: python

    response = disputes_api.submit_dispute_evidence(dispute_token="dispute_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "status": "submitted"
        },
        "status": 200
    }


Accept Dispute
--------------
Accepts a dispute resolution without submitting evidence.

**Usage Example**

.. code-block:: python

    response = disputes_api.accept_dispute(dispute_token="dispute_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "status": "accepted"
        },
        "status": 200
    }

.. tip:: Learn More

    To learn more about disputes functionality, refer to: :mod:`pin_payments.disputes`