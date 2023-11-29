import backtrader as bt

class ris_bollinger(bt.Strategy):
    
    params=(
        ("period", 20),
        ("devfactor", 2),
        ("rsi_period", 13)
    )
    
    def __init__(self):
        super().__init__()
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RelativeStrengthIndex(period=self.params.rsi_period)
        self.bollinger=bt.indicators.BollingerBands(self.data.close, period=self.params.period, devfactor=self.params.devfactor)
        
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    def next(self):
        
        rsi_value = self.rsi[0]
        
        if not self.position and self.dataclose <= self.bollinger.lines.bot and rsi_value < 30:
            cash_disponible = self.broker.get_cash()*0.95
            cash_disponible = cash_disponible-cash_disponible*0.001
            cant = int(cash_disponible/self.dataclose[0])
            self.log(f"BUY CREATE, {self.dataclose[0]} - Cantidad: {cant}")
            self.buy(size=cant)
            
        if self.position:
            if self.dataclose >= self.bollinger.lines.top and rsi_value > 70:
                self.log(f"SELL CREATE, {self.dataclose[0]}")
                self.sell(size=self.position.size)
           
    def notify_order(self, order):
        
        if order.status in [order.Accepted]:
            if order.isbuy():
                self.log(f"BUY ACCEPTED")
            elif order.issell():
                self.log("SELL ACCEPTED")
            return
        
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f"BUY EXECUTED, {order.executed.price}, comision: {order.executed.comm}, cantidad: {order.executed.size}")
            elif order.issell():
                self.log(f"SELL EXECUTED, {order.executed.price}")
                
        elif order.status in [order.Canceled]:
            self.log(f"ORDER CANCELED")
            
        elif order.status in [order.Margin]:
            self.log(f"ORDER MARGIN - Razón: {self.dataclose[0]}")
        
        elif order.status in [order.Rejected]:
            self.log(f"ORDER REJECTED")