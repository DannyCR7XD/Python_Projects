#Lists.py

listX = [5, 10, 15, 20, 25]

listY = ['x', 'y', 'z']

listX.extend(listY)

print(listX)

print (listX.index('x'))

listX.insert(5, 'ABC')

listX.append(25)

print(listX[3:8])

if listX.count(25):
  j = listX.index(25)
  print(j)
else:
  print("Not Found!")  

for i in listX:
 print(i, end='\n')

 #Strings 

stringA = "hello"

stringB = "ecu"

#
if str.islower(stringB):
  stringC = str.capitalize(stringA)+ " " +str.upper(stringB)
  print(stringC)

stringX = "::username:password:UID:GID:Name+123456:homedir:shell:::"  

#
if ((stringX.count(":")) >= 6):
  z = stringX.strip(":")
  listX = [x.strip() for x in z.split (":")]
  print(listX)

#
idnum = ((listX[4]).split("+").pop(1))

#
if idnum.isdigit():
 print(idnum)

#
print(stringX.replace(":","|", 5))


# Equilateral triangle has three sides that are the same
# Scalene triangles have all sides with different lengths
# Isosceles traingles have two sides of same length

a = int(input("Length of side A: "))
b = int(input("Length of side B: "))
c = int(input("Length of side C: "))

if a != b and b != c and a != c:
  print("The triangle is Scalene")

elif a == b and b == c and a == c:
  print("This triangle is an Equilateral")

else:
  print("The makings of an Isosceles")

#Is provided number EVEN or ODD?
n = input("Provide a number: ")
num = int(n)

if num % 2 == 0:
  print("Number provided is EVEN")

else:
  print("Number was ODD")