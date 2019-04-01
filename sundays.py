# Start at 1/1/1901 (Tuesday)

countOfSundays = 0;
year = 1901
dayOfWeek = 2

def month(startingDayOfWeek):
	if startingDayOfWeek == 0:
		return 1
	return 0

def weekDay(dayOfWeek):
	return dayOfWeek % 7

def addDayforLeapYear(year):
	if year%4 == 0 :
		return 1
	return 0

while year < 2001:
	# Jan
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 31)
	# print(dayOfWeek)
	# Feb
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 28 + addDayforLeapYear(year))
	# print(dayOfWeek)
	# March
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 31)
	# print(dayOfWeek)
	# April
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 30)
	# print(dayOfWeek)
	# May
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 31)
	# print(dayOfWeek)
	# June
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 30)
	# print(dayOfWeek)
	# July
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 31)
	# print(dayOfWeek)
	# Aug
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 31)
	# print(dayOfWeek)
	#Sept
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 30)
	# print(dayOfWeek)
	# Oct
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 31)
	# print(dayOfWeek)
	# Nov
	countOfSundays = countOfSundays + month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 30)
	# print(dayOfWeek)
	# Dec
	countOfSundays = countOfSundays +  month(dayOfWeek)
	dayOfWeek = weekDay(dayOfWeek + 31)
	# print(dayOfWeek)

	year = year + 1

print("Sunday " , countOfSundays)
