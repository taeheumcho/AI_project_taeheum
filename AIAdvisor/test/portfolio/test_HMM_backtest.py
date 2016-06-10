'''
Created on 2016. 6. 9.

@author: thCho
'''
from engine.portfolio.strategy.Strategy_HMM import Strategy_HMM
from engine.portfolio.portfolio_Data import portfolio_data
from AIMapper.models import StockData
from engine.portfolio.portfolio_Backtest import portfolio

startDate = '20100820'
teststartdate = '20150330'
testendDate = '20160331'
period = [teststartdate, testendDate]
assetCodes = ['KR7005930003','KR7008770000']
tradingDatesss = StockData.objects.values('dt').distinct()
'strategy setting'
hmmStrategy = Strategy_HMM(assetCodes, startDate)
'PORTFOLIO SETTING'
currentPrice = StockData.objects.filter(dt=teststartdate,ticker=assetCodes[0]).values("price_close")
currentPrice2 = StockData.objects.filter(dt=teststartdate,ticker=assetCodes[1]).values("price_close")

pfo_data = portfolio_data(startDate, 0, assetCodes, [1.0,currentPrice[0]['price_close'],currentPrice2[0]['price_close']], [1000000.0,0.0,0.0])
PFO = portfolio(pfo_data,hmmStrategy)
PFO.backTest(period)

print PFO.get_weight_array()
print PFO.get_day_PnL()
print PFO.get_current_weight()
print PFO.get_accumulated_PnL()

