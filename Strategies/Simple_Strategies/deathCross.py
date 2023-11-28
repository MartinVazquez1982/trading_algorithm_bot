import backtrader as bt

class DeathCross(bt.Strategy):
    
    def __init__(self):
        super().__init__()
        self.dataclose = self.datas[0].close
        self.sma50 = bt.indicators.MovingAverageSimple(self.data.close, period=50)
        self.sma200 = bt.indicators.MovingAverageSimple(self.data.close, period=200)
        
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    def next(self):
        
        if self.position:
            
            if self.sma50[0] < self.sma200[0]:
                self.log(f"SELL CREATE, {self.dataclose[0]} - SMA (P = 50) {self.sma50[0]} - SMA (P = 200) {self.sma200[0]}")
                self.sell()