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

### Customers API

...

### Refunds API

...
