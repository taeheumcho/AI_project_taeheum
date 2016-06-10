'''
Created on 2016. 4. 20.

@author: thCho
'''
from AIMapper.models import StockData
from common.time.Date import Date


startDate = Date.valueOf('20150101')
endDate = Date.valueOf('20160101')
tradingDates = StockData.objects.values('dt').distinct()
dd = [entry for entry in tradingDates]
print(dd)
