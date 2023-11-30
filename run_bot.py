import os.path
import sys

from Strategies.Main_Strategies import strategy_final as sf

import backtrader as bt

def ret_cerebro(data, strategy, comm=0.001, cash_init=100000.0):
    
    '''create a cerebro'''
    
    cerebro = bt.Cerebro()
    cerebro.adddata(data)
    cerebro.addstrategy(strategy)
    cerebro.broker.setcommission(commission=comm)
    cerebro.broker.setcash(cash_init)
    return cerebro


if __name__ == '__main__':
    
    datapath = None
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "ORCL":
            datapath = os.path.join(r".\\Data\\orcl-1995-2014.txt")
        elif sys.argv[1] == "NVDA":
            datapath = os.path.join(r".\\Data\\nvda-1999-2014.txt")
        elif sys.argv[1] == "YHOO":
            datapath = os.path.join(r".\\Data\\yhoo-1996-2015.txt")
        elif sys.argv[1] == "KO":
            datapath = os.path.join(r".\\Data\\KO.csv")
        elif sys.argv[1] == "BMA":
            datapath = os.path.join(r".\\Data\\BMA.csv")
        else:
            raise ValueError("Datafeed inexistente")
    else:
        datapath = os.path.join(r".\\Data\\orcl-1995-2014.txt")
        print("\nUtiliza el datafeed ORCL")
        print("Si desea ultilizar otro, ingreselo por argumento: ")
        print("ORCL - NVDA - YHOO - KO - BMA")
    
    # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    reverse=False)
    
    # create a cerebro
    cerebro = ret_cerebro(data, sf.Strategy_General)
    
    # start execute
    print(f"\nStarting Portfolio Value: {cerebro.broker.getvalue()}")
    print("\n================= Strategy  ================= \n")
    cerebro.run()
    print("============================================== \n")
    print('Final Portfolio Value: %.2f' % (cerebro.broker.getvalue()))
    cerebro.plot()