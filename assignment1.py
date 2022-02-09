#!/bin/python3
import random
'''
#Question1:
#'Generate and print random numbers between 3 and 6'
a = random.randint(3,6)
print(a)
'''

'''
#Question2:
#"A program that generates a random number btw 1 and 50,x, a random number btw 2 and 5,y, computes as x^y"

x=random.randint(1,50)
y=random.randint(2,5)
print(x)
print(y)
sol=(x**y)
print(sol)

'''
'''
#Question3.
#"A program that generates a random number btw 1 & 10 and print your name that many times"

name = random.randint(1,10)
print(name)
for i in range(0, name):
    print("Overcomer")
'''
'''
#Question4.

#"A program that generates a random decimal number btw 1 & 10 with two decimal places of accuracy"

a=random.uniform(1,10)
ans= round(a, 2)
print(ans)
'''
'''
#Question5.
#"A program that generates 50 random numbers such that the first number is between
# 1 and 2, the second is between 1 and 3, third is between 1 and 4,...,and the last
# is between 1 and 51


y=[]
for i in range(1, 50):
    x=random.randint(1, 50)
    y.append(x)
y[0]=random.randint(1,2)
y[1]=random.randint(1,3)
y[2]=random.randint(1,4)
y[-1]=random.randint(1,51)
print(y)
print(f"the 1st number is {y[0]}")
print(f"the 2nd number is {y[1]}")
print(f"the 3rd number is {y[2]}")
print(f"the last number is {y[-1]}")
'''
'''
#Question6:
#"A program that ask user to enter two numbers, x & y, and computes x-y/x+y"

x=int(input(f"Enter value of x:"))
y=int(input(f"Enter value of y:"))
a=(x-y)
b=(x+y)
#print(a)
#print(b)
ans=(a/b)
print(ans)
'''
#Question7
#"

angle=int(input("Enter an angle btw -180 and 180 degrees: "))

if angle > 0:
   ans = angle % 360
else:
   ans = angle
print(f"The equivalent of {angle} degrees is {ans} degrees ")


