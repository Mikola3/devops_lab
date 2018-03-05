#!/usr/bin/python

n = int(input("Input size of the numerical sequence: "))

for i in range(n):
    i+=1
    if i%15 == 0:
        print ("FizzBuzz")
    if i%3 == 0 and i%5 != 0:
        print ("Fizz")
    if i%5 == 0 and i%3 != 0:
        print ("Buzz")
    if i%3 != 0 and i%5 != 0:
        print (i)
