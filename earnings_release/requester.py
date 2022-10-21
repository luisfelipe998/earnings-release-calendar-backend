
from earnings_release.dates.summary import Summary


class Requester:
    async def get_earnings_release_summary_by_ticker(self, ticker: str) -> list[Summary]:
        """Abstract class"""