import unittest
from earnings_release.dates.summary import Summary
from datetime import datetime

class TestSummary(unittest.TestCase):
    def test_should_create_summary_when_all_fields_are_valid(self):
        input = [ 'ticker', 'company_name', '2023-01-23T10:59:00.000Z' ]
        summary = Summary.from_dict(input)
        self.assertEqual(summary.ticker, input[0])
        self.assertEqual(summary.company_name, input[1])
        self.assertEqual(summary.earnings_release_date, datetime.fromisoformat(input[2].replace('Z', '+00:00')))


    def test_should_not_create_summary_when_ticker_is_not_string(self):
        input = [ 1, 'company_name', '2023-01-23T10:59:00.000Z' ]
        with self.assertRaises(ValueError) as context:
            Summary.from_dict(input)
        self.assertTrue('invalid type for ticker' in str(context.exception))

    
    def test_should_not_create_summary_when_company_name_is_not_string(self):
        input = [ 'ticker', 1, '2023-01-23T10:59:00.000Z' ]
        with self.assertRaises(ValueError) as context:
            Summary.from_dict(input)
        self.assertTrue('invalid type for company name' in str(context.exception))


    def test_should_not_create_summary_when_earnings_release_is_not_string(self):
        input = [ 'ticker', 'company_name', 1 ]
        with self.assertRaises(ValueError) as context:
            Summary.from_dict(input)
        self.assertTrue('invalid type for earnings release date' in str(context.exception))


    def test_should_not_create_summary_when_earnings_release_is_not_valid_date_string(self):
        input = [ 'ticker', 'company_name', 'not-a-date-string' ]
        with self.assertRaises(ValueError):
            Summary.from_dict(input)


    def test_should_not_create_summary_when_input_len_is_less_than_3(self):
        input = [ 'ticker', 'company_name' ]
        with self.assertRaises(IndexError) as context:
            Summary.from_dict(input)
        self.assertTrue('input does not have 3 positions' in str(context.exception))

