import unittest

from pin_payments.currencies import Currency, CurrencyCode, Currencies


class TestCurrencyCodeEnum(unittest.TestCase):
    def test_currency_code_enum_has_correct_values(self):
        self.assertEqual(CurrencyCode.AUD.value, 'AUD')
        self.assertEqual(CurrencyCode.USD.value, 'USD')
        self.assertEqual(CurrencyCode.NZD.value, 'NZD')
        self.assertEqual(CurrencyCode.SGD.value, 'SGD')
        self.assertEqual(CurrencyCode.EUR.value, 'EUR')
        self.assertEqual(CurrencyCode.GBP.value, 'GBP')
        self.assertEqual(CurrencyCode.CAD.value, 'CAD')
        self.assertEqual(CurrencyCode.HKD.value, 'HKD')
        self.assertEqual(CurrencyCode.JPY.value, 'JPY')
        self.assertEqual(CurrencyCode.MYR.value, 'MYR')
        self.assertEqual(CurrencyCode.THB.value, 'THB')
        self.assertEqual(CurrencyCode.PHP.value, 'PHP')
        self.assertEqual(CurrencyCode.ZAR.value, 'ZAR')
        self.assertEqual(CurrencyCode.IDR.value, 'IDR')
        self.assertEqual(CurrencyCode.TWD.value, 'TWD')


class TestCurrency(unittest.TestCase):
    def test_currency_initialization_and_attributes(self):
        # Test initialization and attributes for each Currency instance
        aud = Currency(CurrencyCode.AUD, 'cent', 100)
        self.assertEqual(aud.code, CurrencyCode.AUD)
        self.assertEqual(aud.base_unit, 'cent')
        self.assertEqual(aud.min_amount, 100)

        usd = Currency(CurrencyCode.USD, 'cent', 100)
        self.assertEqual(usd.code, CurrencyCode.USD)
        self.assertEqual(usd.base_unit, 'cent')
        self.assertEqual(usd.min_amount, 100)

        nzd = Currency(CurrencyCode.NZD, 'cent', 100)
        self.assertEqual(nzd.code, CurrencyCode.NZD)
        self.assertEqual(nzd.base_unit, 'cent')
        self.assertEqual(nzd.min_amount, 100)

        sgd = Currency(CurrencyCode.SGD, 'cent', 100)
        self.assertEqual(sgd.code, CurrencyCode.SGD)
        self.assertEqual(sgd.base_unit, 'cent')
        self.assertEqual(sgd.min_amount, 100)

        eur = Currency(CurrencyCode.EUR, 'cent', 100)
        self.assertEqual(eur.code, CurrencyCode.EUR)
        self.assertEqual(eur.base_unit, 'cent')
        self.assertEqual(eur.min_amount, 100)

        gbp = Currency(CurrencyCode.GBP, 'penny', 50)
        self.assertEqual(gbp.code, CurrencyCode.GBP)
        self.assertEqual(gbp.base_unit, 'penny')
        self.assertEqual(gbp.min_amount, 50)

        cad = Currency(CurrencyCode.CAD, 'cent', 100)
        self.assertEqual(cad.code, CurrencyCode.CAD)
        self.assertEqual(cad.base_unit, 'cent')
        self.assertEqual(cad.min_amount, 100)

        hkd = Currency(CurrencyCode.HKD, 'cent', 1000)
        self.assertEqual(hkd.code, CurrencyCode.HKD)
        self.assertEqual(hkd.base_unit, 'cent')
        self.assertEqual(hkd.min_amount, 1000)

        jpy = Currency(CurrencyCode.JPY, 'yen', 100)
        self.assertEqual(jpy.code, CurrencyCode.JPY)
        self.assertEqual(jpy.base_unit, 'yen')
        self.assertEqual(jpy.min_amount, 100)

        myr = Currency(CurrencyCode.MYR, 'sen', 300)
        self.assertEqual(myr.code, CurrencyCode.MYR)
        self.assertEqual(myr.base_unit, 'sen')
        self.assertEqual(myr.min_amount, 300)

        thb = Currency(CurrencyCode.THB, 'satang', 2000)
        self.assertEqual(thb.code, CurrencyCode.THB)
        self.assertEqual(thb.base_unit, 'satang')
        self.assertEqual(thb.min_amount, 2000)

        php = Currency(CurrencyCode.PHP, 'centavo', 3000)
        self.assertEqual(php.code, CurrencyCode.PHP)
        self.assertEqual(php.base_unit, 'centavo')
        self.assertEqual(php.min_amount, 3000)

        zar = Currency(CurrencyCode.ZAR, 'cent', 1000)
        self.assertEqual(zar.code, CurrencyCode.ZAR)
        self.assertEqual(zar.base_unit, 'cent')
        self.assertEqual(zar.min_amount, 1000)

        idr = Currency(CurrencyCode.IDR, 'sen', 1000000)
        self.assertEqual(idr.code, CurrencyCode.IDR)
        self.assertEqual(idr.base_unit, 'sen')
        self.assertEqual(idr.min_amount, 1000000)

        twd = Currency(CurrencyCode.TWD, 'cent', 2500)
        self.assertEqual(twd.code, CurrencyCode.TWD)
        self.assertEqual(twd.base_unit, 'cent')
        self.assertEqual(twd.min_amount, 2500)


