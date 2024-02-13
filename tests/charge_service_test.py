import unittest

from pin_payments.charge_service import ChargeService


class TestChargeService(unittest.TestCase):
    def test_standard_card(self):
        response = ChargeService.create_charge("4200000000000000", 100)
        self.assertTrue(response["success"])
        self.assertEqual(response["amount"], 100)

    def test_declined_card(self):
        response = ChargeService.create_charge("4100000000000001", 100)
        self.assertEqual(response["error"], "declined")
        self.assertEqual(response["error_description"], "The card was declined")

    def test_insufficient_funds(self):
        response = ChargeService.create_charge("4000000000000002", 100)
        self.assertEqual(response["error"], "insufficient_funds")
        self.assertEqual(response["error_description"],
                         "There are not enough funds available to process the requested amount")

    def test_invalid_cvv(self):
        response = ChargeService.create_charge("4900000000000003", 100)
        self.assertEqual(response["error"], "invalid_cvv")
        self.assertEqual(response["error_description"],
                         "The card verification code (cvc) was not in the correct format")

    def test_invalid_card(self):
        response = ChargeService.create_charge("4800000000000004", 100)
        self.assertEqual(response["error"], "invalid_card")
        self.assertEqual(response["error_description"], "The card was invalid")

    def test_processing_error(self):
        response = ChargeService.create_charge("4700000000000005", 100)
        self.assertEqual(response["error"], "processing_error")
        self.assertEqual(response["error_description"], "An error occurred while processing the card")

    def test_suspected_fraud(self):
        response = ChargeService.create_charge("4600000000000006", 100)
        self.assertEqual(response["error"], "suspected_fraud")
        self.assertEqual(response["error_description"],
                         "The transaction was flagged as possibly fraudulent and subsequently declined")

    def test_gateway_error(self):
        response = ChargeService.create_charge("4300000000000009", 100)
        self.assertEqual(response["error"], "gateway_error")
        self.assertEqual(response["error_description"],
                         "An upstream error occurred while processing the transaction. Please try again.")

    def test_unknown_card(self):
        response = ChargeService.create_charge("9999999999999999", 100)
        self.assertEqual(response["error"], "unknown_card")
        self.assertEqual(response["error_description"], "The card number is not recognized")
