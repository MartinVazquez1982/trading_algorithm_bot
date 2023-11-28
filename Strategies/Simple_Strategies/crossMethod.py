import backtrader as bt

class CrossMethod(bt.Strategy):
    
    def __init__(self):
        super().__init__()
        self.dataclose = self.datas[0].close
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=20)
        
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
    
    def next(self):
        
        # Realiza la operacion si tengo en cartera la accion
        if not self.position:
        
            # Compra si el precio paso de abajo hacia arriba de la Simple Moving Averange
            if self.dataclose[0] > self.sma[0]:
                self.log(f"BUY CREATE, {self.dataclose[0]} - Simple Moving Averange, {self.sma[0]}")
                self.buy()
            
            # Vende si el precio paso de arriba hacia abajo de la Simple Moving Averange
        elif self.dataclose[0] < self.sma[0]:
            self.log(f"SELL CREATE, {self.dataclose[0]} - Simple Moving Averange, {self.sma[0]}")
            self.sell()
            
            # Impresion precio de cierre 
        else:
            self.log('Close, %.2f' % self.dataclose[0])
    
    def notify_order(self, order):
        
        if order.status in [order.Accepted]:
            if order.isbuy():
                self.log("BUY ACCEPTED")
            elif order.issell():
                self.log("SELL ACCEPTED")
            return
        
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f"BUY EXECUTED, {order.executed.price}")
            elif order.issell():
                self.log(f"SELL EXECUTED, {order.executed.price}")
                
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('ORDER CANCELED/MARGIN/REJECTED')
