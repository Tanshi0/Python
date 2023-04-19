'''def func(x):
    return x**3 + x**2 - 3

def bisection(a, b, accuracy):
    if func(a) * func(b) > 0:
        print("condition not met")

    c = a
    while (b-a) >= accuracy:
        c = (a+b)/2
        if func(c) == 0.0:
            return c
        elif func(c)*func(a) < 0:
            b = c
        else:
            a = c
    return c

a = -10
b = 10
accuracy = 0.00001

result = bisection(a, b, accuracy)

if result is None:
    print("No root found.")
else:
    print("Root =", result)'''

'''def func(x):
    return x**3 + x**2 - 3
 
def bisection(a,b):
    if (func(a) * func(b) >= 0):
        print("Условие не выполняется, тк функция имеет одинаковый знак на концах интервала!")
        return 0
    c = a
    while ((b-a) >= 0.01):
        c = (a+b)/2
        if (func(c) == 0.0):
            break
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
    print("Корень находится в точке:", "%.4f" % c)
 
a = 20
b = 30
bisection(a, b)'''

def func(x):
    return x**2 - 4*x + 3
 
def bisection(a,b):
    if (func(a) * func(b) >= 0):
        print("Условие на сходимость не выполняется, тк функция имеет одинаковый знак на концах интервала!")
        return
    x = a
    while ((b-a) >= 0.0001):
        x = (a+b)/2
        if (func(x) == 0.0):
            break
        if (func(x)*func(a) < 0):
            b = x
        else:
            a = x
    print("Корень находится в точке:", "%.4f" % x)
 
a = float(input("Введите начало интервала: "))
b = float(input("Введите конец интервала: "))
bisection(a, b)