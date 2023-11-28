import backtrader as bt

class Bollinger(bt.Strategy):
    params = (
        ("period", 30),
        ("devfactor", 2),
    )

    
    def __init__(self):
        super().__init__()
        self.dataclose = self.datas[0].close
        self.bollinger =bt.indicators.BollingerBands(self.data.close, period=self.params.period, devfactor=self.params.devfactor)
    
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
    
    def next(self):
        if self.dataclose <= self.bollinger.lines.bot and not self.position:
            self.log(f"BUY CREATE, {self.dataclose[0]} - Line Bot: {self.bollinger.lines.bot}")
            self.buy()
        elif self.dataclose >= self.bollinger.lines.top and self.position:
            self.log(f"SELL CREATE, {self.dataclose[0]} - Line Tot: {self.bollinger.lines.top}")
            self.sell()