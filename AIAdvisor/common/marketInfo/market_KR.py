'''
Created on 2016. 4. 20.

@author: thCho
'''
from common.marketInfo.abstractMarket import AbstractMarket
from common.marketInfo.asset import Equity


class market_KR(AbstractMarket):
    
    def __init__(self, assetType):
        if 'EQUITY' == assetType.getEquityType():
            self.transactionFee = 0
        if 'ETF' == assetType.getEquityType():
            self.transactionFee = 0
        else :
            self.transactionFee = 0
        
        
        
    
    def getTaxInfo(self):
        return self.transactionFee
    
    
