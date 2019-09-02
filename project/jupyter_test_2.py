from vnpy.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting
from vnpy.app.cta_strategy.strategies.atr_rsi_strategy import (
AtrRsiStrategy,
)

from vnpy.trader.constant import Interval

from vnpy.trader.rqdata import rqdata_client
# from vnpy.app.cta_strategy.engine import
from vnpy.trader.database import database_manager



from vnpy.trader.object import (
    #OrderRequest,
    #SubscribeRequest,
    HistoryRequest,
    #LogData,
    #TickData,
    BarData,
    #ContractData
)

from vnpy.trader.constant import (
    Direction,
    OrderType,
    Interval,
    Exchange,
    Offset,
    Status
)



from datetime import datetime
engine = BacktestingEngine()



engine.set_parameters(
vt_symbol="CU99.CFFEX",
interval="1m",
start=datetime(2019, 4, 30),
end=datetime(2019, 8, 20),
rate=0.3/10000,
slippage=0.2,
size=300,
pricetick=0.2,
capital=1_000_000,
)
engine.add_strategy(AtrRsiStrategy, {})
engine.load_data()
engine.run_backtesting()
df = engine.calculate_result()
engine.calculate_statistics(df)
engine.show_chart(df)






########
import rqdatac as rq

class dataClass_mongod():

    def __init__(self):
        pass

    def init_rqdata(self):
        """
        Init RQData client.
        """
        # username = SETTINGS["rqdata.username"]
        # password = SETTINGS["rqdata.password"]
        username = "license"
        password = "hNquASLMnsj6XvN7244jRy9wAiGGpGKcS-mrlPpND9TOUajZD61S2KjTfEEv22szfARmC7Ab4sOWcHGBlc8sJSKjQUxgxGm_uxYmwDmszQoGsr3qrdC1fgvDiTtBtuy3KtdngdyY6kOrkXOnu0hi5-de7Avdfl_riZUc_Yk2DAU=N78cYFYpV95cAStJFo0qcsV6fHuLFainVSspsleIUzgT6gLrld0cV6RU2MsLJX0M6eHKjjkAxfL4ypilQvowHwKUBybdi94hhGOfZ_GmV_GMEDitnM40HoVCYErA4fm_7melaRGHrQBUbcqQQZ2gu3rtmZWQgcIUTTFc6QI-tCM="

        if not username or not password:
            return


        # self.rq_client = rq
        rq.init(username, password,
                            ('rqdatad-pro.ricequant.com', 16011))

        return rq



    def query_bar_from_rq(
            self, vt_symbol: str, interval: Interval, start: datetime, end: datetime
    ):
        """
        Query bar data from RQData.
        """
        symbol, exchange_str = vt_symbol.split(".")
        # rq_symbol = self.to_rq_symbol(vt_symbol, exchange_str)
        # if rq_symbol not in self.rq_symbols:
        #     return None

        # end += timedelta(1)  # For querying night trading period data

        req = HistoryRequest(
            symbol=symbol,
            exchange=Exchange.CFFEX,
            interval=Interval(interval),
            start=start,
            end=end
        )
        rqdata_client.symbols.add('CU99')
        data = rqdata_client.query_history(req)
        print(type(data))
        if data:
            database_manager.save_bar_data(data)

        # df = rq.get_price(
        #     symbol,
        #     frequency=interval.value,
        #     fields=["open", "high", "low", "close", "volume"],
        #     start_date=start,
        #     end_date=end
        # )
        # df = rq.get_price(symbol, frequency='1d', fields=["open", "high", "low", "close", "volume"], start_date='2019-01-01',
        #                   end_date=datetime.now().strftime('%Y%m%d'))
        #
        # data = []
        # for ix, row in df.iterrows():
        #     bar = BarData(
        #         symbol=symbol,
        #         exchange=Exchange(exchange_str),
        #         interval=interval,
        #         datetime=row.name.to_pydatetime(),
        #         open_price=row["open"],
        #         high_price=row["high"],
        #         low_price=row["low"],
        #         close_price=row["close"],
        #         volume=row["volume"],
        #         gateway_name="RQ"
        #     )
        #     data.append(bar)





# date_down = dataClass_mongod()
# date_down.init_rqdata()
# date_down.query_bar_from_rq(vt_symbol='CU99.CFFEX', interval=Interval.MINUTE, start=datetime(2019, 1, 1), end=datetime(2019, 9, 1))

















