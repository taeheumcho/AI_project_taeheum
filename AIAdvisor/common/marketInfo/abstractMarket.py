'''
Created on 2016. 4. 20.

@author: thCho
'''
from abc import ABCMeta, abstractmethod


class AbstractMarket(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def getTaxInfo(self):
        pass
