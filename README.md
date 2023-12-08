### Charges API

The charges API allows you to create new payment card charges and retrieve details of previous charges.

`POST	/charges`

Creates a new charge and returns its details

`PUT	/charges/charge-token/void`

Voids a previously authorised charge and returns its details

`PUT	/charges/charge-token/capture`
Captures a previously authorised charge and returns its details

`GET	/charges`

Returns a paginated list of all charges

`GET	/charges/search`

Returns a paginated list of charges matching the search criteria

`GET	/charges/charge-token`

Returns the details of a charge

`GET	/charges/verify?session_token=session-token`

Verify the result of a 3D Secure enabled charge

---

### Customers API

`POST	/customers`	

Creates a new customer and returns its details

`GET	/customers`

Returns a paginated list of all customers

`GET	/customers/customer-token`

Returns the details of a customer

`PUT	/customers/customer-token`

Updates the details of a customer and returns the updated details

`DELETE	/customers/customer-token`

Deletes a customer and all of its cards. You will not be able to recover them

`GET	/customers/customer-token/charges`

Returns a paginated list of a customer’s charges

`GET	/customers/customer-token/cards`

Returns a paginated list of a customer’s cards

`POST	/customers/customer-token/cards`

Creates an additional card for the specified customer and returns its details

`DELETE	/customers/customer-token/cards/card-token`

Deletes a customer’s non-primary card. You will not be able to recover it

`GET	/customers/customer-token/subscriptions`

Retrieves the specified customer's subscriptions

`DELETE	/customers/customer-token/subscriptions/sub-token`

Cancels the subscription identified by subscription token. Subscriptions can only be cancelled if they are in trial or active state

---

### Refunds API

`GET	/refunds`

Returns a paginated list of all refunds

`GET	/refunds/refund-token`

Returns the details of the specified refund

`POST	/charges/charge-token/refunds`

Creates a new refund and returns its details

`GET	/charges/charge-token/refunds`

Returns a list of all refunds for the specified charge

---