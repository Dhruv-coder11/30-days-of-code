totalMilesToDrive = 2052
totalDays = 6
townToStopPerDay = 2
kmPerMile = 1.60934

avgMiles = (totalMilesToDrive/totalDays)/townToStopPerDay

# coversion miles to km

avgKM = avgMiles*kmPerMile

print("She drive average of", avgKM, "km between every stop")