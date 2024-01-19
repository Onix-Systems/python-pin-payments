from enum import Enum


class CurrencyCode(Enum):
    """List of available currency codes."""
    AUD = "AUD"
    USD = "USD"
    NZD = "NZD"
    SGD = "SGD"
    EUR = "EUR"
    GBP = "GBP"
    CAD = "CAD"
    HKD = "HKD"
    JPY = "JPY"
    MYR = "MYR"
    THB = "THB"
    PHP = "PHP"
    ZAR = "ZAR"
    IDR = "IDR"
    TWD = "TWD"


class Currency:
    """A class to represent a currency with all its properties.

    Attributes:
        code (CurrencyCode): Currency code.
        base_unit (str): Base unit of currency.
        min_amount (int): Minimum amount for a transaction in this currency.
    """

    def __init__(self, code: CurrencyCode, base_unit: str, min_amount: int) -> None:
        self.code = code
        self.base_unit = base_unit
        self.min_amount = min_amount


class Currencies:
    """A class that unites all currencies."""

    AUD = Currency(CurrencyCode.AUD, 'cent', 100)
    USD = Currency(CurrencyCode.USD, 'cent', 100)
    NZD = Currency(CurrencyCode.NZD, 'cent', 100)
    SGD = Currency(CurrencyCode.SGD, 'cent', 100)
    EUR = Currency(CurrencyCode.EUR, 'cent', 100)
    GBP = Currency(CurrencyCode.GBP, 'penny', 50)
    CAD = Currency(CurrencyCode.CAD, 'cent', 100)
    HKD = Currency(CurrencyCode.HKD, 'cent', 1000)
    JPY = Currency(CurrencyCode.JPY, 'yen', 100)
    MYR = Currency(CurrencyCode.MYR, 'sen', 300)
    THB = Currency(CurrencyCode.THB, 'satang', 2000)
    PHP = Currency(CurrencyCode.PHP, 'centavo', 3000)
    ZAR = Currency(CurrencyCode.ZAR, 'cent', 1000)
    IDR = Currency(CurrencyCode.IDR, 'sen', 1000000)
    TWD = Currency(CurrencyCode.TWD, 'cent', 2500)


if __name__ == '__main__':
    print(
        f"Code: {Currencies.AUD.code.value}, "
        f"Base Unit: {Currencies.AUD.base_unit}, "
        f"Min Amount: {Currencies.AUD.min_amount}"
    )
