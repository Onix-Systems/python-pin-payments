from enum import Enum
from typing import Dict, Union


class CardType(Enum):
    STANDARD = "standard"
    DECLINED = "declined"
    INSUFFICIENT_FUNDS = "insufficient_funds"
    INVALID_CVV = "invalid_cvv"
    INVALID_CARD = "invalid_card"
    PROCESSING_ERROR = "processing_error"
    SUSPECTED_FRAUD = "suspected_fraud"
    GATEWAY_ERROR = "gateway_error"
    UNKNOWN = "unknown"


class TestCard:
    def __init__(self, card_number: str, card_type: CardType):
        self.card_number = card_number
        self.card_type = card_type


class TestCards:
    cards = [
        TestCard("4200000000000000", CardType.STANDARD),
        TestCard("4100000000000001", CardType.DECLINED),
        TestCard("4000000000000002", CardType.INSUFFICIENT_FUNDS),
        TestCard("4900000000000003", CardType.INVALID_CVV),
        TestCard("4800000000000004", CardType.INVALID_CARD),
        TestCard("4700000000000005", CardType.PROCESSING_ERROR),
        TestCard("4600000000000006", CardType.SUSPECTED_FRAUD),
        TestCard("4300000000000009", CardType.GATEWAY_ERROR),
        TestCard("4400000000000099", CardType.UNKNOWN)
    ]

    @staticmethod
    def get_card_response(card_number: str, amount: int) -> Dict[str, Union[str, None, int]]:
        card = next((card for card in TestCards.cards if card.card_number == card_number), None)
        if card is None:
            return {
                "error": "unknown_card",
                "error_description": "The card number is not recognized"
            }

        if card.card_type == CardType.STANDARD:
            return {"success": True, "token": "ch_lfUYEBK14zotCTykezJkfg", "amount": amount}
        else:
            return {
                "error": card.card_type.value,
                "error_description": TestCards.get_error_description(card.card_type),
                "charge_token": "ch_lfUYEBK14zotCTykezJkfg"
            }

    @staticmethod
    def get_error_description(card_type: CardType) -> str:
        descriptions = {
            CardType.DECLINED: "The card was declined",
            CardType.INSUFFICIENT_FUNDS: "There are not enough funds available to process the requested amount",
            CardType.INVALID_CVV: "The card verification code (cvc) was not in the correct format",
            CardType.INVALID_CARD: "The card was invalid",
            CardType.PROCESSING_ERROR: "An error occurred while processing the card",
            CardType.SUSPECTED_FRAUD: "The transaction was flagged as possibly fraudulent and subsequently declined",
            CardType.GATEWAY_ERROR: "An upstream error occurred while processing the transaction. Please try again.",
            CardType.UNKNOWN: "Sorry, an unknown error has occurred. This is being investigated"
        }
        return descriptions.get(card_type, "An unknown error occurred")


class ChargeService:
    @staticmethod
    def create_charge(card_number: str, amount: int) -> Dict[str, Union[str, None, int]]:
        return TestCards.get_card_response(card_number, amount)


if __name__ == "__main__":
    card_number_ = "4200000000000000"
    amount_ = 100
    response = ChargeService.create_charge(card_number_, amount_)
    print(response)
