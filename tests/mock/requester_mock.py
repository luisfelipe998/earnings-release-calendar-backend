from unittest import mock
from earnings_release.dates.summary import Summary
from earnings_release.requester import Requester


mock_data = {
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



class MockRequester(Requester):
    async def get_earnings_release_summary_by_ticker(self, ticker: str) -> list[Summary]:
        if ticker.upper() == "GOOGL":
            return mock_data['GOOGL']
        if ticker.upper() == "MSFT":
            return mock_data['MSFT']
        return mock_data["UNKNOWN"]