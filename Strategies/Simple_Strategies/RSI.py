import backtrader as bt

class RSI(bt.Strategy):
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RelativeStrengthIndex()
        
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    def next(self):

        rsi_value = self.rsi[0]
        
        if not self.position:
            if rsi_value < 30:
                self.log(f"BUY CREATE, {self.dataclose[0]} - RSI {rsi_value}")
                self.buy()
        else:
            if rsi_value > 70:
                self.log(f"SELL CREATE, {self.dataclose[0]} - RSI {rsi_value}")
                self.sell()