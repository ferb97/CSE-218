import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def f(x):
    return x**3 - 0.18 * (x**2) + 0.0004752

xlist = np.linspace(0, 0.12, num = 1000)
ylist = f(xlist)

plt.plot(xlist, ylist, 'r')

plt.title('Plotting Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.grid()
plt.show()

def bisection(lower, upper, approximationError, maxIteration):
    iteration = 0
    error = 100.0
    mid = (lower + upper) / 2.0
    prevMid = lower
    while(iteration < maxIteration):
        iteration += 1
        mid = (lower + upper) / 2.0
        error = np.abs(((mid - prevMid) / mid) * 100.0)
        if error <= approximationError and iteration > 1:
            return mid
        elif f(lower) * f(mid) < 0:
            upper = mid
        elif f(lower) * f(mid) > 0:
            lower = mid
        prevMid = mid;
    return mid

lower = float(input('Enter lower bound: '))
upper = float(input('Enter upper bound: '))
approximationError = 0.5
maxIteration = 20

print(bisection(lower, upper, approximationError, maxIteration))

def bisectionErrorTable(lower, upper, maxIteration):
    iteration = 0
    error = 100.0
    mid = (lower + upper) / 2.0
    prevMid = 0
    list = []
    while(iteration < maxIteration):
        iteration += 1
        mid = (lower + upper) / 2.0
        error = np.abs(((mid - prevMid) / mid) * 100.0)
        new = [iteration, lower, upper, mid, error]
        list.append(new)
        if f(lower) * f(mid) < 0:
            upper = mid
        elif f(lower) * f(mid) > 0:
            lower = mid
        prevMid = mid;

    return list

print(tabulate(bisectionErrorTable(lower, upper, maxIteration), headers = ['Iteration', 'Lower', 'Upper', 'Mid', 'Error']))











