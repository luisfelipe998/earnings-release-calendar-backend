import asyncio

from earnings_release.dates.summary import Summary
from earnings_release.requester import Requester


class GetPressReleaseDatesByTickersHandler:

    def __init__(self, requester: Requester):
        self.requester = requester

    async def handle(self, tickers: list[str]) -> list:
        tasks = [ asyncio.create_task(self.__get_earnings_release_summary_by_ticker(ticker.upper())) for ticker in tickers ]
        return await asyncio.gather(*tasks)


    async def __get_earnings_release_summary_by_ticker(self, ticker) -> dict:
        summaries: list[Summary] = await self.requester.get_earnings_release_summary_by_ticker(ticker)
        if len(summaries) == 0:
            return {
                "ticker": ticker,
                "company_name": "unknown (not found)",
                "earnings_release_date": []
            }
        else:
            return {
                "ticker": summaries[0].ticker,
                "company_name": summaries[0].company_name,
                "earnings_release_date": [ summary.earnings_release_date.isoformat().replace("+00:00", "Z") for summary in summaries ][0:10]
            }
