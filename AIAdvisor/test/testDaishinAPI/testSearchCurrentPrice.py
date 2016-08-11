#-*- coding: euc-kr -*-
'''
Created on 2016. 8. 8.

@author: taehe
'''

import win32com.client
inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
inStockMst.SetInputValue(0, "A000660")    # 삼성전자 주식이라는 정보를 입력 
inStockMst.BlockRequest()                    # 삼성전자에 대한 데이터 확인 요청 
dd = inStockMst.GetHeaderValue(1)   
print(dd)