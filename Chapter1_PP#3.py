'''
Write a program that willl prompt the user for a floating-point number that stands
for gallons of gasoline. You will reprint that value along with other information
about gasoline and gasoline usage:
- # of liters
- # of barrels of oil required to make this amount of gasoline
- Equivalent energy amount of ethanol gallons
- Price in U.S. dollars
Use these approximate values:
- 1 barrel of oil produces 19.5 gallons of gasoline
- 1 gallon of gasoline produces 20 pounds of CO2 gas when burned
- 1 gallon of gasoline contains 115,000 BTU of energy
- 1 gallon of ethanol contain 75,700 BTU of energy
- 1 gallon of gasoline costs $3.00 / gallone
'''
print("Welcome! This program will tell you the following: \n1) number of liters.")
print("2) number of barrels of oil required to make this amount of gasoline")
print("3) Equivalent energy amount of ethanol gallons.")
print("4) Price in U.S. dollars.")
      

#Oil conversions and calculations
numberOfGallons = float(input("How many gallons of gasoline? (Please enter here): "))

#Liters
numberOfLiters = numberOfGallons * 3.78541
print('The number of liters are %.2f liters' % numberOfLiters)

#Barrel of oil
numberOfBarrels = numberOfGallons / 19.5
print('The total number of Barrels of oil : %.2f barrels' % numberOfBarrels)

#Pounds of CO2
poundsOfC02 = numberOfGallons * 20
print("The total number of pounds of C02 : %.2f pounds" % poundsOfC02)

#BTU of energy
BTU = numberOfGallons * 115000
print("The total number of BTU of energy: %.2f BTU" % BTU)

#Ethanol gallons
gallonsOfEthanol = BTU / 75700
print("The total number of ethanol to produce the same BTU : %.2f gallons of ethanol" % gallonsOfEthanol)

#Cost
costOfGas = numberOfGallons * 3.00
print("The total cost is : $%.2f " % costOfGas)





