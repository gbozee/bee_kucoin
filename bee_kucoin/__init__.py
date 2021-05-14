import os
from kucoin import client as spot_client
from kucoin_futures import client as future_client

class KucoinExchange:
    def __init__(
        self,
        api_key=None,
        api_secret=None,
        passphrase=None,
        kind="spot",
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase
        if kind == "spot":
            self.API_URL = "https://api.kucoin.com"
            self.client = spot_client
        else:
            self.API_URL = "https://api-futures.kucoin.com"
            self.client = future_client

    @property
    def market_client(self):
        return self.client.Market(url=self.API_URL)

    @property
    def trade_client(self):
        return self.client.Trade(
            key=self.api_key,
            secret=self.api_secret,
            passphrase=self.passphrase,
            url=self.API_URL,
        )

    @property
    def user_client(self):
        return self.client.User(
            key=self.api_key,
            secret=self.api_secret,
            passphrase=self.passphrase,
            url=self.API_URL,
        )


class Client:
    def __init__(
        self,
        spot_api_key=None,
        spot_api_secret=None,
        spot_passphrase=None,
        future_api_key=None,
        future_api_secret=None,
        future_passphrase=None,
    ):
        self.spot_api_key = spot_api_key
        self.spot_api_secret = spot_api_secret
        self.spot_passphrase = spot_passphrase
        self.future_api_key = future_api_key
        self.future_api_secret = future_api_secret
        self.future_passphrase = future_passphrase

    @property
    def spot_api(self):
        return KucoinExchange(
            api_key=self.spot_api_key,
            api_secret=self.spot_api_secret,
            passphrase=self.spot_passphrase,
        )

    @property
    def future_api(self):
        return KucoinExchange(
            api_key=self.future_passphrase,
            api_secret=self.future_api_secret,
            passphrase=self.future_passphrase,
            kind="future",
        )

SPOT_API_KEY = os.getenv("KUCOIN_SPOT_API_KEY")
SPOT_SECRET_KEY = os.getenv("KUCOIN_SPOT_SECRET_KEY")
SPOT_PASSPHRASE = os.getenv("KUCOIN_PASSPHRASE")
FUTURE_API_KEY = os.getenv("KUCOIN_FUTURE_API_KEY")
FUTURE_API_SECRET = os.getenv("KUCOIN_FUTURE_API_SECRET")
FUTURE_PASSPHRASE = os.getenv("KUCOIN_FUTURE_PASSPHRASE")


client = Client(
    spot_api_key=SPOT_API_KEY,
    spot_api_secret=SPOT_SECRET_KEY,
    spot_passphrase=SPOT_PASSPHRASE,
    future_api_key=FUTURE_API_KEY,
    future_api_secret=FUTURE_API_SECRET,
    future_passphrase=FUTURE_PASSPHRASE,
)
