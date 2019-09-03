from vnpy.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting
from vnpy.app.cta_strategy.strategies.atr_rsi_strategy import (
AtrRsiStrategy,
)
from vnpy.trader.constant import (
    Interval,
)

from datetime import datetime


class back_testing_service():

    def __init__(self):

        self.vt_symbol= "CU99.CFFEX"
        self.interval=Interval.MINUTE
        self.start = datetime(2018, 1, 1)
        self.end = datetime(2019, 9, 1)
        self.rate = 0.3 / 10000
        self.slippage = 0.2
        self.size = 300
        self.pricetick = 0.2
        self.capital = 1_000_000



    def run_testing(self, showData=True):
        engine = BacktestingEngine()

        engine.set_parameters(
            vt_symbol=self.vt_symbol,
            interval=self.interval,
            start=self.start,
            end=self.end,
            rate=self.rate,
            slippage=self.slippage,
            size=self.size,
            pricetick=self.pricetick,
            capital=self.capital,
        )
        engine.add_strategy(AtrRsiStrategy, {})
        engine.load_data()
        engine.run_backtesting()
        df = engine.calculate_result()
        test_resure =  engine.calculate_statistics(df, output=showData)
        if showData:
            engine.show_chart(df)
        return test_resure