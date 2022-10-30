import json
import requests_async as requests

from earnings_release.dates.summary import Summary
from earnings_release.requester import Requester
from earnings_release.suggestions.company_info import CompanyInfo


class YahooRequester(Requester):

    async def get_earnings_release_summary_by_ticker(self, ticker: str) -> list[Summary]:
        url = "https://query2.finance.yahoo.com/v1/finance/visualization?crumb=obNzQdITwnr&lang=en-US&region=US"

        payload = json.dumps({
            "sortType": "DESC",
            "entityIdType": "earnings",
            "sortField": "startdatetime",
            "includeFields": [
                "ticker",
                "companyshortname",
                "startdatetime"
            ],
            "query": {
                "operator": "or",
                "operands": [
                    {
                        "operator": "eq",
                        "operands": [
                            "ticker",
                            ticker
                        ]
                    }
                ]
            },
            "offset": 0,
            "size": 250
        })
        headers = {
            'cookie': 'A1=d=AQABBF-0PGMCEEasJHIJJgsf_qMXS6QWQ2gFEgEBAQEFPmNGYwAAAAAA_eMAAA&S=AQAAAq5vEICHrx1CxvcnKMAnfRs; A3=d=AQABBF-0PGMCEEasJHIJJgsf_qMXS6QWQ2gFEgEBAQEFPmNGYwAAAAAA_eMAAA&S=AQAAAq5vEICHrx1CxvcnKMAnfRs; A1S=d=AQABBF-0PGMCEEasJHIJJgsf_qMXS6QWQ2gFEgEBAQEFPmNGYwAAAAAA_eMAAA&S=AQAAAq5vEICHrx1CxvcnKMAnfRs&j=WORLD; cmp=t=1664922723&j=0&u=1---',
            'Content-Type': 'application/json',
            'User-Agent': ''
        }

        response = await requests.post(url, headers=headers, data=payload)

        if response.status_code != 200:
            raise Exception('could not fetch data from yahoo finance API')

        summaries = [Summary.from_dict(row) for row in response.json()["finance"]["result"][0]["documents"][0]["rows"]]
        return summaries

    async def get_companies_suggestions(self, query: str) -> list[CompanyInfo]:
        url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query}&lang=en-US&region=US&newsCount=0&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&enableCb=false&enableNavLinks=true&enableEnhancedTrivialQuery=true&enableCulturalAssets=true&researchReportsCount=2&corsDomain=finance.yahoo.com&listsCount=0"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': ''
        }
        response = await requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            raise Exception('could not fetch data from yahoo finance API')

        company_info_suggestions = [CompanyInfo(row.get('symbol'),
                                                row.get('shortname'),
                                                row.get('exchDisp'),
                                                row.get('sector'),
                                                row.get('industry'),
                                                row.get('typeDisp'))
                                    for row in response.json()['quotes']]
        return company_info_suggestions
