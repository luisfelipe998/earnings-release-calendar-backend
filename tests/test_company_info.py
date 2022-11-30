import unittest
from earnings_release.suggestions.company_info import CompanyInfo


class TestCompanyInfo(unittest.TestCase):
    def test_should_create_company_info_when_all_fields_are_filled(self):
        input_body = {
            "ticker": "some-ticker",
            "company_name": "some-company-name",
            "exchange": "some-exchange",
            "sector": "some-sector",
            "industry": "some-industry",
            "asset_type": "some_asset"
        }
        company_info = CompanyInfo(input_body['ticker'], input_body['company_name'],
                                   input_body['exchange'], input_body['sector'], input_body['industry'],
                                   input_body['asset_type'])
        self.assertEqual(company_info.ticker, input_body['ticker'])
        self.assertEqual(company_info.company_name, input_body['company_name'])
        self.assertEqual(company_info.exchange, input_body['exchange'])
        self.assertEqual(company_info.sector, input_body['sector'])
        self.assertEqual(company_info.industry, input_body['industry'])

    def test_should_create_company_info_when_mandatory_fields_are_filled(self):
        input_body = {
            "ticker": "some-ticker",
            "company_name": "some-company-name",
            "exchange": None,
            "sector": None,
            "industry": None,
            "asset_type": None
        }
        company_info = CompanyInfo(input_body['ticker'], input_body['company_name'],
                                   input_body['exchange'], input_body['sector'], input_body['industry'],
                                   input_body['asset_type'])
        self.assertEqual(company_info.ticker, input_body['ticker'])
        self.assertEqual(company_info.company_name, input_body['company_name'])
        self.assertEqual(company_info.exchange, input_body['exchange'])
        self.assertEqual(company_info.sector, input_body['sector'])
        self.assertEqual(company_info.industry, input_body['industry'])

    def test_should_not_create_company_info_when_ticker_is_not_informed(self):
        input_body = {
            "ticker": None,
            "company_name": "some-company-name",
            "exchange": "some-exchange",
            "sector": "some-sector",
            "industry": "some-industry",
            "asset_type": "some_asset"
        }
        with self.assertRaises(ValueError) as context:
            CompanyInfo(input_body['ticker'], input_body['company_name'],
                        input_body['exchange'], input_body['sector'], input_body['industry'],
                        input_body['asset_type'])
        self.assertTrue('invalid type for ticker' in str(context.exception))

    def test_should_not_create_company_info_when_company_name_is_not_string(self):
        input_body = {
            "ticker": "some-ticker",
            "company_name": 1,
            "exchange": "some-exchange",
            "sector": "some-sector",
            "industry": "some-industry",
            "asset_type": "some_asset"
        }
        with self.assertRaises(ValueError) as context:
            CompanyInfo(input_body['ticker'], input_body['company_name'],
                        input_body['exchange'], input_body['sector'], input_body['industry'],
                        input_body['asset_type'])
        self.assertTrue('invalid type for company name' in str(context.exception))

    def test_should_not_create_company_info_when_ticker_is_not_string(self):
        input_body = {
            "ticker": 1,
            "company_name": "some-company-name",
            "exchange": "some-exchange",
            "sector": "some-sector",
            "industry": "some-industry",
            "asset_type": "some_asset"
        }
        with self.assertRaises(ValueError) as context:
            CompanyInfo(input_body['ticker'], input_body['company_name'],
                        input_body['exchange'], input_body['sector'], input_body['industry'],
                        input_body['asset_type'])
        self.assertTrue('invalid type for ticker' in str(context.exception))

    def test_should_not_create_company_info_when_company_name_is_not_string(self):
        input_body = {
            "ticker": "some-ticker",
            "company_name": 1,
            "exchange": "some-exchange",
            "sector": "some-sector",
            "industry": "some-industry",
            "asset_type": "some_asset"
        }
        with self.assertRaises(ValueError) as context:
            CompanyInfo(input_body['ticker'], input_body['company_name'],
                        input_body['exchange'], input_body['sector'], input_body['industry'],
                        input_body['asset_type'])
        self.assertTrue('invalid type for company name' in str(context.exception))

    def test_should_not_create_company_info_when_exchange_is_not_string(self):
        input_body = {
            "ticker": "some-ticker",
            "company_name": "some-company-name",
            "exchange": 1,
            "sector": "some-sector",
            "industry": "some-industry",
            "asset_type": "some_asset"
        }
        with self.assertRaises(ValueError) as context:
            CompanyInfo(input_body['ticker'], input_body['company_name'],
                        input_body['exchange'], input_body['sector'], input_body['industry'],
                        input_body['asset_type'])
        self.assertTrue('invalid type for exchange' in str(context.exception))

    def test_should_not_create_company_info_when_sector_is_not_string(self):
        input_body = {
            "ticker": "some-ticker",
            "company_name": "some-company-name",
            "exchange": "some-exchange",
            "sector": 1,
            "industry": "some-industry",
            "asset_type": "some_asset"
        }
        with self.assertRaises(ValueError) as context:
            CompanyInfo(input_body['ticker'], input_body['company_name'],
                        input_body['exchange'], input_body['sector'], input_body['industry'],
                        input_body['asset_type'])
        self.assertTrue('invalid type for sector' in str(context.exception))

    def test_should_not_create_company_info_when_industry_is_not_string(self):
        input_body = {
            "ticker": "some-ticker",
            "company_name": "some-company-name",
            "exchange": "some-exchange",
            "sector": "some-sector",
            "industry": 1,
            "asset_type": "some_asset"
        }
        with self.assertRaises(ValueError) as context:
            CompanyInfo(input_body['ticker'], input_body['company_name'],
                        input_body['exchange'], input_body['sector'], input_body['industry'],
                        input_body['asset_type'])
        self.assertTrue('invalid type for industry' in str(context.exception))

    def test_should_not_create_company_info_when_asset_type_is_not_string(self):
        input_body = {
            "ticker": "some-ticker",
            "company_name": "some-company-name",
            "exchange": "some-exchange",
            "sector": "some-sector",
            "industry": "some-industry",
            "asset_type": 1
        }
        with self.assertRaises(ValueError) as context:
            CompanyInfo(input_body['ticker'], input_body['company_name'],
                        input_body['exchange'], input_body['sector'], input_body['industry'],
                        input_body['asset_type'])
        self.assertTrue('invalid type for asset type' in str(context.exception))
