import datetime
import os.path
import sys

from Strategies.Simple_Strategies import crossMethod as cm
from Strategies.Simple_Strategies import goldenCross as gc
from Strategies.Simple_Strategies import deathCross as dc
from Strategies.Simple_Strategies import MACD as macd
from Strategies.Simple_Strategies import RSI as rsi
from Strategies.Simple_Strategies import bollinger as bl

from Strategies.Combined_Strategies import rsi_bollinger as rb

import backtrader as bt


if __name__ == '__main__':
    
    # Create a Cerebro entity
    cerebro = bt.Cerebro()
    
    datapath_orcl = os.path.join(r".\\Data\\orcl-1995-2014.txt")
    datapath_nvda = os.path.join(r".\\Data\\nvda-1999-2014.txt")
    datapath_yhoo = os.path.join(r".\\Data\\yhoo-1996-2015.txt")
    
     # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath_orcl,
    reverse=False)
    # Add the Data Feed to Cerebro
    cerebro.adddata(data)
    cerebro.addstrategy(rb.ris_bollinger)
    cerebro.broker.setcommission(commission=0.001)
    cerebro.broker.setcash(100000.0)
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    '''
    mostrar porcentaje de ganancia o perdida
    if (100000.0 > cerebro.broker.getvalue()):
        print(f"Loss: {cerebro.broker.getvalue()/100000.0}")
    else: 
        print(f"profit: {100000.0/cerebro.broker.getvalue()}")
    '''
    cerebro.plot()