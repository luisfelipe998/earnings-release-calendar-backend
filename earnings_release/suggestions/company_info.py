from dataclasses import dataclass


@dataclass
class CompanyInfo:
    __ticker: str
    __company_name: str
    __exchange: str
    __sector: str
    __industry: str
    __type: str

    def __init__(self, ticker, company_name, exchange, sector, industry, asset_type):
        self.ticker = ticker
        self.company_name = company_name
        self.exchange = exchange
        self.sector = sector
        self.industry = industry
        self.type = asset_type

    @property
    def ticker(self) -> str:
        return self.__ticker

    @ticker.setter
    def ticker(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('invalid type for ticker')
        self.__ticker = value

    @property
    def company_name(self) -> str:
        return self.__company_name

    @company_name.setter
    def company_name(self, value: str) -> None:
        if not isinstance(value, str) and value is not None:
            raise ValueError('invalid type for company name')
        self.__company_name = value

    @property
    def exchange(self) -> str:
        return self.__exchange

    @exchange.setter
    def exchange(self, value: str) -> None:
        if not isinstance(value, str) and value is not None:
            raise ValueError('invalid type for exchange')
        self.__exchange = value

    @property
    def sector(self) -> str:
        return self.__sector

    @sector.setter
    def sector(self, value: str) -> None:
        if not isinstance(value, str) and value is not None:
            raise ValueError('invalid type for sector')
        self.__sector = value

    @property
    def industry(self) -> str:
        return self.__industry

    @industry.setter
    def industry(self, value: str) -> None:
        if not isinstance(value, str) and value is not None:
            raise ValueError('invalid type for industry')
        self.__industry = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str) -> None:
        if not isinstance(value, str) and value is not None:
            raise ValueError('invalid type for asset type')
        self.__type = value
