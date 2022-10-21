from earnings_release.dates.summary import Summary
from earnings_release.requester import Requester


class GetPressReleaseDatesByTickerHandler:

    def __init__(self, requester: Requester):
        self.requester = requester

    async def handle(self, ticker: str) -> dict:
        summaries: list[Summary] = await self.requester.get_earnings_release_summary_by_ticker(ticker.upper())
        if len(summaries) == 0:
            raise ValueError(
                "could not found any press release dates for ticker " + ticker)

        return {
            "ticker": summaries[0].ticker,
            "company_name": summaries[0].company_name,
            "earnings_release_date": [summary.earnings_release_date.isoformat().replace("+00:00", "Z") for summary in summaries]
        }
