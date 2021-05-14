import os
from bee_kucoin import Client


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
