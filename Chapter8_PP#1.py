#Chapter 8_Programming Project #1 - Data mining stock prices
'''Program will calculate the monthly average prices of Amazon stock for a year
and tell us the best six months and the worse six months'''

#Entry message
#getMonthlyAverages function
#printInfo function

avePrice = 0
avePriceNum = 0
avePriceDen = 0
def getDataList(fileName):
    with open(fileName, 'r') as dataFile:
        dataList = []
        count = 0
        for lineStr in dataFile:
            if lineStr == '\n':
                pass
            else:
                dataList.append(lineStr.strip().split(','))
        return dataList

dataList = getDataList('AMZN.csv')

count = 0
multiCloseVol = 0
totalMVC = 0
for i in dataList:
    multiCloseVol = float(dataList[count][5]) * float(dataList[count][6])
    print("Multi Close #1 " + str(multiCloseVol))
    totalMCV = multiCloseVol + multiCloseVol
    print("total MCV " + str(totalMCV))
    count+=1
    #Out of range due to count
          
'''for i in dataList:
    for j in i:
        dataList[i][j] for i, j in dataList if i...'''
            
