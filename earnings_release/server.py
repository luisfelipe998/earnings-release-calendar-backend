import json
from sanic import Sanic, response, request
from earnings_release.dates.get_press_release_dates_by_ticker import GetPressReleaseDatesByTickerHandler
from earnings_release.dates.get_press_release_dates_by_tickers import GetPressReleaseDatesByTickersHandler

from earnings_release.request.yahoo import YahooRequester

app = Sanic("app")

yahoo_requester = YahooRequester()
get_press_release_dates_by_ticker_handler = GetPressReleaseDatesByTickerHandler(yahoo_requester)
get_press_release_dates_by_tickers_handler = GetPressReleaseDatesByTickersHandler(yahoo_requester)

@app.get("/press-release-dates/<ticker>")
async def get_press_release_dates_by_ticker(request, ticker):
    try:
        return response.json(await get_press_release_dates_by_ticker_handler.handle(ticker))
    except ValueError as error:
        return response.json({"error": str(error)}, status=404)
    except Exception:
        return internal_server_error()

@app.post("/press-release-dates")
async def get_press_release_dates_by_tickers(request: request.Request):
    try:
        input = json.loads(request.body)
        if not is_list_of_strings(input):
            return bad_request_not_list_input()

        return response.json(await get_press_release_dates_by_tickers_handler.handle(input))
    except json.decoder.JSONDecodeError:
        return bad_request_not_list_input()
    except Exception:
        return internal_server_error()


def is_list_of_strings(input) -> bool:
    return type(input) is list and len(input) > 0 and type(input[0]) is str


def bad_request_not_list_input():
    return response.json({"error": "request body is malformed. Make sure it is a array of strings with at least one item."}, status=400)


def internal_server_error():
    return response.json({ "error": "Sorry for the inconvenience. An internal error ocurred getting press release dates." }, status=500)