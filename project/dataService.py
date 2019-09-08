from vnpy.trader.rqdata import rqdata_client
from vnpy.trader.database import database_manager
from vnpy.trader.object import (HistoryRequest)
from vnpy.trader.constant import (Exchange, Interval)
from datetime import datetime
import rqdatac as rq


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
        else:
            print('2')


        # print(data)
        if data:
            database_manager.save_bar_data(data)



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


# date_down = data_class_mongod()
# date_down.query_bar_from_rq(vt_symbol='CU99.CFFEX', interval=Interval.MINUTE, start=datetime(2019, 1, 1), end=datetime(2019, 9, 1))
