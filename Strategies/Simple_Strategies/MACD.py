import backtrader as bt

class MACD(bt.Strategy):
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.macd = bt.indicators.MACDHisto()
        
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    def next(self):
        
        macd_value = self.macd.macd[0]
        signal_value = self.macd.signal[0]
        
        if not self.position:
            
            if macd_value > signal_value:
                self.log(f"BUY CREATE, {self.dataclose[0]} - MACD Value {macd_value} - Signal Value {signal_value}")
                self.buy()
        
        else:
            
            if macd_value < signal_value:
                self.log(f"SELL CREATE, {self.dataclose[0]} - MACD Value {macd_value} - Signal Value {signal_value}")
                self.sell()