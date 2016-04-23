'''
Created on 2016. 4. 20.

@author: thCho
'''
from common.time.Date import Date
from AIMapper.models import StockData

startDate = Date.valueOf('20150101')
endDate = Date.valueOf('20160101')
tradingDates = StockData.objects.values('DT').distinct()
dd = [entry for entry in tradingDates]
print(dd)
