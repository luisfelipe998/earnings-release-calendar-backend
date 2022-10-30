from unittest import IsolatedAsyncioTestCase

from earnings_release.suggestions.get_company_info_suggestions import GetCompanyInfoSuggestionsHandler
from tests.mock.requester_mock import MockRequester


class TestGetCompanyInfoSuggestions(IsolatedAsyncioTestCase):
    async def test_should_get_suggestions_successfully(self):
        input_param = "ticker"
        mock_requester = MockRequester()
        handler = GetCompanyInfoSuggestionsHandler(mock_requester)

        response = await handler.handle(input_param)

        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]['ticker'], "nyse-ticker")
        self.assertEqual(response[1]['ticker'], "nasdaq-ticker")
