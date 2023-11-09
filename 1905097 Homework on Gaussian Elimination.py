import numpy as np
import sys

n = int(input())

A = np.zeros((n, n))

B = np.zeros(n)

print()
for i in range(n):
    A[i] = list(map(float,input().split()))


print()
for i in range(n):
    B[i] = float(input())

def GaussianElimination(A, B, pivot = True, showall = True):
    for i in range(n):

        if A[i][i] == 0.0 and pivot == False:
            sys.exit('Division by zero detected')

        if pivot == True:
            mx = A[i][i]
            pos = i
            for j in range(i+1, n):
                if np.abs(A[j][i]) > mx:
                    mx = np.abs(A[j][i])
                    pos = j

            A[[i, pos]] = A[[pos, i]]
            B[i], B[pos] = B[pos], B[i]

        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]

            for k in range(i, n):
                A[j][k] = A[j][k] - ratio * A[i][k]

            B[j] = B[j] - ratio * B[i]

            if showall == True:
                print()
                print("A Matrix:")
                for k in range(n):
                    for l in range(n):
                        print('%0.4f' %A[k][l], end ='  ')
                    print()

                print()
                print("B Matrix:")
                for k in range(n):
                    print('%0.4f' %B[k])

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = B[i]

        for j in range(i+1, n):
            x[i] = x[i] - x[j] * A[i][j]

        x[i] = x[i] / A[i][i]

    return x


x = GaussianElimination(A, B)

print()
print("Solution:")
for i in range(n):
    print('%0.4f' %x[i])