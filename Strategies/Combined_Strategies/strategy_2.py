from Strategies.Combined_Strategies import strategy_general as sg

import backtrader as bt

class Strategy2(sg.Strategy_General):
    
    params=(
        ("period", 30),
        ("devfactor", 2),
        ("rsi_period", 13)
    )
    
    def __init__(self):
        super().__init__()
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RelativeStrengthIndex(period=self.params.rsi_period)
        self.bollinger=bt.indicators.BollingerBands(self.data.close, period=self.params.period, devfactor=self.params.devfactor)
    
        
    def next(self):
        
        rsi_value = self.rsi[0]
        
        if not self.position and self.dataclose <= self.bollinger.lines.bot and rsi_value < 30:
            cant = self.vol_buy()
            self.log(f"BUY CREATE, {self.dataclose[0]} - Cantidad: {cant}")
            self.buy(size=cant)
            
        if self.position and self.dataclose >= self.bollinger.lines.top and rsi_value > 70:
            self.log(f"SELL CREATE, {self.dataclose[0]}")
            self.sell(size=self.position.size)
           