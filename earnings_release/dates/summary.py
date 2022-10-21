from datetime import datetime, timedelta, timezone
from dataclasses import dataclass

@dataclass
class Summary:
    __ticker: str
    __company_name: str
    __earnings_release_date: datetime

    def __init__(self, ticker, company_name, earnings_release_date):
        self.ticker = ticker
        self.company_name = company_name
        self.earnings_release_date = earnings_release_date


    @property
    def ticker(self) -> str:
        return self.__ticker


    @ticker.setter
    def ticker(self, value: str) -> None:
        if (type(value) != str):
            raise ValueError('invalid type for ticker')
        self.__ticker = value


    @property
    def company_name(self) -> str:
        return self.__company_name


    @company_name.setter
    def company_name(self, value: str) -> None:
        if (type(value) != str):
            raise ValueError('invalid type for company name')
        self.__company_name = value


    @property
    def earnings_release_date(self) -> datetime:
        return self.__earnings_release_date


    @earnings_release_date.setter
    def earnings_release_date(self, value: str) -> None:
        if (type(value) != str):
            raise ValueError('invalid type for earnings release date')
        self.__earnings_release_date = datetime.fromisoformat(value.replace('Z', '+00:00'))


    @staticmethod
    def from_dict(obj: list) -> 'Summary':
        if len(obj) == 2:
            raise IndexError("input does not have 3 positions")

        return Summary(obj[0], obj[1], obj[2])