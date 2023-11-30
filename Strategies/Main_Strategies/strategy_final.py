import backtrader as bt

class Strategy_General(bt.Strategy):
    
    params = (
        ("period_short_sma", 20),
        ("period_long_sma", 50),
        ("rsi_period", 14),
        ("macd_short", 12),
        ("macd_long", 26),
        ("macd_signal", 9),
        ("bollinger_period", 20),
        ("bollinger_dev", 2),
        ("adx_period", 14),
        ("adx_threshold", 25),
        ("allocation", 0.95),
        ("commision", 0.001),
    )
    
    def __init__(self):
        super().__init__()
        self.dataclose = self.datas[0].close
        self.short_sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.period_short_sma)
        self.long_sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.period_long_sma)
        self.rsi = bt.indicators.RelativeStrengthIndex(period=self.params.rsi_period)
        self.macd = bt.indicators.MACDHisto(
            period_me1=self.params.macd_short,
            period_me2=self.params.macd_long,
            period_signal=self.params.macd_signal
        )
        self.bollinger = bt.indicators.BollingerBands(
            self.data.close,
            period=self.params.bollinger_period,
            devfactor=self.params.bollinger_dev
        )
        self.adx = bt.indicators.AverageDirectionalMovementIndex(period=self.params.adx_period)
        
        
    def log(self, txt, dt=None):
        
        ''' Logging function for this strategy'''
        
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    def vol_buy(self) -> int:
        
        '''Calculate the volumen of buy'''
        
        if self.broker.cash >= self.dataclose[0]:
            cash = self.broker.get_cash()*self.params.allocation
            cash = cash-cash*self.params.commision
            return int(cash/self.dataclose[0])
        return 0
    
    def conditions_buy(self):
        
        '''If 3 indicators return True, the buy is made'''
        
        conditions = [
            self.short_sma[0] > self.long_sma[0],
            self.rsi[0] < 30,
            self.macd.macd[0] > 0 and self.macd.signal[0] > 0 and self.macd.macd[0] > self.macd.signal[0],
            self.dataclose[0] < self.bollinger.lines.bot,
            self.adx > self.params.adx_threshold,
        ]

        return sum(conditions) >= 3 
    
    def conditions_sell(self):
        
        '''If 3 indicators return True, the sell is made'''
        
        conditions = [
            self.short_sma[0] < self.long_sma[0],
            self.rsi[0] > 70,
            self.macd.macd[0] < 0 and self.macd.signal[0] < 0 and self.macd.macd[0] < self.macd.signal[0],
            self.dataclose[0] > self.bollinger.lines.top,
        ]

        return sum(conditions) >= 3
        
    def next(self):
        
        '''Invoked if there are changes in market data'''
        
        if not self.position and  self.conditions_buy():
            vol = self.vol_buy()
            if vol > 0:
                self.log('BUY CREATE, %.2f - Cantidad: %i' % (self.dataclose[0], vol))
                self.buy(size=vol)

        elif self.position and self.conditions_sell():
            self.log(f"SELL CREATE, {self.dataclose[0]}")
            self.sell(size=self.position.size)
    
    def notify_order(self, order):
        
        '''Notifies if the order has been executed, canceled, margin or rejeted'''
        
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