#Chapter 8_Programming Project #1 - Data mining stock prices
'''Program will calculate the monthly average prices of Amazon stock for a year
and tell us the best six months and the worse six months'''

#Entry message
#getMonthlyAverages function
#printInfo function


def getDataList(fileName):
    with open(fileName, 'r') as dataFile:
        dataList = []
        count = 0
        for lineStr in dataFile:
            dataList.append(lineStr.strip().split(','))
            #if lineStr == '\n':
                #pass
            #else:
                #dataList.append(lineStr.strip().split(','))
        return dataList

dataList = getDataList('AMZN(1).csv')


count = 1
volume_int = 0
close_float = 0
date = ""
ave_price_num = 0
ave_price_den = 0
ave_price = 0

for i in dataList:
    date = dataList[count][0]
    volume_int = int(dataList[count][6])
    close_float = float(dataList[count][5])
    ave_price_num += volume_int * close_float
    ave_price_den += volume_int
    print("Volume " + str(volume_int))
    print("close price " + str(close_float))
    print("Ave price Numerator " + str(ave_price_num))
    print("Ave price den " + str(ave_price_den))
    print("-----------------" * 2)
    count += 1
    if count > 22:
        ave_price = ave_price_num/ave_price_den
        print("average price " + str(ave_price))
        print("Average price for June 2018 is : " + str(ave_price))
        break
 
          
'''for i in dataList:
    for j in i:
        dataList[i][j] for i, j in dataList if i...'''
            