class TestCurrencies(unittest.TestCase):
    def test_currencies_class_attributes(self):
        # AUD
        self.assertIsInstance(Currencies.AUD, Currency)
        self.assertEqual(Currencies.AUD.code, CurrencyCode.AUD)
        self.assertEqual(Currencies.AUD.base_unit, 'cent')
        self.assertEqual(Currencies.AUD.min_amount, 100)

        # USD
        self.assertIsInstance(Currencies.USD, Currency)
        self.assertEqual(Currencies.USD.code, CurrencyCode.USD)
        self.assertEqual(Currencies.USD.base_unit, 'cent')
        self.assertEqual(Currencies.USD.min_amount, 100)

        # NZD
        self.assertIsInstance(Currencies.NZD, Currency)
        self.assertEqual(Currencies.NZD.code, CurrencyCode.NZD)
        self.assertEqual(Currencies.NZD.base_unit, 'cent')
        self.assertEqual(Currencies.NZD.min_amount, 100)

        # SGD
        self.assertIsInstance(Currencies.SGD, Currency)
        self.assertEqual(Currencies.SGD.code, CurrencyCode.SGD)
        self.assertEqual(Currencies.SGD.base_unit, 'cent')
        self.assertEqual(Currencies.SGD.min_amount, 100)

        # EUR
        self.assertIsInstance(Currencies.EUR, Currency)
        self.assertEqual(Currencies.EUR.code, CurrencyCode.EUR)
        self.assertEqual(Currencies.EUR.base_unit, 'cent')
        self.assertEqual(Currencies.EUR.min_amount, 100)

        # GBP
        self.assertIsInstance(Currencies.GBP, Currency)
        self.assertEqual(Currencies.GBP.code, CurrencyCode.GBP)
        self.assertEqual(Currencies.GBP.base_unit, 'penny')
        self.assertEqual(Currencies.GBP.min_amount, 50)

        # CAD
        self.assertIsInstance(Currencies.CAD, Currency)
        self.assertEqual(Currencies.CAD.code, CurrencyCode.CAD)
        self.assertEqual(Currencies.CAD.base_unit, 'cent')
        self.assertEqual(Currencies.CAD.min_amount, 100)

        # HKD
        self.assertIsInstance(Currencies.HKD, Currency)
        self.assertEqual(Currencies.HKD.code, CurrencyCode.HKD)
        self.assertEqual(Currencies.HKD.base_unit, 'cent')
        self.assertEqual(Currencies.HKD.min_amount, 1000)

        # JPY
        self.assertIsInstance(Currencies.JPY, Currency)
        self.assertEqual(Currencies.JPY.code, CurrencyCode.JPY)
        self.assertEqual(Currencies.JPY.base_unit, 'yen')
        self.assertEqual(Currencies.JPY.min_amount, 100)

        # MYR
        self.assertIsInstance(Currencies.MYR, Currency)
        self.assertEqual(Currencies.MYR.code, CurrencyCode.MYR)
        self.assertEqual(Currencies.MYR.base_unit, 'sen')
        self.assertEqual(Currencies.MYR.min_amount, 300)

        # THB
        self.assertIsInstance(Currencies.THB, Currency)
        self.assertEqual(Currencies.THB.code, CurrencyCode.THB)
        self.assertEqual(Currencies.THB.base_unit, 'satang')
        self.assertEqual(Currencies.THB.min_amount, 2000)

        # PHP
        self.assertIsInstance(Currencies.PHP, Currency)
        self.assertEqual(Currencies.PHP.code, CurrencyCode.PHP)
        self.assertEqual(Currencies.PHP.base_unit, 'centavo')
        self.assertEqual(Currencies.PHP.min_amount, 3000)

        # ZAR
        self.assertIsInstance(Currencies.ZAR, Currency)
        self.assertEqual(Currencies.ZAR.code, CurrencyCode.ZAR)
        self.assertEqual(Currencies.ZAR.base_unit, 'cent')
        self.assertEqual(Currencies.ZAR.min_amount, 1000)

        # IDR
        self.assertIsInstance(Currencies.IDR, Currency)
        self.assertEqual(Currencies.IDR.code, CurrencyCode.IDR)
        self.assertEqual(Currencies.IDR.base_unit, 'sen')
        self.assertEqual(Currencies.IDR.min_amount, 1000000)

        # TWD
        self.assertIsInstance(Currencies.TWD, Currency)
        self.assertEqual(Currencies.TWD.code, CurrencyCode.TWD)
        self.assertEqual(Currencies.TWD.base_unit, 'cent')
        self.assertEqual(Currencies.TWD.min_amount, 2500)
