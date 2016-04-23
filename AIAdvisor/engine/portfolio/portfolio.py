'''
Created on 2016. 4. 20.

@author: thCho
'''
from AIMapper.models import StockData

class portfolio(object):
    def __init__(self, portfolio_data, strategy):
        self.positions = {}
        self.strategy = strategy
        self.weight_array = [portfolio_data.getCurrentWeights()]
        self.pnl = [portfolio_data.getAccumulatedPnL()]
        self.balanceAmount = portfolio_data.getBudget()
        self.tradingDates = StockData.objects.values('DT').distinct()
    
    def backTest(self, testPeriod):
        weight_at_time = []
        weight_timearray = [[]]
        testDates = []
        for elements in self.tradingDates:
            if elements.get('DT') >= testPeriod[0] and elements.get('DT') <= testPeriod[1] :
                testDates.append(elements)
            
        self.strategy.calculate_weights()
        
    
        
        
    