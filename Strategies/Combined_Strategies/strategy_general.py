import backtrader as bt


class Strategy_General(bt.Strategy):
    
    params = (
        ('allocation', 0.95),
        ('commision', 0.001)
    )
    
    def __init__(self):
        super().__init__()
        
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    def vol_buy(self) -> int:
        if self.broker.cash >= self.dataclose[0]:
            cash = self.broker.get_cash()*self.params.allocation
            cash = cash-cash*self.params.commision
            return int(cash/self.dataclose[0])
        return 0
    
    def notify_order(self, order):
        
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f, COMM: %.2f, SIZE: %i' % (order.executed.price, order.executed.comm, order.executed.size))
            elif order.issell():
                self.log('SELL EXECUTED, %.2f, COMM: %.2f, SIZE: %i' % (order.executed.price, order.executed.comm, order.executed.size))
                
        elif order.status in [order.Canceled]:
            self.log("ORDER CANCELED")
            
        elif order.status in [order.Margin]:
            self.log("ORDER MARGIN")
        
        elif order.status in [order.Rejected]:
            self.log("ORDER REJECTED")