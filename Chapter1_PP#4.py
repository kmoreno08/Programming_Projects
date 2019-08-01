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

#Ask user for years
years = int(input("How many years ? : "))

#Calculate days
days = years*365

#Calculate hours
hours = days*24

#Calculate minutes
minutes = hours*60

#Calculate seconds
seconds = minutes*60

#Calculate total births
totalBirths = seconds/7
intTotalBirths = int(totalBirths)
print("The total number of births are : " + str(intTotalBirths))

#Calculate total deaths
totalDeaths = seconds/13
intTotalDeaths = int(totalDeaths)
print("The total number of deaths are : " + str(intTotalDeaths))

#Calculate total immigrants
totalImmigrants = seconds/35
intTotalImmigrants = int(totalImmigrants)
print("The total number of New Immigrants are : " + str(intTotalImmigrants))
print("---" * 22)


startingPopulation = int(307357870)

#New population
newPopulation =  startingPopulation + totalBirths + totalImmigrants - totalDeaths
intNewPopulation = int(newPopulation)

#How much population increased from starting population.
popIncreased = intNewPopulation - startingPopulation

#Print statement
popIncreasedPrint = f'Over {years} years, the population had increased by {popIncreased}'
print(popIncreasedPrint)

newPopulationStatement = f'The total population is : {intNewPopulation}'
print(newPopulationStatement)
