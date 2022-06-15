#Quadratic Equation

from math import sqrt as sqroot 

def solve_linear (b, c): # defining the linear solutions for when there is no 'a' inputted
  x = -c /(1.0 * b)
  print ("x= {} Equation is Linear!".format(x))

def solve_quad(a, b, c): # if negatives are involved sending the inputs to solve_complex otherwise sent to solve_real to be handled accordingly. 
  if b*b - (4 * a * c) < 0:
    solve_complex(a, b, c)
  else:
    solve_real(a, b, c)

def solve_real(a, b, c): #after recieving the numbers performs equation and prints 'real' answers
  x1 = (-b + sqroot(b*b -4*a*c))/(2*a)
  x2 = (-b - sqroot(b*b -4*a*c))/(2*a)
  print ("x= {}, {} Equation is Real!".format(x1, x2))

def solve_complex(a, b, c): #this portion uses the absolute to convert the negative into positive to be able to complete the equation and the print 'i' with the answer
  x_real = -b /(2*a)
  x_imag = sqroot(abs((b*b - 4*a*c)/(2*a)))
  print ("x= {} + {}i".format(x_real,x_imag))
  print ("x= {} - {}i".format(x_real,x_imag))


#Main 
a = int(input("Coefficient for A: "))
b = int(input("Coefficient for B: "))
c = int(input("Coefficient for C: "))

if a is 0: 				#this portions controls which calls are made depending on the numbers provided.
  if b is 0:
   print("Degenerate Equation, Try Again!")
  else:
    solve_linear(b,c)
else:
  solve_quad(a, b, c)