'''
Created on 2016. 6. 15.

@author: thCho
'''
from engine.stockPicker.tools.AbstractTools import AbstractTools
from AIMapper.models import StockData

class Tools_RNN(AbstractTools):
    def __int__(self, assetCode, train_assets, train_startDate):
        self.asset_code = assetCode
        self.train_asset_codes = train_assets
        self.historical_Data = {}
        self.weight = []
        self.stacked = False
        self.tradingDates = StockData.objects.values('dt').distinct()
        self.trainingDates = []
    
    def getAssetPoint(self):
        
        return AbstractTools.getAssetPoint(self)
        