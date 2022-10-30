from earnings_release.dates.summary import Summary
from earnings_release.requester import Requester
from earnings_release.suggestions.company_info import CompanyInfo


mock_summary_data = {
    "GOOGL": [
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2023-07-24T20:00:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2023-04-24T20:00:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2023-01-30T21:00:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2022-10-25T21:00:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2022-10-25T10:59:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2022-07-26T16:02:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2022-04-26T16:09:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2022-02-01T16:02:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2021-10-26T16:00:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2021-07-27T16:20:00Z"]),
        Summary.from_dict(["GOOGL", "Alphabet Inc", "2021-04-26T16:00:00Z"]),
    ],
    "MSFT": [
        Summary.from_dict(["MSFT", "Microsoft Corp", "2023-07-24T10:59:00Z"]),
        Summary.from_dict(["MSFT", "Microsoft Corp", "2023-04-24T10:59:00Z"]),
        Summary.from_dict(["MSFT", "Microsoft Corp", "2023-01-23T10:59:00Z"]),
        Summary.from_dict(["MSFT", "Microsoft Corp", "2022-10-25T21:30:00Z"]),
        Summary.from_dict(["MSFT", "Microsoft Corp", "2022-10-25T20:00:00Z"]),
        Summary.from_dict(["MSFT", "Microsoft Corp", "2022-07-26T16:09:00Z"]),
        Summary.from_dict(["MSFT", "Microsoft Corp", "2022-04-26T16:04:00Z"]),
    ],
    "UNKNOWN": []
}

mock_company_info_data = [
    CompanyInfo(ticker="nyse-ticker", company_name="nyse-company",
                exchange="nyse", sector="sector", industry="industry", asset_type="equity"),
    CompanyInfo(ticker="nasdaq-ticker", company_name="nasdaq-company",
                exchange="nasdaq", sector="sector", industry="industry", asset_type="equity"),
    CompanyInfo(ticker="wrong-exchange-ticker", company_name="wrong-exchange-company",
                exchange="wrong-exchange", sector="sector", industry="industry", asset_type="equity"),
    CompanyInfo(ticker="wrong-asset-type-ticker", company_name="wrong-asset-type-company",
                exchange="nsyse", sector="sector", industry="industry", asset_type="not-equity"),
    CompanyInfo(ticker="only-mandatory-ticker", company_name="only-mandatory-company",
                exchange=None, sector=None, industry=None, asset_type=None),
]


class MockRequester(Requester):
    async def get_earnings_release_summary_by_ticker(self, ticker: str) -> list[Summary]:
        if ticker.upper() == "GOOGL":
            return mock_summary_data['GOOGL']
        if ticker.upper() == "MSFT":
            return mock_summary_data['MSFT']
        return mock_summary_data["UNKNOWN"]

    async def get_companies_suggestions(self, _: str) -> list[CompanyInfo]:
        return mock_company_info_data
