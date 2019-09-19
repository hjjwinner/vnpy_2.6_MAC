from datetime import datetime, timedelta
from vnpy.trader.rqdata import rqdata_client
from vnpy.trader.database import database_manager
from vnpy.trader.object import (HistoryRequest)
from vnpy.trader.constant import (Exchange, Interval)
from vnpy.trader.object import BarData, HistoryRequest
from datetime import datetime
from typing import List
import rqdatac as rq

import tushare as ts


INTERVAL_ADJUSTMENT_MAP = {
    Interval.MINUTE: timedelta(minutes=1),
    Interval.HOUR: timedelta(hours=1),
    Interval.DAILY: timedelta()         # no need to adjust for daily bar
}



class data_class_mongod(object):

    def __init__(self):
        self.vt_symbol = None
        self.interval = Interval.MINUTE
        self.exchange = Exchange.CFFEX
        self.start = None
        self.end = None
        self.init_rqdata()
        pass

    def init_rqdata(self):
        """
        Init RQData client.
        """
        username = "license"
        password = "hNquASLMnsj6XvN7244jRy9wAiGGpGKcS-mrlPpND9TOUajZD61S2KjTfEEv22szfARmC7Ab4sOWcHGBlc8sJSKjQUxgxGm_uxYmwDmszQoGsr3qrdC1fgvDiTtBtuy3KtdngdyY6kOrkXOnu0hi5-de7Avdfl_riZUc_Yk2DAU=N78cYFYpV95cAStJFo0qcsV6fHuLFainVSspsleIUzgT6gLrld0cV6RU2MsLJX0M6eHKjjkAxfL4ypilQvowHwKUBybdi94hhGOfZ_GmV_GMEDitnM40HoVCYErA4fm_7melaRGHrQBUbcqQQZ2gu3rtmZWQgcIUTTFc6QI-tCM="

        if not username or not password:
            return
        rq.init(username, password,
                ('rqdatad-pro.ricequant.com', 16011))
        return rq

    def query_bar_from_rq_list(
            self, vt_symbol: str, interval: Interval, start: datetime, end: datetime
    ):
        """
        Query bar data from RQData.
        """
        symbol, exchange_str = vt_symbol.split(".")

        req = HistoryRequest(
            symbol=symbol,
            exchange=Exchange.CFFEX,
            interval=Interval(interval),
            start=start,
            end=end
        )
        rqdata_client.symbols.add('CU99')
        data = rqdata_client.query_history(req)

        if data:
            database_manager.save_bar_data(data)

    def query_bar_from_rq(self):
        """
        Query bar data from RQData.
        """
        symbol, exchange_str = self.vt_symbol.split(".")

        if exchange_str == 'CFFEX':
            self.exchange = Exchange.CFFEX
        elif exchange_str == 'SHFE':
            self.exchange = Exchange.SHFE
        elif exchange_str == 'CZCE':
            self.exchange = Exchange.CZCE
        elif exchange_str == 'DCE':
            self.exchange = Exchange.DCE
        elif exchange_str == 'INE':
            self.exchange = Exchange.INE
        elif exchange_str == 'SSE':
            self.exchange = Exchange.SSE
        elif exchange_str == 'SZSE':
            self.exchange = Exchange.SZSE
        elif exchange_str == 'SGE':
            self.exchange = Exchange.SGE
        elif exchange_str == 'WXE':
            self.exchange = Exchange.WXE
        print('self.exchange=' )
        print(self.exchange)
        req = HistoryRequest(
            symbol=symbol,
            exchange=self.exchange,
            interval=Interval(self.interval),
            start=self.start,
            end=self.end
        )
        rqdata_client.symbols.add(symbol)
        data = rqdata_client.query_history(req)
        try:
            print(len(data))
        except:
            print('1')



        # print(data)
        if data:
            database_manager.save_bar_data(data)


    def query_bar_from_tushare(self):
        ts.set_token('e9e8888a3999e16583f0221e6af7d9f3e4bbca70f6bbc84169808d0c')
        pro = ts.pro_api()
        data = pro.query('stock_basic', exchange='', list_status='L',
                         fields='ts_code,symbol,name,area,industry,list_date')
        print(data)

        vtsymbol = '000002.SZ'
        data_daily = pro.query('daily', ts_code=vtsymbol, start_date='20170701', end_date='20190718')

        print(data_daily)

        data_bar = self.symbol_data_to_Bar(df=data_daily, vt_symbol=vtsymbol, interval=Interval.DAILY, star='20170701', end=datetime(2019, 7, 18))

        print(data_bar)


    """
    3663  688066.SH  688066   航天宏图   北京     软件服务  20190722
    3664  688088.SH  688088   虹软科技   浙江     软件服务  20190722
    3665  688099.SH  688099   晶晨股份   上海      半导体  20190808
    3666  688122.SH  688122   西部超导   陕西      小金属  20190722
    3667  688168.SH  688168   N安博通   北京     软件服务  20190906
    """




    def query_bar_from_rq_base(self):
        symbol, exchange_str = self.vt_symbol.split(".")

        req = HistoryRequest(
            symbol=symbol,
            exchange=self.exchange,
            interval=Interval(self.interval),
            start=self.start,
            end=self.end
        )
        rqdata_client.symbols.add(symbol)
        data = rqdata_client.query_history(req)
        print(len(data))
        print(data)
        if data:
            database_manager.save_bar_data(data)



    def symbol_data_to_Bar(self,df=None,vt_symbol=None,interval=None,star=None,end=None):

        # For adjust timestamp from bar close point (RQData) to open point (VN Trader)
        adjustment = INTERVAL_ADJUSTMENT_MAP[interval]

        # For querying night trading period data
        end += timedelta(1)

        symbol, exchange_str = self.vt_symbol.split(".")
        data: List[BarData] = []

        if df is not None:
            for ix, row in df.iterrows():
                bar = BarData(
                    symbol=symbol,
                    exchange=exchange_str,
                    interval=Interval(self.interval),
                    datetime=row.name.to_pydatetime() - adjustment,
                    open_price=row["open"],
                    high_price=row["high"],
                    low_price=row["low"],
                    close_price=row["close"],
                    volume=row["volume"],
                    gateway_name="RQ"
                )
                data.append(bar)

        return data



# date_down = data_class_mongod()
# date_down.query_bar_from_rq(vt_symbol='CU99.CFFEX', interval=Interval.MINUTE, start=datetime(2019, 1, 1), end=datetime(2019, 9, 1))
