# mexc-python
Python SDK (sync and async) for Mexc with Rest and WS capabilities.

You can check Mexc's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/mexc)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install mexc-exchange-api
```

## Usage

### Async

```Python
from mexc_exchange_api import MexcAsync

async def main():
    instance = MexcAsync({})
    order = await instance.create_order(BTC/USDC, "limit", "buy", 1, 100000)
```

### Sync

```Python
from mexc_exchange_api import MexcSync

def main():
    instance = MexcSync({})
    order =  instance.create_order(BTC/USDC, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from mexc_exchange_api import MexcWs

async def main():
    instance = MexcWs({})
    while True:
        orders = await instance.watch_orders(BTC/USDC)
```

