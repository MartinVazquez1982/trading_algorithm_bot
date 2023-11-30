import datetime
import os.path
import sys

from Strategies.Simple_Strategies import crossMethod as cm
from Strategies.Simple_Strategies import goldenCross as gc
from Strategies.Simple_Strategies import deathCross as dc
from Strategies.Simple_Strategies import MACD as macd
from Strategies.Simple_Strategies import RSI as rsi
from Strategies.Simple_Strategies import bollinger as bl

from Strategies.Combined_Strategies import strategy_1 as s1
from Strategies.Combined_Strategies import strategy_2 as s2

import backtrader as bt

def ret_cerebro(data, strategy):
    cerebro = bt.Cerebro()
    cerebro.adddata(data)
    cerebro.addstrategy(strategy)
    cerebro.broker.setcommission(commission=0.001)
    cerebro.broker.setcash(100000.0)
    return cerebro


if __name__ == '__main__':
    
    # Create a Cerebro entity
    cerebro = bt.Cerebro()
    
    datapath_orcl = os.path.join(r".\\Data\\orcl-1995-2014.txt")
    datapath_nvda = os.path.join(r".\\Data\\nvda-1999-2014.txt")
    datapath_yhoo = os.path.join(r".\\Data\\yhoo-1996-2015.txt")
    datapath_ko = os.path.join(r".\\Data\\KO.csv")
    datapath_bma = os.path.join(r".\\Data\\BMA.csv")
     # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath_nvda,
    reverse=False)
    # Add the Data Feed to Cerebro
    cerebro1 = ret_cerebro(data, s1.Strategy1)
    cerebro2 = ret_cerebro(data, s2.Strategy2)
    print(f"Starting Portfolio Value - Strategy 1: {cerebro1.broker.getvalue()} Strategy 2: {cerebro2.broker.getvalue()}")
    print("\n================= Strategy 1 ================= \n")
    cerebro1.run()
    print("============================================== \n")
    print("================= Strategy 2 ================= \n")
    cerebro2.run()
    print("============================================== \n")
    print('Final Portfolio Value - Strategy 1: %.2f | Strategy 2: %.2f' % (cerebro1.broker.getvalue(),cerebro2.broker.getvalue()))
    #cerebro1.plot()