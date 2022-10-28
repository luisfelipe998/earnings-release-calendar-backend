import json
from sanic import Sanic, response, log
from sanic.request import Request
from earnings_release.dates.get_press_release_dates_by_ticker import GetPressReleaseDatesByTickerHandler
from earnings_release.dates.get_press_release_dates_by_tickers import GetPressReleaseDatesByTickersHandler

from earnings_release.request.yahoo import YahooRequester

app = Sanic("app")

yahoo_requester = YahooRequester()
get_press_release_dates_by_ticker_handler = GetPressReleaseDatesByTickerHandler(yahoo_requester)
get_press_release_dates_by_tickers_handler = GetPressReleaseDatesByTickersHandler(yahoo_requester)


@app.get("/")
async def health_check(_):
    return response.json({"status": "UP"})


@app.get("/press-release-dates/<ticker>")
async def get_press_release_dates_by_ticker(_, ticker):
    try:
        return response.json(await get_press_release_dates_by_ticker_handler.handle(ticker))
    except ValueError as error:
        return response.json({"error": str(error)}, status=404)
    except Exception as error:
        return internal_server_error(error)


@app.post("/press-release-dates")
async def get_press_release_dates_by_tickers(request: Request):
    try:
        input_body = json.loads(request.body)
        if not is_list_of_strings(input_body):
            return bad_request_not_list_input()

        return response.json(await get_press_release_dates_by_tickers_handler.handle(input_body))
    except json.decoder.JSONDecodeError as error:
        return bad_request_not_list_input(error)
    except Exception as error:
        return internal_server_error(error)


def is_list_of_strings(input_body) -> bool:
    return isinstance(input_body, list) and len(input_body) > 0 and isinstance(input_body[0], str)


def bad_request_not_list_input(error="request body is malformed."):
    log.logger.error('error reading body: %s', str(error))
    return response.json({"error": "request body is malformed. Make sure it is a array of strings with at least one item."}, status=400)


def internal_server_error(error):
    log.logger.error("unexpected error: %s", str(error))
    return response.json({"error": "Sorry for the inconvenience. An internal error ocurred getting press release dates."}, status=500)
