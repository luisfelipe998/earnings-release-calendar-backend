import unittest
from datetime import datetime
from earnings_release.dates.summary import Summary


class TestSummary(unittest.TestCase):
    def test_should_create_summary_when_all_fields_are_valid(self):
        input_body = ['ticker', 'company_name', '2023-01-23T10:59:00.000Z']
        summary = Summary.from_dict(input_body)
        self.assertEqual(summary.ticker, input_body[0])
        self.assertEqual(summary.company_name, input_body[1])
        self.assertEqual(summary.earnings_release_date, datetime.fromisoformat(input_body[2].replace('Z', '+00:00')))

    def test_should_not_create_summary_when_ticker_is_not_string(self):
        input_body = [1, 'company_name', '2023-01-23T10:59:00.000Z']
        with self.assertRaises(ValueError) as context:
            Summary.from_dict(input_body)
        self.assertTrue('invalid type for ticker' in str(context.exception))

    def test_should_not_create_summary_when_company_name_is_not_string(self):
        input_body = ['ticker', 1, '2023-01-23T10:59:00.000Z']
        with self.assertRaises(ValueError) as context:
            Summary.from_dict(input_body)
        self.assertTrue(
            'invalid type for company name' in str(context.exception))

    def test_should_not_create_summary_when_earnings_release_is_not_string(self):
        input_body = ['ticker', 'company_name', 1]
        with self.assertRaises(ValueError) as context:
            Summary.from_dict(input_body)
        self.assertTrue('invalid type for earnings release date' in str(context.exception))

    def test_should_not_create_summary_when_earnings_release_is_not_valid_date_string(self):
        input_body = ['ticker', 'company_name', 'not-a-date-string']
        with self.assertRaises(ValueError):
            Summary.from_dict(input_body)

    def test_should_not_create_summary_when_input_body_len_is_less_than_3(self):
        input_body = ['ticker', 'company_name']
        with self.assertRaises(IndexError) as context:
            Summary.from_dict(input_body)
        self.assertTrue('input does not have 3 positions' in str(context.exception))
