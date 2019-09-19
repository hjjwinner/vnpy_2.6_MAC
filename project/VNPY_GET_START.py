# from vnpy.event import EventEngine
#
# from vnpy.trader.engine import MainEngine
# from vnpy.trader.ui import MainWindow, create_qapp
#
# from vnpy.app.cta_strategy import CtaStrategyApp
# from vnpy.app.csv_loader import CsvLoaderApp
# from vnpy.app.algo_trading import AlgoTradingApp
# from vnpy.app.cta_backtester import CtaBacktesterApp
#
# # 也可以 import 修改版的 TigerGateway
# from vnpy.gateway.tiger import TigerGateway
#
# def main():
#     """"""
#     qapp = create_qapp()
#
#     event_engine = EventEngine()
#
#     main_engine = MainEngine(event_engine)
#
#     main_engine.add_gateway(TigerGateway)
#
#     main_engine.add_app(CtaStrategyApp)
#     main_engine.add_app(CtaBacktesterApp)
#     main_engine.add_app(CsvLoaderApp)
#     main_engine.add_app(AlgoTradingApp)
#
#     main_window = MainWindow(main_engine, event_engine)
#     main_window.showMaximized()
#
#     qapp.exec()
#
#
# if __name__ == "__main__":
#     main()

