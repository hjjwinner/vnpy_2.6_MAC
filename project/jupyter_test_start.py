from vnpy.trader.constant import (Exchange,Interval)
from vnpy.project.dataService import data_class_mongod
from vnpy.project.backTestingService import back_testing_service
from datetime import datetime


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

test_data = ts.run_testing(showData=False)
print(test_data)

# ts = back_testing_service()
# ts.vt_symbol = VT_SYMBOL
# ts.interval = INTERVAL
# ts.start = START
# ts.end = END
# ts.rate = 0.3 / 10000
# ts.slippage = 0.2
# ts.size = 300
# ts.pricetick = 0.2
# ts.capital = 1500_000
#
# test_data = ts.run_testing(showData=False)
# print(test_data)
#
# ts = back_testing_service()
# ts.vt_symbol = VT_SYMBOL
# ts.interval = INTERVAL
# ts.start = START
# ts.end = END
# ts.rate = 0.3 / 10000
# ts.slippage = 0.2
# ts.size = 300
# ts.pricetick = 0.2
# ts.capital = 3500_000
#
# test_data = ts.run_testing(showData=False)
# print(test_data)