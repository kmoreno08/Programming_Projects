 #Chapter 8_Programming Project #1 - Data mining stock prices
'''Program will calculate the monthly average prices of Amazon stock for a year
and tell us the best six months and the worse six months'''

#Entry message
#getMonthlyAverages function
#printInfo function
#DRY code

#Open file and read
def getDataList(fileName):
    with open(fileName, 'r') as dataFile:
        dataList = []
        count = 0
        for lineStr in dataFile:
            dataList.append(lineStr.strip().split(','))
        return dataList
#Sort tuple by second element
def sort_second(val):
    return val[1]

dataList = getDataList('AMZN.csv')



count = 1
volume_int = 0
close_float = 0
date = ""
ave_price_num = 0
ave_price_den = 0
ave_price = 0
month_list = []

for i in dataList:
    date = dataList[count][0]
    volume_int = int(dataList[count][6])
    close_float = float(dataList[count][5])
    ave_price_num += volume_int * close_float
    ave_price_den += volume_int
    count += 1
    
    #June/18
    if count == 22:
        ave_price = ave_price_num/ave_price_den
        tuple_june = ("06/2018", ave_price)
        month_list.append(tuple_june)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #July/18
    elif count == 43:
        ave_price = ave_price_num/ave_price_den 
        tuple_july = ("07/2018", ave_price)
        month_list.append(tuple_july)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0 
    #August/18
    elif count == 66:
        ave_price = ave_price_num/ave_price_den 
        tuple_aug = ("08/2018", ave_price)
        month_list.append(tuple_aug)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0 
    #September/18
    elif count == 85:
        ave_price = ave_price_num/ave_price_den 
        tuple_sep = ("09/2018", ave_price)
        month_list.append(tuple_sep)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #October/18
    elif count == 108:
        ave_price = ave_price_num/ave_price_den 
        tuple_oct = ("10/2018", ave_price)
        month_list.append(tuple_oct)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #November/18
    elif count == 129:
        ave_price = ave_price_num/ave_price_den 
        tuple_nov = ("11/2018", ave_price)
        month_list.append(tuple_nov)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #December/18
    elif count == 148:
        ave_price = ave_price_num/ave_price_den 
        tuple_dec = ("12/2018", ave_price)
        month_list.append(tuple_dec)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #Jan/19
    elif count == 169:
        ave_price = ave_price_num/ave_price_den 
        tuple_jan = ("01/2019", ave_price)
        month_list.append(tuple_jan)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #Feb/19
    elif count == 188:
        ave_price = ave_price_num/ave_price_den 
        tuple_feb = ("02/2019", ave_price)
        month_list.append(tuple_feb)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #March/19
    elif count == 209:
        ave_price = ave_price_num/ave_price_den 
        tuple_march = ("03/2019", ave_price)
        month_list.append(tuple_march)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #April/19
    elif count == 230:
        ave_price = ave_price_num/ave_price_den 
        tuple_april = ("04/2019", ave_price)
        month_list.append(tuple_april)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
    #May/19
    elif count == 252:
        ave_price = ave_price_num/ave_price_den 
        tuple_may = ("05/2019", ave_price)
        month_list.append(tuple_may)
        ave_price_num = 0
        ave_price_den = 0
        ave_price = 0
        close_float = 0
        volume_int = 0
        break

list_count = 0
tuple_count = 0
counter = 0

#Sort tuples to highest avg-price
month_list.sort(key = sort_second, reverse = True)
for i in month_list:
    if counter == 0:
            print("The top 6 months of average price are:")
            print(F'\n\t{i}')
            counter +=1
    elif counter == 6:
        counter = 0
        break
    else:
        print(F'\n\t{i}')
        counter += 1


#Sort tuples to lowest avg-price
month_list.sort(key = sort_second, reverse = False)
for i in month_list:
    if counter == 0:
        print("The bottom 6 months of average price are:")
        print(F'\n\t{i}')
        counter +=1
    elif counter == 6:
        break
    else:
        print(F'\n\t{i}')
        counter += 1
   
        
   
        
    
    
