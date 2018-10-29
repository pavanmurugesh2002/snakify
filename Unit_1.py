print(36/7)

print('Hi', input())# hi john

a=int(input()) # squares
print(a*a)

a = int(input()) #area or a right triangle
b= int(input())

print(a*b/2)


name = input()# hello harry

# Print the result using:
# print('Greeting', name)
Greeting = 'Hello,'

print(Greeting , name + '!')

n = int(input()) # apple sharing
k = int(input())

# Print the result with print()

# Example of division, integer division and remainder:
print(k // n)

print(k % n)


a = int(input())# previous and next

print("The next number for the number",a, "is",a+1,)
print("The previous number for the number",a, "is",a-1,)


a = float(input()) #two timestamps
b = float(input())
c = float(input())
a1 = float(input())
b1 = float(input())
c1 = float(input())


print(-((a*3600 + b*60 + c) - (a1*3600 + b1*60 + c1)) )

a = int(input())#school desks
b = int(input())
c = int(input())

print(a//2 + b//2 + c//2 + b%2 + c%2 + a%2 )


#Unit 2
a = int(input()) # last digit of an integer

b = a%10

print(b)


a = int(input()) #tens digit

b = ((a//10)%10)

print(b)


b = (a%10) # sum of digits
c = ((a//10)%10)
d = ((a//100)%10)

print(b + c + d)


a = float(input())# fractional parts
print(a%1)


b = float(input()) # first digit after decimal point
print(int((b/0.1)%10))


import math #Car Route

from math import ceil

N = int(input())

M = int(input())


N = int(input()) # Digital Clock

a = (N//60)

b = (N%60)

print( a , b)


A = int(input()) #total cost
B = int(input())

N = int(input())

x = A*100
t = N*(x + B)
print(t//100, t%100)



import math #clockface 1

H = int(input())

M = int(input())

S = int(input())

x = (H*3600) + (M*60) + S
print(x*.008333333)


a = float(input()) # clockface 2 

x = a%30

print(x*12)







