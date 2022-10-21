from unittest import IsolatedAsyncioTestCase
from earnings_release.dates.get_press_release_dates_by_tickers import GetPressReleaseDatesByTickersHandler
from tests.mock.requester_mock import MockRequester


class TestGetPressReleaseDatesByTicker(IsolatedAsyncioTestCase):
    async def test_should_get_by_tickers_successfully(self):
        input_body = ["GOOGL", "msft", "invalid"]
        mock_requester = MockRequester()
        handler = GetPressReleaseDatesByTickersHandler(mock_requester)

        response = await handler.handle(input_body)

        self.assertEqual(len(response), 3)
        self.assertEqual(response[0]["ticker"], "GOOGL")
        self.assertEqual(response[0]["company_name"], "Alphabet Inc")
        self.assertEqual(len(response[0]["earnings_release_date"]), 10)
        self.assertEqual(response[0]["earnings_release_date"][0], "2023-07-24T20:00:00Z")
        self.assertEqual(response[1]["ticker"], "MSFT")
        self.assertEqual(response[1]["company_name"], "Microsoft Corp")
        self.assertEqual(len(response[1]["earnings_release_date"]), 7)
        self.assertEqual(response[1]["earnings_release_date"][0], "2023-07-24T10:59:00Z")
        self.assertEqual(response[2]["ticker"], "INVALID")
        self.assertEqual(response[2]["company_name"], "unknown (not found)")
        self.assertEqual(len(response[2]["earnings_release_date"]), 0)
