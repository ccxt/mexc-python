# mexc-python
Python SDK (sync and async) for Mexc cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/mexc)
- You can check Mexc's docs here: [Docs](https://www.google.com/search?q=google+mexc+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/mexc-python
- Pypi package: https://pypi.org/project/mexc-exchange-api


## Installation

```
pip install mexc-exchange-api
```

## Usage

### Sync

```Python
from mexc import MexcSync

def main():
    instance = MexcSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from mexc import MexcAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = MexcAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from mexc import MexcWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = MexcWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_deposit_address(self, code: str, params={})`
- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_market_sell_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `create_spot_order_request(self, market, type, side, amount, price=None, marginMode=None, params={})`
- `create_spot_order(self, market, type, side, amount, price=None, marginMode=None, params={})`
- `create_swap_order(self, market, type, side, amount, price=None, marginMode=None, params={})`
- `fetch_account_helper(self, type, params)`
- `fetch_accounts(self, params={})`
- `fetch_balance(self, params={})`
- `fetch_bids_asks(self, symbols: Strings = None, params={})`
- `fetch_canceled_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_addresses_by_network(self, code: str, params={})`
- `fetch_deposit_withdraw_fees(self, codes: Strings = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_interval(self, symbol: str, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_leverage_tiers(self, symbols: Strings = None, params={})`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order_trades(self, id: str, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders_by_ids(self, ids, symbol: Str = None, params={})`
- `fetch_orders_by_state(self, state, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position_mode(self, symbol: Str = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions_history(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_spot_markets(self, params={})`
- `fetch_status(self, params={})`
- `fetch_swap_markets(self, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_transaction_fees(self, codes: Strings = None, params={})`
- `fetch_transfer(self, id: str, code: Str = None, params={})`
- `fetch_transfers(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `add_margin(self, symbol: str, amount: float, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids, symbol: Str = None, params={})`
- `custom_parse_balance(self, response, marketType)`
- `describe(self)`
- `get_tif_from_raw_order_type(self, orderType: Str = None)`
- `modify_margin_helper(self, symbol: str, amount, addOrReduce, params={})`
- `nonce(self)`
- `reduce_margin(self, symbol: str, amount: float, params={})`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_margin_mode(self, marginMode: str, symbol: Str = None, params={})`
- `set_position_mode(self, hedged: bool, symbol: Str = None, params={})`
- `synthetic_trade_id(self, market=None, timestamp=None, side=None, amount=None, price=None, orderType=None, takerOrMaker=None)`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `spot_public_get_ping(request)`
- `spot_public_get_time(request)`
- `spot_public_get_exchangeinfo(request)`
- `spot_public_get_depth(request)`
- `spot_public_get_trades(request)`
- `spot_public_get_historicaltrades(request)`
- `spot_public_get_aggtrades(request)`
- `spot_public_get_klines(request)`
- `spot_public_get_avgprice(request)`
- `spot_public_get_ticker_24hr(request)`
- `spot_public_get_ticker_price(request)`
- `spot_public_get_ticker_bookticker(request)`
- `spot_public_get_etf_info(request)`
- `spot_private_get_order(request)`
- `spot_private_get_openorders(request)`
- `spot_private_get_allorders(request)`
- `spot_private_get_account(request)`
- `spot_private_get_mytrades(request)`
- `spot_private_get_tradefee(request)`
- `spot_private_get_sub_account_list(request)`
- `spot_private_get_sub_account_apikey(request)`
- `spot_private_get_capital_config_getall(request)`
- `spot_private_get_capital_deposit_hisrec(request)`
- `spot_private_get_capital_withdraw_history(request)`
- `spot_private_get_capital_withdraw_address(request)`
- `spot_private_get_capital_deposit_address(request)`
- `spot_private_get_capital_transfer(request)`
- `spot_private_get_capital_transfer_tranid(request)`
- `spot_private_get_capital_transfer_internal(request)`
- `spot_private_get_capital_sub_account_universaltransfer(request)`
- `spot_private_get_capital_convert(request)`
- `spot_private_get_capital_convert_list(request)`
- `spot_private_get_margin_loan(request)`
- `spot_private_get_margin_allorders(request)`
- `spot_private_get_margin_mytrades(request)`
- `spot_private_get_margin_openorders(request)`
- `spot_private_get_margin_maxtransferable(request)`
- `spot_private_get_margin_priceindex(request)`
- `spot_private_get_margin_order(request)`
- `spot_private_get_margin_isolated_account(request)`
- `spot_private_get_margin_maxborrowable(request)`
- `spot_private_get_margin_repay(request)`
- `spot_private_get_margin_isolated_pair(request)`
- `spot_private_get_margin_forceliquidationrec(request)`
- `spot_private_get_margin_isolatedmargindata(request)`
- `spot_private_get_margin_isolatedmargintier(request)`
- `spot_private_get_rebate_taxquery(request)`
- `spot_private_get_rebate_detail(request)`
- `spot_private_get_rebate_detail_kickback(request)`
- `spot_private_get_rebate_refercode(request)`
- `spot_private_get_rebate_affiliate_commission(request)`
- `spot_private_get_rebate_affiliate_withdraw(request)`
- `spot_private_get_rebate_affiliate_commission_detail(request)`
- `spot_private_get_mxdeduct_enable(request)`
- `spot_private_get_userdatastream(request)`
- `spot_private_get_selfsymbols(request)`
- `spot_private_post_order(request)`
- `spot_private_post_order_test(request)`
- `spot_private_post_sub_account_virtualsubaccount(request)`
- `spot_private_post_sub_account_apikey(request)`
- `spot_private_post_sub_account_futures(request)`
- `spot_private_post_sub_account_margin(request)`
- `spot_private_post_batchorders(request)`
- `spot_private_post_capital_withdraw_apply(request)`
- `spot_private_post_capital_withdraw(request)`
- `spot_private_post_capital_transfer(request)`
- `spot_private_post_capital_transfer_internal(request)`
- `spot_private_post_capital_deposit_address(request)`
- `spot_private_post_capital_sub_account_universaltransfer(request)`
- `spot_private_post_capital_convert(request)`
- `spot_private_post_mxdeduct_enable(request)`
- `spot_private_post_userdatastream(request)`
- `spot_private_put_userdatastream(request)`
- `spot_private_delete_order(request)`
- `spot_private_delete_openorders(request)`
- `spot_private_delete_sub_account_apikey(request)`
- `spot_private_delete_margin_order(request)`
- `spot_private_delete_margin_openorders(request)`
- `spot_private_delete_userdatastream(request)`
- `spot_private_delete_capital_withdraw(request)`
- `contract_public_get_ping(request)`
- `contract_public_get_detail(request)`
- `contract_public_get_support_currencies(request)`
- `contract_public_get_depth_symbol(request)`
- `contract_public_get_depth_commits_symbol_limit(request)`
- `contract_public_get_index_price_symbol(request)`
- `contract_public_get_fair_price_symbol(request)`
- `contract_public_get_funding_rate_symbol(request)`
- `contract_public_get_kline_symbol(request)`
- `contract_public_get_kline_index_price_symbol(request)`
- `contract_public_get_kline_fair_price_symbol(request)`
- `contract_public_get_deals_symbol(request)`
- `contract_public_get_ticker(request)`
- `contract_public_get_risk_reverse(request)`
- `contract_public_get_risk_reverse_history(request)`
- `contract_public_get_funding_rate_history(request)`
- `contract_private_get_account_assets(request)`
- `contract_private_get_account_asset_currency(request)`
- `contract_private_get_account_transfer_record(request)`
- `contract_private_get_position_list_history_positions(request)`
- `contract_private_get_position_open_positions(request)`
- `contract_private_get_position_funding_records(request)`
- `contract_private_get_position_position_mode(request)`
- `contract_private_get_order_list_open_orders_symbol(request)`
- `contract_private_get_order_list_history_orders(request)`
- `contract_private_get_order_external_symbol_external_oid(request)`
- `contract_private_get_order_get_order_id(request)`
- `contract_private_get_order_batch_query(request)`
- `contract_private_get_order_deal_details_order_id(request)`
- `contract_private_get_order_list_order_deals(request)`
- `contract_private_get_planorder_list_orders(request)`
- `contract_private_get_stoporder_list_orders(request)`
- `contract_private_get_stoporder_order_details_stop_order_id(request)`
- `contract_private_get_account_risk_limit(request)`
- `contract_private_get_account_tiered_fee_rate(request)`
- `contract_private_get_position_leverage(request)`
- `contract_private_post_position_change_margin(request)`
- `contract_private_post_position_change_leverage(request)`
- `contract_private_post_position_change_position_mode(request)`
- `contract_private_post_order_submit(request)`
- `contract_private_post_order_submit_batch(request)`
- `contract_private_post_order_cancel(request)`
- `contract_private_post_order_cancel_with_external(request)`
- `contract_private_post_order_cancel_all(request)`
- `contract_private_post_account_change_risk_level(request)`
- `contract_private_post_planorder_place(request)`
- `contract_private_post_planorder_cancel(request)`
- `contract_private_post_planorder_cancel_all(request)`
- `contract_private_post_stoporder_cancel(request)`
- `contract_private_post_stoporder_cancel_all(request)`
- `contract_private_post_stoporder_change_price(request)`
- `contract_private_post_stoporder_change_plan_price(request)`
- `spot2_public_get_market_symbols(request)`
- `spot2_public_get_market_coin_list(request)`
- `spot2_public_get_common_timestamp(request)`
- `spot2_public_get_common_ping(request)`
- `spot2_public_get_market_ticker(request)`
- `spot2_public_get_market_depth(request)`
- `spot2_public_get_market_deals(request)`
- `spot2_public_get_market_kline(request)`
- `spot2_public_get_market_api_default_symbols(request)`
- `spot2_private_get_account_info(request)`
- `spot2_private_get_order_open_orders(request)`
- `spot2_private_get_order_list(request)`
- `spot2_private_get_order_query(request)`
- `spot2_private_get_order_deals(request)`
- `spot2_private_get_order_deal_detail(request)`
- `spot2_private_get_asset_deposit_address_list(request)`
- `spot2_private_get_asset_deposit_list(request)`
- `spot2_private_get_asset_address_list(request)`
- `spot2_private_get_asset_withdraw_list(request)`
- `spot2_private_get_asset_internal_transfer_record(request)`
- `spot2_private_get_account_balance(request)`
- `spot2_private_get_asset_internal_transfer_info(request)`
- `spot2_private_get_market_api_symbols(request)`
- `spot2_private_post_order_place(request)`
- `spot2_private_post_order_place_batch(request)`
- `spot2_private_post_order_advanced_place_batch(request)`
- `spot2_private_post_asset_withdraw(request)`
- `spot2_private_post_asset_internal_transfer(request)`
- `spot2_private_delete_order_cancel(request)`
- `spot2_private_delete_order_cancel_by_symbol(request)`
- `spot2_private_delete_asset_withdraw(request)`
- `broker_private_get_sub_account_universaltransfer(request)`
- `broker_private_get_sub_account_list(request)`
- `broker_private_get_sub_account_apikey(request)`
- `broker_private_get_capital_deposit_subaddress(request)`
- `broker_private_get_capital_deposit_subhisrec(request)`
- `broker_private_get_capital_deposit_subhisrec_getall(request)`
- `broker_private_post_sub_account_virtualsubaccount(request)`
- `broker_private_post_sub_account_apikey(request)`
- `broker_private_post_capital_deposit_subaddress(request)`
- `broker_private_post_capital_withdraw_apply(request)`
- `broker_private_post_sub_account_universaltransfer(request)`
- `broker_private_post_sub_account_futures(request)`
- `broker_private_delete_sub_account_apikey(request)`

### WS Unified

- `describe(self)`
- `watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `watch_spot_public(self, channel, messageHash, params={})`
- `watch_spot_private(self, channel, messageHash, params={})`
- `watch_swap_public(self, channel, messageHash, requestParams, params={})`
- `watch_swap_private(self, messageHash, params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `get_cache_index(self, orderbook, cache)`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_balance(self, params={})`
- `un_watch_ticker(self, symbol: str, params={})`
- `un_watch_tickers(self, symbols: Strings = None, params={})`
- `un_watch_bids_asks(self, symbols: Strings = None, params={})`
- `un_watch_ohlcv(self, symbol: str, timeframe='1m', params={})`
- `un_watch_order_book(self, symbol: str, params={})`
- `un_watch_trades(self, symbol: str, params={})`
- `authenticate(self, subscriptionHash, params={})`
- `keep_alive_listen_key(self, listenKey, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.