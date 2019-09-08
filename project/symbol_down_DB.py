import rqdatac
from rqdatac import *
import pandas as pd
from vnpy.project.dataService import data_class_mongod
from vnpy.trader.constant import (Exchange,Interval)
from datetime import datetime

def get_all_instruments():
    username = "license"
    password = "hNquASLMnsj6XvN7244jRy9wAiGGpGKcS-mrlPpND9TOUajZD61S2KjTfEEv22szfARmC7Ab4sOWcHGBlc8sJSKjQUxgxGm_uxYmwDmszQoGsr3qrdC1fgvDiTtBtuy3KtdngdyY6kOrkXOnu0hi5-de7Avdfl_riZUc_Yk2DAU=N78cYFYpV95cAStJFo0qcsV6fHuLFainVSspsleIUzgT6gLrld0cV6RU2MsLJX0M6eHKjjkAxfL4ypilQvowHwKUBybdi94hhGOfZ_GmV_GMEDitnM40HoVCYErA4fm_7melaRGHrQBUbcqQQZ2gu3rtmZWQgcIUTTFc6QI-tCM="

    rq = rqdatac.init(username, password, ('rqdatad-pro.ricequant.com', 16011))
    data = all_instruments(type='Future', market='cn')
    instruments_list = data['order_book_id']
    id_convert_list = []
    for id in instruments_list:
        print(type(id))
        print(id)
        converid = id_convert(id)
        id_convert_list.append(converid)

    pd_convert_id_list = pd.DataFrame(id_convert_list)
    data['convertid'] = pd_convert_id_list
    pd_convert_id_list.to_csv('id_convert.csv')
    data.to_csv('Future_conver.csv')
    return data

# get_all_instruments()


def danlown_symbol(symbol):
    VT_SYMBOL = symbol
    INTERVAL = Interval.MINUTE
    START = datetime(2014, 1, 1)
    END = datetime(2019, 9, 7)

    date_down = data_class_mongod()
    date_down.vt_symbol = VT_SYMBOL
    date_down.interval = INTERVAL
    date_down.start = START
    date_down.end = END
    date_down.query_bar_from_rq()


Future_conver= pd.read_csv('Future_conver.csv')
for index, row in Future_conver.iterrows():
    if index < 100:
        print(index)
        # symbol =''
        # symbol = row['convertid']

        symbol = f"{row['convertid']}.{row['exchange']}"
        print(symbol)
        danlown_symbol(symbol)


def get_all_instruments_CS():
    username = "license"
    password = "hNquASLMnsj6XvN7244jRy9wAiGGpGKcS-mrlPpND9TOUajZD61S2KjTfEEv22szfARmC7Ab4sOWcHGBlc8sJSKjQUxgxGm_uxYmwDmszQoGsr3qrdC1fgvDiTtBtuy3KtdngdyY6kOrkXOnu0hi5-de7Avdfl_riZUc_Yk2DAU=N78cYFYpV95cAStJFo0qcsV6fHuLFainVSspsleIUzgT6gLrld0cV6RU2MsLJX0M6eHKjjkAxfL4ypilQvowHwKUBybdi94hhGOfZ_GmV_GMEDitnM40HoVCYErA4fm_7melaRGHrQBUbcqQQZ2gu3rtmZWQgcIUTTFc6QI-tCM="

    rqdatac.init(username, password, ('rqdatad-pro.ricequant.com', 16011))
    data = all_instruments(type='CS')
    return data


# danlown_symbol('000001.XSHE')







def load_all_instruments_csv():
    Future_conver = pd.read_csv('Future_conver.csv')
    for index, row in Future_conver.iterrows():
        if index < 5:
            print(index)
            symbol = f"{row['convertid']}.{row['exchange']}"

    return Future_conver