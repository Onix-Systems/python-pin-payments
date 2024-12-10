Usage
=====

Here are some examples of how to use the Python-Pin-Payments library.

Creating a Charge
-----------------

.. code-block:: python

   from pin_payments import charges

   charge = charges.create(
       amount=1000,
       currency='usd',
       description='Charge for test@example.com',
       email='test@example.com',
       card_token='card_token_123'
   )

   print(charge)

Managing Customers
------------------

.. code-block:: python

   from pin_payments import customers

   customer = customers.create(
       email='customer@example.com',
       card_token='card_token_123'
   )

   print(customer)
