#!/usr/bin/python
N = 3
print ("Input matrix 3x3")

matrix = [ list(map(int, input().split())) for i in range(N)]

sumMain = 0
sumSecondary = 0
dif = 0 
for i in range(N):
    sumMain += matrix[i][i]
    sumSecondary += matrix[i][N-i-1]
dif = sumMain - sumSecondary

print(sumMain)
print(sumSecondary)
print(dif)