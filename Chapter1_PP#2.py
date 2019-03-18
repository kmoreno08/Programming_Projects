#Where is Voyager 1?
'''
The Voyager 1 spacecraft, launched September 15, 1977, is the farthest traveling
Earth-made object. It is presently on the outer edges of our solar system. The
NASA updated page on September 25, 2009, reported it as being a distance of
approximately 16,637,000,000 miles from the sun, traveling at 38,241 miles/hour.
Write a program that will prompt the user for an integer number that indicates
the number of days after 9/25/09. You will calculate the distance the Voyager
from the sun using the numbers from 9/25/09 (assume that velocity is constant)
plus the entered number of days, and report:
-Distance in miles
-Distance in kilometers (1.609344 kilometers/mile)
-Distance in astronomical units (AU, 92,955,807.6 miles/AU)
-Round-trip time for radio communication in hours. Radio waves travel at the
speed of light, listed at 299,792,458 meters/second
'''

#Make sure they only put an interger number

print("Welcome!")
print("This program will calculate: how far the voyager is from the sun in miles, kilometers, AU, and round-trip time for radio communication.")
print("Please enter the number of days after September 25th, 2009 to find its distance ")
numDays = int(input("How many days have passed? "))


totalMilesPerDay = 38241 * 4
milesFromEarth = float(16637000000)

#Miles
totalMilesFromSun = numDays * totalMilesPerDay
totalMilesFromEarthToVoyager = totalMilesFromSun + milesFromEarth
print("The distance is %.2f miles." % totalMilesFromEarthToVoyager)

#Kilometers
kiloConv = totalMilesFromSun * 1.609344
kiloConvEarthToSun = milesFromEarth * 1.609344
totalKiloFromEarthToVoyager = kiloConvEarthToSun + kiloConv
print("The distance is %.2f kilometers." % totalKiloFromEarthToVoyager)

#Astronomical Units
AUConv = totalMilesFromSun / 92955807.6
AUConvEarthToSun = milesFromEarth / 92955807.6
totalAUFromEarthToVoyager = AUConvEarthToSun + AUConv
print("The distance is %.2f astronomical units" % totalAUFromEarthToVoyager)


#Round trip time in meters
metersConv = totalMilesFromSun * 1609.344

metersEarthToVoyager = metersConv + milesFromEarth
metersEarthToVoyagerAndBack = metersEarthToVoyager*2

speedOfLightPerSecondInMeters = float(299792458)
speedOfLightPerHourInMeters = speedOfLightPerSecondInMeters * 60


totalHoursRoundTripTime = metersEarthToVoyagerAndBack / speedOfLightPerHourInMeters
print("The round-trip time for radio communication to the voyager is %.2f hours." % totalHoursRoundTripTime)





