# Python-Pin-Payments Library

## Documentation

[![Documentation Status](https://readthedocs.org/projects/python-pin-payments/badge/?version=latest)](https://python-pin-payments.readthedocs.io/en/latest/overview.html)
---
The full documentation is available [here](https://python-pin-payments.readthedocs.io/en/latest/overview.html).

## Overview

The Python-Pin-Payments library is a comprehensive tool designed to interact with the Pin Payments API.
It simplifies the process of handling payment operations, including charges, customer management, and refunds.
This library encompasses several modules:

- **Charges**: For creating and managing payment card charges.
- **Customers**: To store and manage customer information and their payment details.
- **Refunds**: Allows refunding charges and retrieving details of previous refunds.


## Installation

This framework is published at the PyPI, install it with pip:

```bash
pip install python-pin-payments
```

## Installation using Poetry

Poetry is a tool for dependency management and packaging in Python. To set up and use the Python-Pin-Payments library
with Poetry:

### Install Poetry

If Poetry is not already installed, follow the instructions on
the [Poetry website](https://python-poetry.org/docs/#installation).

### Create and Configure a New Project

If starting a new project:

```bash
poetry new python-pin-payments-project
cd python-pin-payments-project
```

### Activate the Virtual Environment

Activate the virtual environment created by Poetry:

```bash
poetry shell
```

### Add Python-Pin-Payments Library

Add the library as a dependency:

- poetry installation:

```bash
poetry add python-pin-payments
```

- Alternative way of installing from the repository

```bash
poetry add git+https://github.com/Onix-Systems/python-pin-payments
```

### Install Dependencies

Install all necessary dependencies:

```bash
poetry install
```

## Configuration and Initialization

### Configuration

Before using the Refunds API, you must configure it with your API key:

```python
from pin_payments import Refunds

api_key = "your-api-key"
refunds_api = Refunds(api_key=api_key)
```

### Test Purposes (devs only)

create `.env` file
set up the `API_KEY` to write it to the environment

### Initialization

Instantiate the Refunds class with your secret API key:

```python
refunds_api = Refunds(api_key="your-secret-api-key")
```

## API Usage - Retrieving and Creating Refunds

### Retrieve All Refunds

To get a paginated list of all refunds:

```python
all_refunds = refunds_api.list()
```

### Retrieve a Specific Refund

Fetch details of a particular refund using its token:

```python
refund_details = refunds_api.details(refund_token="rf_123456789")
```

### Issue a Refund

Create a new refund on a specific charge:

```python
new_refund = refunds_api.create_refund(
	charge_token="ch_123456789",
	amount=5000  # Refund amount in the smallest currency unit (e.g., cents for AUD)
)
```

### Retrieve Refunds for a Specific Charge

List all refunds made for a specific charge:

```python
charge_refunds = refunds_api.list_charge(charge_token="ch_123456789")
```

## Error Handling and Logging

### Error Handling

The library will return detailed error messages in case of failure. Ensure to handle these errors gracefully in your
code:

```python
response = refunds_api.list()
if 'error' in response:
	logging.error(f"Refund retrieval failed with error: {response['error']}")
else:
# Process successful response
```

### Logging

Logging is crucial for monitoring API interactions. Set up logging at the beginning of your application:

```python
import logging

logging.basicConfig(level=logging.INFO)
```

## Development and Testing

### Development

Contributions to the library are encouraged. When developing additional features or fixing bugs:

1. Clone the repository and create a new branch for your changes.
2. Write your code following the existing code style and conventions.
3. Add or update tests as necessary.

### Testing

Before submitting your changes, ensure all tests pass:

```shell
pytest
```

## Support and Contribution Guidelines

### Support

If you encounter any issues or require assistance, please file an issue on the repository's issue tracker. Ensure to
provide a detailed description of the problem, including steps to reproduce, input data, and any relevant logs or error
messages.

### Contributing

We welcome contributions from the community. To contribute to the library:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Write clean code and adhere to the existing coding standards.
4. Write appropriate tests for your changes.
5. Ensure all tests pass.
6. Submit a pull request with a clear description of your changes.

### Code of Conduct

Respect the Code of Conduct and interact with other contributors professionally. Contributions should be made in a
spirit of collaboration, not competition.

## Release Notes and FAQs

### Release Notes

Keep a section for release notes to inform users about new features, bug fixes, and improvements in each version.
Example:

```markdown
### Version 1.0.0

- Project Initialization
```

### FAQs

A Frequently Asked Questions (FAQ) section can be helpful for users. Include answers to common questions about the
library. Example:

```markdown
**Q: Can I process refunds in different currencies?**  
A: Yes, the library supports multi-currency transactions. Ensure the currency is supported by the API.

**Q: How do I handle network errors gracefully?**  
A: The library includes detailed logging. It's recommended to log errors and retry the request if appropriate.

**Q: Where can I find my API key?**  
A: API keys are available in your Pin Payments dashboard. Never expose your secret API key publicly.
```

### Additional Resources

Provide links to external resources, such as API documentation, community forums, or related libraries:

```markdown
- [Pin Payments API Documentation](https://docs.pinpayments.com/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [Stack Overflow - Tagged Questions](https://stackoverflow.com/questions/tagged/pin-payments)
```

## Charges API

### Overview

**Charges** handles the creation, management, and retrieval of payment card charges. It allows for various operations
such as listing all charges, creating new charges, capturing authorized charges, and more.

### Usage

#### Create a New Charge

```python
charge = charges_api.create(
	email="customer@example.com",
	description="Order #1234",
	amount=5000,
	ip_address="203.0.113.0",
	currency="AUD",
	card={
		"number": "5520000000000000",
		"expiry_month": "05",
		"expiry_year": "2023",
		"cvc": "123",
		"name": "Cardholder Name",
		"address_line1": "123 Main St",
		"address_city": "Anytown",
		"address_state": "State",
		"address_country": "Country"
	}
)
```

#### Retrieve a List of All Charges

```python
charges_list = charges_api.list()
```

## Customers API

### Overview

**Customers** is designed for storing and managing customer information and their payment details. It supports multiple
operations including creating new customers, updating customer information, and managing their payment methods.

### Usage

#### Create a New Customer

```python
new_customer = customers_api.create(
	email="customer@example.com",
	first_name="Jane",
	last_name="Doe",
	card={
		"number": "5520000000000000",
		"expiry_month": "12",
		"expiry_year": "2024",
		"cvc": "123",
		"name": "Jane Doe",
		"address_line1": "123 Main St",
		"address_city": "Anytown",
		"address_postcode": "123456",
		"address_state": "State",
		"address_country": "Country"
	}
)
```

#### Retrieve a Customer's Details

```python
customer_details = customers_api.details(customer_token="cus_token")
```

# Currency Module Documentation

## Overview

This module is designed for representing and managing various currencies. It includes classes for defining currency
codes, their properties like base unit, and minimum transaction amounts.

## Classes

### `CurrencyCode`

An enumeration representing the codes of available currencies.

#### Attributes:

- `AUD`: Australian Dollar
- `USD`: United States Dollar
- `NZD`: New Zealand Dollar
- `SGD`: Singaporean Dollar
- `EUR`: Euro
- `GBP`: Pound Sterling
- `CAD`: Canadian Dollar
- `HKD`: Hong Kong Dollar
- `JPY`: Japanese Yen
- `MYR`: Malaysian Ringgit
- `THB`: Thai Baht
- `PHP`: Philippine Peso
- `ZAR`: South African Rand
- `IDR`: Indonesian Rupiah
- `TWD`: New Taiwan Dollar

### `Currency`

A class representing a currency with all its properties.

#### Parameters:

- `code` (`CurrencyCode`): Currency code.
- `base_unit` (`str`): Base unit of the currency.
- `min_amount` (`int`): Minimum amount for a transaction in this currency.

#### Attributes:

- `code` (`CurrencyCode`): Currency code.
- `base_unit` (`str`): Base unit of the currency.
- `min_amount` (`int`): Minimum amount for a transaction.

### `Currencies`

A class that encapsulates all currencies.

#### Attributes:

- `AUD`: Currency object for the Australian Dollar.
- `USD`: Currency object for the United States Dollar.
- ... (and so on for other currencies).

## Example Usage:

```python
if __name__ == '__main__':
	print(
		f"Code: {Currencies.AUD.code.value}, "
		f"Base Unit: {Currencies.AUD.base_unit}, "
		f"Min Amount: {Currencies.AUD.min_amount}"
	)
```

# Recipients API Module

## Overview

The Recipients API module enables storage and retrieval of transfer recipient details. This module facilitates fund
transfers to recipients using the transfer API.

## Initialization

Create an instance of the Recipients class with your API key.

The bank account should be valid.

```python
recipients_api = Recipients(api_key='your-api-key')
```

## Methods

### create

Creates a new recipient and returns its details.

```python
response = recipients_api.create(
	email='email@example.com',
	name='Recipient Name',
	bank_account={
		'name': 'Recipient Name',
		'bsb': '123456',
		'number': '123456789'
	},
	bank_account_token='bank_account_token'
)
```

**Arguments**:

- `email` (str): Email address of the recipient.
- `name` (str, optional): Name for this recipient.
- `bank_account` (dict, optional): Full details of the bank account to be stored.
- `bank_account_token` (str, optional): Token of the bank account to be stored.

### list

Returns a paginated list of all recipients.

```python
response = recipients_api.list()
```

### get_details

Returns the details of a recipient.

```python
response = recipients_api.get_details(recipient_token='recipient_token')
```

**Arguments**:

- `recipient_token` (str): Token of the recipient.

### update

Updates the details of a recipient and returns its new details.

```python
response = recipients_api.update(
	recipient_token='recipient_token',
	email='new_email@example.com',
	bank_account={
		'name': 'New Recipient Name',
		'bsb': '654321',
		'number': '987654321'
	},
	bank_account_token='new_bank_account_token'
)
```

**Arguments**:

- `recipient_token` (str): Token of the recipient.
- `email` (str, optional): New email address of the recipient.
- `bank_account` (dict, optional): New full details of the bank account to be stored.
- `bank_account_token` (str, optional): New token of the bank account to be stored.

### list_transfers

Returns a paginated list of a recipient’s transfers.

```python
response = recipients_api.list_transfers(recipient_token='recipient_token')
```

**Arguments**:

- `recipient_token` (str): Token of the recipient.

## Example Usage

```python
# Create a new recipient
recipients_api.create(email="example@email.com")

# List all recipients
recipients_api.list()

# Get details of a specific recipient
recipients_api.get_details(recipient_token="your-recipient-token")

# Update a recipient's details
recipients_api.update(recipient_token="your-recipient-token")

# List transfers for a specific recipient
recipients_api.list_transfers(recipient_token="your-recipient-token")
```

# Transfers Module Documentation

## Overview

The `Transfers` module is a part of the Pin Payments API that allows sending money to Australian bank accounts and
retrieving details of previous transfers. This module is designed to be used within a broader payment processing system.

## Class: Transfers

This class provides methods to interact with the Pin Payments Transfers API.

### Initialization

```python
transfers_api = Transfers(api_key, mode)
```

- `api_key` (str): Your API key for Pin Payments.
- `mode` (str): Mode of operation, either 'live' or 'test'.

### Methods

#### create

Create a new transfer.

```python
response = transfers_api.create(description, amount, currency, recipient)
```

- `description` (str): Description of the transfer.
- `amount` (int): Amount to transfer in the currency's base unit.
- `currency` (str): Currency of the transfer.
- `recipient` (str): Recipient's token or 'self' for own account.

#### list

List all transfers.

```python
response = transfers_api.list()
```

#### search

Search transfers with criteria.

```python
response = transfers_api.search(query, start_date, end_date, sort, direction)
```

- `query` (Optional[str]): Search query.
- `start_date` (Optional[str]): Start date for filtering.
- `end_date` (Optional[str]): End date for filtering.
- `sort` (Optional[str]): Field to sort by.
- `direction` (Optional[int]): Sort direction.

#### details

Get details of a specific transfer.

```python
response = transfers_api.details(transfer_token)
```

- `transfer_token` (str): Token of the transfer.

#### line_items

Get line items of a specific transfer.

```python
response = transfers_api.line_items(transfer_token)
```

- `transfer_token` (str): Token of the transfer.

## Usage Example

```python
transfers_api = Transfers(api_key='your_api_key')
transfers_api.create(description='Transfer for service', amount=1000, currency='AUD', recipient='recipient_token')
transfers_api.list()
transfers_api.search(query='service')
transfers_api.details('transfer_token')
transfers_api.line_items('transfer_token')
```

# Balance API Documentation

## Overview

The Balance API module provides an interface to view the current balance of funds in your Pin Payments account. It is
useful for confirming the availability of funds before initiating transfers.

## Class: Balance

This class inherits from the Base class and is responsible for interacting with the Pin Payments balance API.

### Initialization

```python
balance_api = Balance(api_key: str, mode: str = 'live')
```

- `api_key`: Your Pin Payments API key.
- `mode`: The mode of operation, either 'live' or 'test'.

### Methods

#### detail()

This method retrieves the current balance of the Pin Payments account.

```python
response = balance_api.detail()
```

- `Returns`: A dictionary containing the balance details.

#### Example Usage

```python
balance_api = Balance(api_key='your_api_key', mode='live')
balance_details = balance_api.detail()
print(balance_details)
```

This will output the current balance details of the Pin Payments account associated with the provided API key.

## Plans API

The `Plans` class in the `pin_payments` module provides an interface to create, modify, and examine recurring billing
plans using the Pin Payments API.

### Initialization

```python
plans_api = Plans(api_key='your_api_key', mode='live')
```

- `api_key`: Your secret API key for Pin Payments.
- `mode`: Mode of operation, either `'live'` or `'test'`. Default is `'live'`.

### Methods

#### `create`

Creates a new billing plan.

```python
response = plans_api.create(
	name='Plan Name',
	amount=1000,
	interval=30,
	interval_unit='day',
	currency='AUD',
	intervals=12,
	setup_amount=100,
	trial_amount=0,
	trial_interval=7,
	trial_interval_unit='day',
	customer_permissions=['cancel']
)
```

#### `list`

Returns a paginated list of all plans.

```python
response = plans_api.list()
```

#### `details`

Retrieves details of a specified plan.

```python
response = plans_api.details(plan_token='plan_token')
```

#### `update`

Updates a specified plan.

```python
response = plans_api.update(
	plan_token='plan_token',
	name='New Plan Name',
	customer_permissions=['cancel']
)
```

#### `delete`

Deletes a specified plan and all of its subscriptions.

```python
response = plans_api.delete(plan_token='plan_token')
```

#### `create_subscription`

Creates a new subscription to a specified plan.

```python
response = plans_api.create_subscription(
	plan_token='plan_token',
	customer_token='customer_token',
	card_token='card_token',
	include_setup_fee=True
)
```

#### `list_subscriptions`

Lists all subscriptions for a specified plan.

```python
response = plans_api.list_subscriptions(plan_token='plan_token')
```

# Merchants API Documentation

## Overview

The Merchants API allows you to examine merchants you have referred to us. Access to this API requires a partner API
key, available to approved partners.

## Class `Merchants`

### Method: `create`

- Creates a new referred merchant in the system and returns a confirmation.
- Parameters:
    - `contact` (dict): Personal details of the user logging into the merchant entity account.
    - `entity` (dict): Legal operating details of the merchant entity.
    - `business` (dict): Business details of the merchant entity.
    - `bank_account` (dict): Full details of the bank account for fund settlement.
    - `director` (dict): Details of a person legally responsible for the merchant entity.
    - `notes` (Optional[str]): Additional information to support the merchant’s application.
- Example Request:
  ```python
  response = merchants_api.create(
      contact={
          "first_name": "Roland",
          "last_name": "Robot",
          "phone_number": "02 9876 5432",
          "email": "roland@pinpayments.com",
          "password": "new-user-password"
      },
      entity={
          "business_registration_number": "11223491505",
          "full_legal_name": "Roland Robot's coffee robots",
          "address_line_1": "58 Durham Rd",
          "address_locality": "Kilsyth",
          "address_region": "VIC",
          "address_postal_code": "3137",
          "address_country_code": "AU"
      },
      business={
          "trading_name": "Roland Robot's coffee robots",
          "description": "We sell robots that make coffee",
          "typical_product_price": 1000,
          "transactions_per_month": 100,
          "annual_transaction_volume": 1000000,
          "sells_physical_goods": True,
          "average_delivery_days": 14,
          "url": "https://rrcr.net.au"
      },
      bank_account={
          "name": "RRCR",
          "bsb": "182222",
          "number": "000111111"
      },
      director={
          "full_name": "Roland Robot",
          "contact_number": "02 9876 5432",
          "date_of_birth": "1984-06-12"
      },
      notes="Some additional notes here"
  )
  ```

### Method: `list`

- Returns a paginated list of all the merchants referred by you.
- Example Request:
  ```python
  response = merchants_api.list()
  ```

### Method: `details`

- Returns the details of a specified merchant referred by you.
- Parameters:
    - `merchant_token` (str): Token of the merchant.
- Example Request:
  ```python
  response = merchants_api.details(merchant_token='mrch_roland')
  ```

### Method: `default_settings`

- Returns the default settings that will be applied to new merchants referred by you.
- Example Request:
  ```python
  response = merchants_api.default_settings()
  ```

# Bank Accounts API

The Bank Accounts API allows for securely storing bank account details in exchange for a bank account token. This API is
suitable for scenarios where you need to store bank account details securely and use them in operations like creating
recipients.

## Usage

```python
from pin_payments import BankAccounts

api_key = 'your-api-key'
bank_accounts_api = BankAccounts(api_key)

response = bank_accounts_api.create(
	name='John Doe',
	bsb='123456',
	number='987654321',
	publishable_api_key='your-publishable-api-key'  # Optional for insecure environments
)

print(response)
```

### Method: create

- **Description**: Creates a bank account token and returns its details.
- **Parameters**:
    - `name` (str): The account holder's name.
    - `bsb` (str): The BSB code of the bank account.
    - `number` (str): The account number of the bank account.
    - `publishable_api_key` (Optional[str]): Publishable API key for insecure environments.
- **Returns**: A dictionary with the bank account token and its details.

# Deposits API Documentation

## Overview

The Deposits API allows you to retrieve details of deposits made to your account. It is part of the Pin Payments
service.

## Initialization

```python
from pin_payments.deposits import Deposits

deposits_api = Deposits(api_key="your_api_key", mode="live")
```

## Methods

### List All Deposits

Returns a paginated list of all deposits made to your account.

```python
response = deposits_api.list()
```

### Deposit Details

Fetches the details of a specific deposit by its token.

```python
response = deposits_api.details(deposit_token="your_deposit_token")
```

## Response Format

Responses are returned in dictionary format with key-value pairs corresponding to the deposit details.

## Events API

The `Events` class in the module provides functionality to interact with the Events API, allowing users to view
activities on their account. It supports listing all events and retrieving details of specific events.

### Methods

- `list()`: Returns a paginated list of all events. It performs a `GET` request to the `/events` endpoint and returns a
  dictionary of the response.
- `details(event_token: str)`: Retrieves the details of a specified event. It accepts an `event_token` as a parameter
  and performs a `GET` request to `/events/{event_token}`. The response is returned as a dictionary.

### Usage

To use the `Events` class, initialize it with your API key and optionally specify the mode ('live' or 'test'). Then,
call its methods to interact with the API.

```python
events_api = Events(api_key="your_api_key")
all_events = events_api.list()
event_details = events_api.details(event_token="your_event_token")
```

### Event Types

The module also includes the `EventType` enumeration, providing a comprehensive list of all possible event types that
can be encountered, such as `charge.authorised`, `customer.created`, and many more.

## Disputes API Documentation

The `Disputes` class in the `pin_payments` package provides an interface to interact with the Disputes API. This API
allows you to retrieve details of disputes against your charges and perform actions to either challenge or accept them.

### Initialization

Before using the Disputes API, initialize the `Disputes` class with your API key.

```python
from pin_payments import Disputes

api_key = 'your_api_key'
disputes_api = Disputes(api_key=api_key)
```

### Methods

#### List Disputes

Retrieve a paginated list of all disputes, optionally sorted by a specified field in ascending or descending order.

```python
response = disputes_api.list_disputes(sort='received_at', direction=1)
```

#### Search Disputes

Search for disputes matching specific criteria such as query term, status, and sorting parameters.

```python
response = disputes_api.search_disputes(query='chargeback', status='open', sort='amount', direction=-1)
```

#### Get Dispute Details

Get the details of a specific dispute by providing its unique token.

```python
dispute_token = 'dis_JRs6Xgk4jMyF33yGijQ7Nw'
response = disputes_api.get_dispute_details(dispute_token)
```

#### Get Dispute Activity

Retrieve the activity feed for a specific dispute by its token.

```python
response = disputes_api.get_dispute_activity(dispute_token)
```

#### Get Dispute Evidence

Displays the current evidence batch for a specific dispute identified by its token.

```python
response = disputes_api.get_dispute_evidence(dispute_token)
```

#### Update Dispute Evidence

Update the evidence batch for a specific dispute. Provide the dispute token and a dictionary of evidence data.

```python
evidence_data = {'proof_of_delivery_or_service': 'Delivered on 2023-09-25', 'invoice_or_receipt': 'Invoice #123456'}
response = disputes_api.update_dispute_evidence(dispute_token, evidence_data)
```

#### Submit Dispute Evidence

Submit the current evidence batch of a specific dispute for review.

```python
response = disputes_api.submit_dispute_evidence(dispute_token)
```

#### Accept Dispute

Accept a specific dispute by its token.

```python
response = disputes_api.accept_dispute(dispute_token)
```

# Webhooks API Documentation

## Overview

The Webhooks API provided by the `Webhooks` class in `pin_payments` package allows for the management and replay of
webhooks. This API is essential for handling requests sent to your webhook endpoints by Pin Payments in response to
various events.

## Usage

### Initialization

To use the Webhooks API, you need to initialize the `Webhooks` class with your API key.

```python
from pin_payments import Webhooks

webhooks_api = Webhooks(api_key="your_api_key")
```

### Listing All Webhooks

To retrieve a paginated list of all webhooks:

```python
response = webhooks_api.list_webhooks()
```

### Getting Webhook Details

To get the details of a specific webhook by its token:

```python
response = webhooks_api.get_webhook_details(webhook_token="your_webhook_token")
```

### Replaying a Webhook

To replay a webhook:

```python
response = webhooks_api.replay_webhook(webhook_token="your_webhook_token")
```

This will send a request to the URL of the webhook again, useful for testing or in case of errors.

## Webhook Endpoints API Documentation

### Overview

The `WebhookEndpoints` class in the `pin_payments` package provides methods for managing webhook endpoints in the Pin
Payments API. Webhook endpoints are URLs that Pin Payments requests when events occur on your account.

### Initialization

```python
from pin_payments import WebhookEndpoints

api_key = 'your_api_key'
webhook_endpoints_api = WebhookEndpoints(api_key)
```

### Methods

#### Create Webhook Endpoint

Create a new webhook endpoint and return its details.

- **Method**: `create_webhook_endpoint(url)`
- **Arguments**:
    - `url`: The destination URL of the webhook endpoint.

```python
response = webhook_endpoints_api.create_webhook_endpoint(url='https://example.org/webhooks/')
```

#### List Webhook Endpoints

Return a paginated list of all webhook endpoints.

- **Method**: `list_webhook_endpoints()`

```python
response = webhook_endpoints_api.list_webhook_endpoints()
```

#### Get Webhook Endpoint Details

Return the details of a specific webhook endpoint.

- **Method**: `get_webhook_endpoint_details(webhook_endpoint_token)`
- **Arguments**:
    - `webhook_endpoint_token`: Token of the webhook endpoint.

```python
response = webhook_endpoints_api.get_webhook_endpoint_details(webhook_endpoint_token='token_here')
```

#### Delete Webhook Endpoint

Delete a webhook endpoint and all of its webhook requests.

- **Method**: `delete_webhook_endpoint(webhook_endpoint_token)`
- **Arguments**:
    - `webhook_endpoint_token`: Token of the webhook endpoint to be deleted.

```python
response = webhook_endpoints_api.delete_webhook_endpoint(webhook_endpoint_token='token_here')
```

# Authorisations API

The Authorisations API provides a robust solution for managing payment card authorisations, including creating new
authorisations, retrieving details of previous ones, voiding existing authorisations, and capturing authorised funds.
This API is designed to streamline the payment process, ensuring secure and efficient transactions.

## Initialization

To use the Authorisations API, initialize it with your API key and the desired mode (`live` or `test` for sandbox
testing):

```python
from authorisations import Authorisations

api_key = "your_api_key_here"
authorisations_api = Authorisations(api_key=api_key, mode='test')
```

## Creating a New Authorisation

Create a new payment card authorisation by providing details such as the purchaser's email, a description of the item
purchased, the amount, and the IP address:

```python
response = authorisations_api.create_authorisation(
	email="purchaser@example.com",
	description="500g of single origin coffee beans",
	amount=2500,
	ip_address="203.0.113.0",
	currency="AUD",
	card={
		"number": "5520000000000000",
		"expiry_month": "05",
		"expiry_year": "2025",
		"cvc": "123",
		"name": "Jane Doe",
		"address_line1": "123 Main St",
		"address_city": "Anytown",
		"address_postcode": "12345",
		"address_state": "State",
		"address_country": "Country"
	}
	# Alternatively, use card_token or customer_token if available
)
```

## Voiding an Authorisation

To void a previously created authorisation:

```python
response = authorisations_api.void_authorisation(auth_token="auth_token_here")
```

## Capturing Authorised Funds

Capture the authorised funds with the specific amount:

```python
response = authorisations_api.capture_authorisation(
	auth_token="auth_token_here",
	amount=1500
)
```

## Listing All Authorisations

Retrieve a paginated list of all authorisations:

```python
response = authorisations_api.list_authorisations()
```

## Getting Authorisation Details

Retrieve the details of a specific authorisation by its token:

```python
response = authorisations_api.get_authorisation_details(auth_token="auth_token_here")
```

# Subscriptions API

The Subscriptions API facilitates the management of subscription services, allowing for the creation of new
subscriptions, retrieval of subscription details, updating subscription information, reactivation of subscriptions, and
cancellation of active or trial subscriptions. This comprehensive API is designed to integrate seamlessly with your
existing payment and subscription management systems.

## Getting Started

First, initialize the Subscriptions API with your API key and the desired operation mode (`live` or `test`):

```python
from subscriptions import Subscriptions

api_key = "your_secret_api_key"
subscriptions_api = Subscriptions(api_key=api_key, mode='test')
```

## Create a New Subscription

To activate a new subscription, provide the plan token, customer token, and whether to include the setup fee:

```python
response = subscriptions_api.create_subscription(
	plan_token='plan_token_here',
	customer_token='customer_token_here',
	include_setup_fee=True
)
```

## List All Subscriptions

Retrieve a paginated list of all subscriptions:

```python
response = subscriptions_api.list_subscriptions()
```

## Get Subscription Details

Fetch the details of a specific subscription using its subscription token:

```python
sub_token = 'subscription_token_here'
response = subscriptions_api.get_subscription_details(sub_token)
```

## Update a Subscription

Update the card associated with a specific subscription:

```python
sub_token = 'subscription_token_here'
card_token = 'new_card_token_here'
response = subscriptions_api.update_subscription(sub_token, card_token)
```

## Cancel a Subscription

Cancel an active or trial subscription:

```python
sub_token = 'subscription_token_here'
response = subscriptions_api.cancel_subscription(sub_token)
```

## Reactivate a Subscription

Reactivate a previously canceled subscription:

```python
sub_token = 'subscription_token_here'
response = subscriptions_api.reactivate_subscription(sub_token, include_setup_fee=True)
```

## Fetch Subscription Ledger

Retrieve ledger entries related to a specific subscription:

```python
sub_token = 'subscription_token_here'
response = subscriptions_api.fetch_subscription_ledger(sub_token)
```

## Files API Documentation

The Files API provides functionalities for managing file uploads within your application. It supports operations such as
uploading new files, retrieving details about uploaded files, and deleting files by their tokens.

### Uploading a New File

To upload a new file, use the `upload_file` method. This method requires the local path to the file you wish to upload
and the purpose of the file upload, such as 'dispute_evidence'.

```python
response = files_api.upload_file('/path/to/your/file.jpeg', 'dispute_evidence')
```

### Retrieving File Details

To retrieve details about an uploaded file, use the `get_file_details` method with the file token.

```python
file_token = 'file_M3wowEURfIpSQI6xCEoamQ'
response = files_api.get_file_details(file_token)
```

### Deleting a File

To delete an uploaded file, use the `delete_file` method with the file token.

```python
file_token = 'file_M3wowEURfIpSQI6xCEoamQ'
response = files_api.delete_file(file_token)
```

# Apple Pay API Documentation

## Overview

The `ApplePayAPI` class provides methods to manage Apple Pay merchant domains and sessions, including creating, listing,
and deleting domains, checking domain registration, creating Apple Pay sessions, and managing Apple Pay certificates.

## Initialization

```python
from apple_pay_api import ApplePayAPI

apple_pay_api = ApplePayAPI(api_key="your_api_key", mode="test")
```

## Create Domain

Registers a new domain for Apple Pay.

```python
response = apple_pay_api.create_domain(domain_name="example.com")
```

## List Domains

Retrieves a list of all registered Apple Pay domains.

```python
response = apple_pay_api.list_domains()
```

## Delete Domain

Deletes a registered Apple Pay domain.

```python
response = apple_pay_api.delete_domain(domain_token="domain_token_here")
```

## Check Host

Checks if an Apple Pay domain is registered.

```python
response = apple_pay_api.check_host(domain_name="example.com")
```

## Create Session

Creates an Apple Pay session.

```python
response = apple_pay_api.create_session(
	validation_url="validation_url_here",
	initiative="web",
	initiative_context="example.com"
)
```

## Create Certificate

Creates a new Apple Pay certificate.

```python
response = apple_pay_api.create_certificate()
```

## List Certificates

Retrieves a list of all Apple Pay certificates.

```python
response = apple_pay_api.list_certificates()
```

## Get Certificate

Retrieves details of a specific Apple Pay certificate.

```python
response = apple_pay_api.get_certificate(certificate_token="certificate_token_here")
```

## Upload Certificate

Uploads an Apple Pay payment processing certificate.

```python
response = apple_pay_api.upload_certificate(certificate_pem="certificate_pem_here")
```

## Delete Certificate

Deletes an Apple Pay certificate.

```python
response = apple_pay_api.delete_certificate(certificate_token="certificate_token_here")
```

## Payment Sources API Integration

The Payment Sources API module allows for the secure storage of payment source details, returning a token that can be
used for creating charges. This is crucial for handling different types of payment sources like cards, Apple Pay, Google
Pay, and network tokens.

### Initialization

To use the Payment Sources API, initialize the `PaymentSources` class with your API key and the desired mode ('live'
or 'test').

```python
from payment_sources import PaymentSources

payment_sources_api = PaymentSources(api_key="your_api_key", mode="test")
```

### Creating a Payment Source

You can store payment source details by calling the `create_payment_source` method. This method accepts the type of
payment source (`card`, `applepay`, `googlepay`, `network_token`), the source details as a dictionary, and optionally, a
publishable API key for requests from insecure environments.

#### Example: Creating a Card Payment Source

```python
card_details = {
	"number": "5520000000000000",
	"expiry_month": "05",
	"expiry_year": "2025",
	"cvc": "123",
	"name": "Roland Robot",
	"address_line1": "42 Sevenoaks St",
	"address_city": "Lathlain",
	"address_postcode": "6454",
	"address_state": "WA",
	"address_country": "Australia"
}
response = payment_sources_api.create_payment_source("card", card_details)
```

#### Example: Creating an Apple Pay Payment Source

```python
apple_pay_details = {
	"data": "encrypted_data",
	"signature": "signature_value",
	"header": {
		"publicKeyHash": "hash_value",
		"ephemeralPublicKey": "public_key",
		"transactionId": "transaction_id"
	},
	"version": "EC_v1"
}
response = payment_sources_api.create_payment_source("applepay", apple_pay_details)
```

# Charge Service Module Documentation (Test Cards on pinpayments)

## Overview

This module provides a simple interface for simulating transactions with different types of test credit cards. It allows
the simulation of various scenarios such as successful transactions, declined transactions, insufficient funds, invalid
CVV, and more.

## Classes

- `CardType`: An enumeration of possible types of card responses.
- `TestCard`: Represents a test card with a specific card number and type.
- `TestCards`: A collection of predefined test cards.
- `ChargeService`: A service to create charges with test cards.

## Usage

### Creating a Charge

To create a charge, you can use the `ChargeService.create_charge` method. This method requires a card number and an
amount. It returns a dictionary with the transaction result.

```python
from charge_service import ChargeService

card_number = "4200000000000000"
amount = 100

response = ChargeService.create_charge(card_number, amount)
```

### Handling Different Card Types

You can simulate different outcomes by using different card numbers. Here are some examples:

- **Successful Transaction**:
    - Card Number: `"4200000000000000"`
    - Response: `{'success': True, 'token': 'ch_lfUYEBK14zotCTykezJkfg', 'amount': amount}`

- **Declined Transaction**:
    - Card Number: `"4100000000000001"`
    - Response:
      `{'error': 'declined', 'error_description': 'The card was declined', 'charge_token': 'ch_lfUYEBK14zotCTykezJkfg'}`

- **Insufficient Funds**:
    - Card Number: `"4000000000000002"`
    - Response:
      `{'error': 'insufficient_funds', 'error_description': 'There are not enough funds available to process the requested amount', 'charge_token': 'ch_lfUYEBK14zotCTykezJkfg'}`

### Error Descriptions

The `TestCards.get_error_description` static method provides a human-readable description of the error based on the card
type.

## Test Cards

The module includes a variety of test cards for different scenarios. Each card is associated with a specific behavior,
such as being declined, having insufficient funds, etc.

For a full list of test cards and their behaviors, please refer to the `TestCards.cards` list within the module.
