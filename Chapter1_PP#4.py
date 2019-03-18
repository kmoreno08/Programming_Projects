#Population Estimation
'''Birth every 7 seconds
   death every 13 seconds
   new immigrant every 35 seconds
Write a program that takes years as input (as an integer) and prints out an estimated population
(as an integer). Assume that the current population is 307,357,870, and assume that there are
exactly 365 days in a year '''


print("Welcome! This program will estimate population with a birth every 7 seconds, death every 13 seconds, and a new immigrant every 35 seconds in a country.")
print("This program will assume the current population is 307,357,870 and exactly 365 days in a year.")

birth  = 7
death = 13
immigrant = 35


years = int(input("How many years ? : "))

days = years*365


hours = days*24


minutes = hours*60


seconds = minutes*60


totalBirths = seconds/7
intTotalBirths = int(totalBirths)
print("The total number of births are : " + str(intTotalBirths))

totalDeaths = seconds/13
intTotalDeaths = int(totalDeaths)
print("The total number of deaths are : " + str(intTotalDeaths))

totalImmigrants = seconds/35
intTotalImmigrants = int(totalImmigrants)
print("The total number of New Immigrants are : " + str(intTotalImmigrants))
print("---" * 22)


startingPopulation = int(307357870)

newPopulation =  startingPopulation + totalBirths + totalImmigrants - totalDeaths
intNewPopulation = int(newPopulation)

popIncreased = intNewPopulation - startingPopulation

popIncreasedPrint = f'Over {years} years, the population had increased by {popIncreased}'
print(popIncreasedPrint)

newPopulationStatement = f'The total population is : {intNewPopulation}'
print(newPopulationStatement)
