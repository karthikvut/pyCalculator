"""Scientific operations"""

import math

num1 = int(input('Enter your first number: '))

#Log
print('log {0}'.format(num1))
print(math.log(num1,10))

#Natural logarithm
print('log e {0}'.format(num1))
print(math.log(num1,math.e))

#Square Root
print('sqrt{0}'.format(num1))
print(math.sqrt(num1))

#Sin
print('sin({0})'.format(num1))
print(math.sin(num1))

#Cosine
print('cos({0})'.format(num1))
print(math.cos(num1))

#Tan
print('tan({0})'.format(num1))
print(math.tan(num1))