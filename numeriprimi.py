result = []
lastPrimeNumber = 1
maxValue = 100

for candidate in range(2, maxValue + 1):
	isDivisible = False
	for lowerPrimeNumber in result:
		if candidate % lowerPrimeNumber == 0:
			isDivisible = True
			break
	if not isDivisible:
		result.append(candidate)

print(result)