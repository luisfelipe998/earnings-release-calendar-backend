from unittest import IsolatedAsyncioTestCase

from earnings_release.dates.get_press_release_dates_by_ticker import GetPressReleaseDatesByTickerHandler
from tests.mock.requester_mock import MockRequester


class TestGetPressReleaseDatesByTicker(IsolatedAsyncioTestCase):
    async def test_should_get_googl_uppercase_by_ticker_successfully(self):
        input_param = "GOOGL"
        mock_requester = MockRequester()
        handler = GetPressReleaseDatesByTickerHandler(mock_requester)

        response = await handler.handle(input_param)

        self.assertEqual(response["ticker"], "GOOGL")
        self.assertEqual(response["company_name"], "Alphabet Inc")
        self.assertEqual(len(response["earnings_release_date"]), 11)
        self.assertEqual(response["earnings_release_date"][0], "2023-07-24T20:00:00Z")

    async def test_should_get_googl_by_ticker_successfully(self):
        input_param = "GOOGL"
        mock_requester = MockRequester()
        handler = GetPressReleaseDatesByTickerHandler(mock_requester)

        response = await handler.handle(input_param)

        self.assertEqual(response["ticker"], "GOOGL")
        self.assertEqual(response["company_name"], "Alphabet Inc")
        self.assertEqual(len(response["earnings_release_date"]), 11)
        self.assertEqual(response["earnings_release_date"][0], "2023-07-24T20:00:00Z")

    async def test_should_get_invalid_by_ticker_and_raise_value_error(self):
        input_param = "unknown"
        mock_requester = MockRequester()
        handler = GetPressReleaseDatesByTickerHandler(mock_requester)

        with self.assertRaises(ValueError) as context:
            await handler.handle(input_param)
        self.assertTrue("could not found any press release dates for ticker " + input_param in str(context.exception))
