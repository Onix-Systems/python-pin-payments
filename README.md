
# Python-Pin-Payments Library

## Overview

The Python-Pin-Payments library is a comprehensive tool designed to interact with the Pin Payments API. It simplifies the process of handling payment operations, including charges, customer management, and refunds. This library encompasses several modules:

- **Charges**: For creating and managing payment card charges.
- **Customers**: To store and manage customer information and their payment details.
- **Refunds**: Allows refunding charges and retrieving details of previous refunds.

## Installation using Poetry

Poetry is a tool for dependency management and packaging in Python. To set up and use the Python-Pin-Payments library with Poetry:

### Install Poetry

If Poetry is not already installed, follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

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

- If published on PyPI:

```bash
poetry add python-pin-payments
```

- For a local or git version:

```bash
poetry add git+https://gitlab.onix.ua/onix-systems/python-pin-payments.git#master
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

The library will return detailed error messages in case of failure. Ensure to handle these errors gracefully in your code:

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

If you encounter any issues or require assistance, please file an issue on the repository's issue tracker. Ensure to provide a detailed description of the problem, including steps to reproduce, input data, and any relevant logs or error messages.

### Contributing

We welcome contributions from the community. To contribute to the library:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Write clean code and adhere to the existing coding standards.
4. Write appropriate tests for your changes.
5. Ensure all tests pass.
6. Submit a pull request with a clear description of your changes.

### Code of Conduct

Respect the Code of Conduct and interact with other contributors professionally. Contributions should be made in a spirit of collaboration, not competition.

## Release Notes and FAQs

### Release Notes

Keep a section for release notes to inform users about new features, bug fixes, and improvements in each version. Example:

```markdown
### Version 1.0.0
- Project Initialization
```

### FAQs

A Frequently Asked Questions (FAQ) section can be helpful for users. Include answers to common questions about the library. Example:

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

**Charges** handles the creation, management, and retrieval of payment card charges. It allows for various operations such as listing all charges, creating new charges, capturing authorized charges, and more.

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

**Customers** is designed for storing and managing customer information and their payment details. It supports multiple operations including creating new customers, updating customer information, and managing their payment methods.

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
This module is designed for representing and managing various currencies. It includes classes for defining currency codes, their properties like base unit, and minimum transaction amounts.

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
The Recipients API module enables storage and retrieval of transfer recipient details. This module facilitates fund transfers to recipients using the transfer API.

## Initialization
Create an instance of the Recipients class with your API key.

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

