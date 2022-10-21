import json
import requests_async as requests

from earnings_release.dates.summary import Summary
from earnings_release.requester import Requester


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

        summaries = []
        if response.status_code != 200:
            return summaries
        
        for row in response.json()["finance"]["result"][0]["documents"][0]["rows"]:
            summaries.append(Summary.from_dict(row))

        return summaries
