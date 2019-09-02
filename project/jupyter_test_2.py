from vnpy.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting
from vnpy.app.cta_strategy.strategies.atr_rsi_strategy import (
AtrRsiStrategy,
)
from datetime import datetime
engine = BacktestingEngine()

engine.set_parameters(
vt_symbol="IF88.CFFEX",
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