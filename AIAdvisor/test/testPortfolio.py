'''
Created on 2016. 4. 21.

@author: thCho
'''
from common.time.Date import Date
from engine.portfolio.portfolio import portfolio


startDate = '20150101'
endDate = '20160101'
period = [startDate, endDate]
strategy = 0
pfo = portfolio(100, strategy)
pfo.backTest(period)