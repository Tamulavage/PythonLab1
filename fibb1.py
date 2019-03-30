i = 0
j = 1
evenNumbers = []
sum = 0

while sum<4000000:
	sum=i+j
	i=j
	j=sum
	if j%2==0:
		evenNumbers.append(j)

sumOfEven = 0
for x in evenNumbers:
	sumOfEven = sumOfEven+x

print( sumOfEven)	
