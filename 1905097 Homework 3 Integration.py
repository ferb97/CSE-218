import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (6.73 * x + 6.725 * (10 ** -8) + 7.26 * (10 ** -4) * C) / (3.62 * (10 ** -12) * x + 3.908 * (10 ** -8) * x * C)


def trapezoid_rule_integration(a, b, n):

    ans = (b - a) / (2 * n)

    temp = f(a) + f(b)
    for i in range(1, n):
        d = a + i * (b-a) / n
        temp = temp + 2 * f(d)

    ans = ans * temp
    return ans


def simpsons_rule_integration(a, b, n):

    ans = (b - a) / (6 * n)

    temp = f(a) + f(b)
    for i in range(1, 2 * n, 2):
        d = a + i * (b-a) / (2 * n)
        temp = temp + 4 * f(d)

    for i in range(2, 2 * n, 2):
        d = a + i * (b-a) / (2 * n)
        temp = temp + 2 * f(d)

    ans = ans * temp
    return ans


def print_trapezoid_rule_integration(a, b):

    ans = [0.0]
    for i in range(1, 6):
        ans.append(trapezoid_rule_integration(a, b, i))

    print('Trapezoid Rule Integration:')
    for i in range(1, 6):
        error = (np.abs(ans[i] - ans[i - 1]) / ans[i]) * 100
        if i == 1:
            print('For n =', i, ' --> The Calculated Value = ', ans[i], '\t The Absolute Relative Approximate Error =  N/A')
        else:
            print('For n =', i, ' --> The Calculated Value = ', ans[i], '\t The Absolute Relative Approximate Error = ', error)


def print_simpsons_rule_integration(a, b):

    ans = [0.0]
    for i in range(1, 6):
        ans.append(simpsons_rule_integration(a, b, i))

    print('Simpsons Rule Integration:')
    for i in range(1, 6):
        error = (np.abs(ans[i] - ans[i - 1]) / ans[i]) * 100
        if i == 1:
            print('For n =', i, ' --> The Calculated Value = ', ans[i], '\t The Absolute Relative Approximate Error =  N/A')
        else:
            print('For n =', i, ' --> The Calculated Value = ', ans[i], '\t The Absolute Relative Approximate Error = ', error)


C = 5 * (10 ** -4)
n = int(input('Enter sub intervals: '))
b = 1.22 * (10 ** -4)
a = 0.5 * b
print()


trapezoid_ans = trapezoid_rule_integration(a, b, n)
print('The time for trapezoid rule integration using', n, 'sub-intervals:', trapezoid_ans)
print_trapezoid_rule_integration(a, b)
print()


simpsons_ans = simpsons_rule_integration(a, b, n)
print('The time for simpsons rule integration using', 2 * n, 'sub-intervals:', simpsons_ans)
print_simpsons_rule_integration(a, b)
print()


x = [1.22 * (10 ** -4), 1.20 * (10 ** -4), 1.0 * (10 ** -4), 0.8 * (10 ** -4), 0.6 * (10 ** -4), 0.4 * (10 ** -4), 0.2 * (10 ** -4)]

T = []
for i in range(7):
    print('The value of T for x = ', x[i], ' --> ', simpsons_rule_integration(x[i], b, 5))
    T.append(simpsons_rule_integration(x[i], b, 5))


plt.plot(x, T, 'r')
plt.plot(x, T, 'b*')

plt.title('Plotting Graph of x vs T')
plt.xlabel('x')
plt.ylabel('T')

plt.grid()
plt.show()
