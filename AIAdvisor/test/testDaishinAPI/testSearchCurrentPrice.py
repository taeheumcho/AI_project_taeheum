#-*- coding: euc-kr -*-
'''
Created on 2016. 8. 8.

@author: taehe
'''

import win32com.client
inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
inStockMst.SetInputValue(0, "A000660")    # �Ｚ���� �ֽ��̶�� ������ �Է� 
inStockMst.BlockRequest()                    # �Ｚ���ڿ� ���� ������ Ȯ�� ��û 
dd = inStockMst.GetHeaderValue(1)   
print(dd)