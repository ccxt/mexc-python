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

### Sync

```Python
from mexc_exchange_api import MexcSync

def main():
    instance = MexcSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)
```

### Async

```Python
import asyncio
from mexc_exchange_api import MexcAsync

async def main():
    instance = MexcAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

asyncio.run(main())
```

### Websockets

```Python
from mexc_exchange_api import MexcWs

async def main():
    instance = MexcWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")
```

