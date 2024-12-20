Bank Accounts API
=================

The `BankAccounts` API allows you to securely store bank account details in exchange for a bank account token.


To initialize the `BankAccounts` API, use the following:

.. code-block:: python

    from bank_accounts import BankAccounts
    from config import get_api_key

    # Initialize the API with your API key and mode
    bank_accounts_api = BankAccounts(api_key=get_api_key(), mode='test')



Create
------
Creates a bank account token and stores bank account details securely.

**Usage Example**

.. code-block:: python

    response = bank_accounts_api.create(
        name="John Doe",
        bsb="123-456",
        number="123456789"
    )
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "bank_acc_token_example",
            "bsb": "123-456",
            "number": "123456789",
            "name": "John Doe"
        },
        "status": 201
    }

.. tip:: Learn More

    To learn more about bank accounts functionality, refer to: :mod:`pin_payments.bank_accounts`