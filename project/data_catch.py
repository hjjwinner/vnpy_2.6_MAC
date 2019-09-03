



class symbol_data(object):

    def __init__(self):
        self.symbolData = dict()
        pass

    def save_symbol_data(self, symbol=None, start=None, end=None, data=None):

        symbolDict = {'start' : start, 'end' :end, 'data': data}

        self.symbolData.update({symbol : symbolDict})
        pass

symbol_data_catch = symbol_data()
