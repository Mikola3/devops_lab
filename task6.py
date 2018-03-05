#!/usr/bin/python
a = int(input("Input a: "))
b = int(input("Input b: "))

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

nod = a + b
print("nod is:",nod)
