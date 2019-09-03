from vnpy.trader.constant import (Exchange,Interval)
from vnpy.project.dataService import data_class_mongod
from vnpy.project.backTestingService import back_testing_service
from datetime import datetime
from vnpy.app.cta_strategy.strategies.atr_rsi_strategy import (
AtrRsiStrategy,
)
import time

VT_SYMBOL = 'IF99.CFFEX'
INTERVAL= Interval.MINUTE
START=datetime(2019, 1, 1)
END=datetime(2019, 9, 1)

# date_down = data_class_mongod()
# date_down.vt_symbol = VT_SYMBOL
# date_down.interval = INTERVAL
# date_down.start = START
# date_down.end = END
# date_down.query_bar_from_rq()

def run_Template_testing(template=None):
    ts = back_testing_service()
    ts.vt_symbol = VT_SYMBOL
    ts.interval = INTERVAL
    ts.start = START
    ts.end = END
    ts.rate = 0.3 / 10000
    ts.slippage = 0.2
    ts.size = 300
    ts.pricetick = 0.2
    ts.capital = 500_000
    test_data = ts.run_testing(showData=False,Template=template)
    print(test_data)
    return test_data




def run_AtrRsiStrategy():
    atr_length = 1
    atr_ma_length = 5
    rsi_length = 1
    rsi_entry = 1
    trailing_percent = 0.2
    fixed_size = 1

    resure = {}

    while atr_length < 20:
        atr_length += 1
        atr_ma_length = 1

        while atr_ma_length < 20:
            atr_ma_length += 1
            rsi_length = 1

            while rsi_length < 10:
                rsi_length += 1
                rsi_entry = 1

                while rsi_entry < 5:
                    rsi_entry += 1
                    trailing_percent = 0.4

                    while trailing_percent < 2:
                        trailing_percent += 0.4
                        fixed_size = 1

                        while fixed_size < 3:
                            fixed_size += 1

                            AtrRsiStrategy.atr_length = atr_length
                            AtrRsiStrategy.atr_ma_length = atr_ma_length
                            AtrRsiStrategy.rsi_length = rsi_length
                            AtrRsiStrategy.rsi_entry = rsi_entry
                            AtrRsiStrategy.trailing_percent = trailing_percent
                            AtrRsiStrategy.fixed_size = fixed_size
                            print("-------")
                            print(atr_length, atr_ma_length, rsi_length, rsi_entry, trailing_percent, fixed_size)
                            data = run_Template_testing(AtrRsiStrategy)
                            # time.sleep(5)
                            if len(resure) == 0:
                                resure = data
                            else:
                                if data['sharpe_ratio'] > resure['sharpe_ratio']:
                                    resure = data
                                    resure['template'] = {'atr_length':atr_length,
                                                        'atr_ma_length': atr_ma_length,
                                                        'rsi_length': rsi_length,
                                                        'rsi_entry': rsi_entry,
                                                        'trailing_percent': trailing_percent,
                                                        'fixed_size': fixed_size,
                                                        }

    print(resure['template'])
    print(resure)





run_AtrRsiStrategy()



def run_Template_testing_resure(template=None):

    ts = back_testing_service()
    ts.vt_symbol = VT_SYMBOL
    ts.interval = INTERVAL
    ts.start = START
    ts.end = END
    ts.rate = 0.3 / 10000
    ts.slippage = 0.2
    ts.size = 300
    ts.pricetick = 0.2
    ts.capital = 500_000
    test_data = ts.run_testing(showData=True,Template=template)
    print(test_data)
    return test_data

# AtrRsiStrategy.atr_length = 2
# AtrRsiStrategy.atr_ma_length = 2
# AtrRsiStrategy.rsi_length = 2
# AtrRsiStrategy.rsi_entry = 2
# AtrRsiStrategy.trailing_percent = 0.8
# AtrRsiStrategy.fixed_size = 5
# run_Template_testing_resure(AtrRsiStrategy)