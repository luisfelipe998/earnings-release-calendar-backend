
from earnings_release.dates.summary import Summary
from earnings_release.suggestions.company_info import CompanyInfo


class Requester:
    async def get_earnings_release_summary_by_ticker(self, ticker: str) -> list[Summary]:
        """Abstract class"""

    async def get_companies_suggestions(self, query: str) -> list[CompanyInfo]:
        """Abstract class"""
