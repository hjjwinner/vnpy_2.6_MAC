import pandas as pd
import quandl
from datetime import date

quandl.ApiConfig.api_key = "RA-eYfxupP66K5-pM6jA"


start = date(2017, 1, 1)
end = date.today()
# apple = quandl.get("WIKI/AAPL", start_date=start, end_date=end)
# mydata = quandl.get("FRED/GDP", returns="numpy")
# print(mydata)
# print(apple)
# data = quandl.get_table('ZACKS/FC', ticker='BABA')
# print(data)


import pandas_datareader as pdr


df = pdr.get_data_yahoo('BABA')
print(df)