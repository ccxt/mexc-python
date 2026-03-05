import sys
import mexc.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from mexc.ccxt import mexc as MexcSync
from mexc.ccxt.async_support.mexc import mexc as MexcAsync
from mexc.ccxt.pro.mexc import mexc as MexcWs
