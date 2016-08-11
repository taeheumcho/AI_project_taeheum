#-*- coding: euc-kr -*-
'''
Created on 2016. 8. 8.

@author: taehe
'''
import win32com.client
inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
inStockChart.SetInputValue(0, "A003540")        # ������� �ڵ�
inStockChart.SetInputValue(1, '2')
inStockChart.SetInputValue(4, 60)
inStockChart.SetInputValue(5, 8)
inStockChart.SetInputValue(6, ord('D'))
inStockChart.SetInputValue(9, '1')
inStockChart.BlockRequest()
data = []
num = inStockChart.GetHeaderValue(3)
for i in range(num):                            # 60���� �����Ϳ� ���ؼ� for ���� ������. 
    volumn = inStockChart.GetDataValue(0,i)     # 0�� ���� 59������ �����͸� �ϳ��� �����´�. (�ŷ���)
    data.append(volumn)
    print(data[i])       
    
avg = (sum(data) - data[0]) / (len(data) - 1)
print(avg)

if data[0] > (avg * 10):
    print("oh oh daebak")
elif data[0] > (avg * 8):
    print("oh something will happen")
else:
    print("damn")
    