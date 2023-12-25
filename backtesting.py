import backtrader as bt
import pandas as pd
import yfinance as yf
import csv
class SupportResistanceStrategy(bt.Strategy):
    params = (
        ("support_period", 20),
        ("resistance_period", 20),
    )

    def __init__(self):
        self.support_period = self.params.support_period
        self.resistance_period = self.params.resistance_period
        self.support, self.resistance = self.calculate_support_resistance()

    def calculate_support_resistance(self):

        data = pd.DataFrame(self.data.get(size=self.support_period * 2))  # Use more data for calculation
        print(data)
        support = data['low'].rolling(window=self.support_period).min()
        resistance = data['high'].rolling(window=self.resistance_period).max()
        return support.values, resistance.values

    def next(self):
        if self.data.close > self.resistance[-1]:
            self.sell()
        elif self.data.close < self.support[-1]:
            self.buy()


class BreakoutStrategy(bt.Strategy):
    params = (
        ("resistance_period", 20),
    )

    def __init__(self):
        self.resistance_period = self.params.resistance_period
        self.resistance = self.calculate_resistance()

    def calculate_resistance(self):
        data = pd.DataFrame(self.data.get(size=self.resistance_period * 2))  # Use more data for calculation
        print(data.columns)  # Print column names
        return data['Low'].rolling(window=self.resistance_period).max().values

    def next(self):
        if self.data.close > self.resistance[-1]:
            self.buy()
         
class RandomStrategy(bt.Strategy):
    params = (
        ("short_period", 50),
        ("long_period", 200),
    )

    def __init__(self):
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_period)

    def next(self):
        if self.short_ma > self.long_ma:
            self.buy()
        elif self.short_ma < self.long_ma:
            self.sell()
   

def run_strategy(strategy, data, symbol):
    cerebro = bt.Cerebro()
    cerebro.adddata(bt.feeds.PandasData(dataname=data))
    cerebro.addstrategy(strategy)

    # Set the initial cash amount for backtesting
    cerebro.broker.set_cash(100000)

    # Set commission
    cerebro.broker.setcommission(commission=0.001)

    # Print the starting cash amount
    print(f"\nRunning {strategy.__name__} strategy for {symbol}:")
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")

    # Run the backtest
    cerebro.run()

    # Print the final cash amount
    print(f"Ending Portfolio Value: {cerebro.broker.getvalue()}")

def main():
    # Replace 'indian_stock_list.csv' with the path to your CSV file containing Indian stock symbols
    stock_list_path = 'indian_stock_list.csv'
    stock_symbols = pd.read_csv(stock_list_path)['Symbol'].tolist()

    for symbol in stock_symbols:
        data = yf.download(symbol, start="2022-01-01", end="2023-01-01")
        print(data.columns)  # Print column names
        run_strategy(RandomStrategy, data, symbol)

if __name__ == "__main__":
    main()


