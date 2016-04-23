'''
Created on 2016. 4. 20.

@author: thCho
'''
from engine.strategy.AbstractStrategy import AbstractStrategy
from abc import abstractmethod

class Strategy_FamaFrench(AbstractStrategy):
    def __init__(self):
        self.weight = []
    
   
    def calculate_weights(self):
        AbstractStrategy.calculate_weights(self)