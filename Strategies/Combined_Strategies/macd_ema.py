import backtrader as bt

class macd_ema(bt.Strategy):
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.macd = bt.indicators.MACDHisto()
        self.ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=200)
        
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
    
    def next(self):
        
        macd_value = self.macd.macd[0]
        signal_value = self.macd.signal[0]
        
        if not self.position and self.ema[0] < self.dataclose[0]:
            if  macd_value > signal_value and macd_value > 0 and signal_value > 0 :
                cash_disponible = self.broker.get_cash()*0.95
                cash_disponible = cash_disponible-cash_disponible*0.001
                cant = int(cash_disponible/self.dataclose[0])
                self.log(f"BUY CREATE, {self.dataclose[0]}")
                self.buy(size=cant)
        
        elif self.position and macd_value < 0 and signal_value < 0 and  macd_value < signal_value and self.ema[0] > self.dataclose[0]:
            self.log(f"SELL CREATE, {self.dataclose[0]}")
            self.sell(size=self.position.size)
        
