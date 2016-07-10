'''
Created on 2016. 6. 22.

@author: thCho
'''
# Time Series Testing 
from engine.stockPicker.tools.Tools_RNN import Tools_RNN
startDate = '20100820'
teststartdate = '20150330'
assetCodes = 'KR7005930003'

dd = Tools_RNN(assetCodes, startDate)

dd.getAssetPoint(teststartdate)
