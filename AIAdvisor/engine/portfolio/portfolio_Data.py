'''
Created on 2016. 4. 21.

@author: thCho
'''

class portfolio_data():
    
    def __init__(self, budget, accumulatedPnL, assets, currentWeights):
        self.budget = budget
        self.accumulatedPnL = accumulatedPnL
        self.assets
        self.currentWeights = currentWeights
        
    def getBudget(self):
        return self.budget
    
    def getAccumulatedPnL(self):
        return self.accumulatedPnL
    
    def getCurrentWeights(self):
        return self.currentWeights
    
    def setBudget(self, budget):
        self.budget = budget
        
    def setAccumulatePnL(self, pnl):
        self.accumulatedPnL = pnl
    
    def setAssets(self, assets):
        self.assets = assets
        
    def setWeights(self, weights):
        self.currentWeights = weights