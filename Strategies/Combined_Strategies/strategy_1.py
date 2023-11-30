from Strategies.Combined_Strategies import strategy_general as sg
import backtrader as bt

class Strategy1(sg.Strategy_General):
    
    def __init__(self):
        self.macd = bt.indicators.MACDHisto()
        self.ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=200)  
        self.dataclose = self.datas[0].close
    
    def next(self):
        
        macd_value = self.macd.macd[0]
        signal_value = self.macd.signal[0]
        
        if not self.position and self.ema[0] < self.dataclose[0]:
            if  macd_value > signal_value and macd_value > 0 and signal_value > 0 :
                cant = self.vol_buy()
                self.log(f"BUY CREATE, {self.dataclose[0]}")
                self.buy(size=cant)
        
        elif self.position and self.ema[0] > self.dataclose[0]: 
            if  macd_value < signal_value and macd_value < 0 and signal_value < 0:
                self.log(f"SELL CREATE, {self.dataclose[0]}")
                self.sell(size=self.position.size)
        
