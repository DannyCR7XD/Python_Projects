#root table

import math

start = int(input("Provide Start Value: "))
stop = int(input("Provide Stop Value: "))
step = int(input("Provide the Step Value :"))

if (start <= stop and step > 0):
	for i in range(start, stop+1, step):
		if i < 0: 
			print (i, math.sqrt(abs(i)),"i")
		else:
			print(i, math.sqrt(i)) 
elif (start >= stop and step < 0):
	for j in range(start, stop+1, step):
		if j < 0:
			print(j, math.sqrt(abs(j)),"i")
		else:
			print(j, math.sqrt(j))


else:
	print("Either one or more Values provided do not create a valid loop!!")