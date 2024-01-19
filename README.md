
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


# Transfers Module Documentation

## Overview
The `Transfers` module is a part of the Pin Payments API that allows sending money to Australian bank accounts and retrieving details of previous transfers. This module is designed to be used within a broader payment processing system.

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
The Balance API module provides an interface to view the current balance of funds in your Pin Payments account. It is useful for confirming the availability of funds before initiating transfers.

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
