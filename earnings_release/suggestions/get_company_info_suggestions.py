from earnings_release.requester import Requester
from earnings_release.suggestions.company_info import CompanyInfo


class GetCompanyInfoSuggestionsHandler:

    def __init__(self, requester: Requester):
        self.requester = requester

    async def handle(self, query: str) -> dict:
        suggestions: list[CompanyInfo] = await self.requester.get_companies_suggestions(query)
        fitered_suggestions = []
        for suggestion in suggestions:
            if suggestion.type is None or suggestion.type.lower() != 'equity':
                continue
            if suggestion.exchange is None or (suggestion.exchange.lower() != 'nyse' and suggestion.exchange.lower() != 'nasdaq'):
                continue
            fitered_suggestions.append(suggestion)

        return [{
            "ticker": suggestion.ticker,
            "company_name": suggestion.company_name,
            "exchange": suggestion.company_name,
            "sector": suggestion.sector,
            "industry": suggestion.industry
        } for suggestion in fitered_suggestions]
