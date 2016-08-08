'''
Created on 2016. 8. 8.

@author: Jay
'''
import win32com.client
from engine.stockPicker.CybosPlus.StockMst import StockMstClass


def CheckVolumn(instStockMst, code):
    # SetInputValue
    instStockMst.SetInputValue(0, code)
    
    # BlockRequest
    instStockMst.BlockRequest()

    # GetData
    stockCode = instStockMst.GetHeaderValue(0)
    stockName = instStockMst.GetHeaderValue(1)
    currPrice = instStockMst.GetHeaderValue(11)
    
    print (stockCode, stockName, currPrice)
    
if __name__ == "__main__":
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    
    codeList = instCpCodeMgr.GetStockListByMarket(1)
    stockMstClass = StockMstClass() 
    for code in codeList:
        stockMstClass.setInputValue(StockMstClass.InputType.StockCode, code)
        stockCode = stockMstClass.getResult(StockMstClass.OutputType.StockCode)
        currPrice = stockMstClass.getResult(StockMstClass.OutputType.HighestPrice52wk)
        print (stockCode, currPrice)