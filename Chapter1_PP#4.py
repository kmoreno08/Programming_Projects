#Population Estimation
'''Birth every 7 seconds
   death every 13 seconds
   new immigrant every 35 seconds
Write a program that takes years as input (as an integer) and prints out an estimated population
(as an integer). Assume that the current population is 307,357,870, and assume that there are
exactly 365 days in a year '''

#Welcome print
#has to be ints
#Finish 

birth  = 7
death = 13
immigrant = 35


years = int(input("How many years ? : "))

days = years*365
print(days)

hours = days*24
print(hours)

minutes = hours*60
print(minutes)

seconds = minutes*60
print("The amount of total seconds are " + str(seconds))

totalBirths = seconds/7
print("The total number of births are : " + str(totalBirths))

totalDeaths = seconds/13
print("The total number of deaths are : " + str(totalDeaths))

totalImmigrants = seconds/35
print("The total number of New Immigrants are : " + str(totalImmigrants))

population = int(307357870)
print(population)

print("With the current population the totals are : ")
newPopulation =  population + totalBirths + totalImmigrants - totalDeaths
print("The total number of new population is : " + str(newPopulation))
