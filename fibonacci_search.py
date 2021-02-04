import math

def f(x):
    return x**2


def fibonacci_search(func, a, b, n, eps):
    s = (1 - math.sqrt(5)) / (1 + math.sqrt(5))
    phi = (1 + math.sqrt(5)) / 2
    ro = 1 / (phi * (1 - s ** (n + 1)) / (1 - s ** n))
    d = ro * b + (1 - ro) * a
    print(d)
    yd = func(d)

    for i in range(1, n):
        if i == n - 1:
            c = eps * a + (1 - eps) * d
        else:
            c = ro * a + (1 - ro) * b

        yc = f(c)

        if yc < yd:
            b, d, yd = d, c, yc
        else:
            a, b = b, c

        ro = 1 / (phi * (1 - s ** (n - i + 1)) / 1 - s ** (n - i))

    if a < b:
        return (a, b)
    return (b, a)


print(fibonacci_search(f, -10, 10, 20, 0.01))

def f_new(x):
    return 0.5 * x**3 - 2*x**2 + x - 1


print(fibonacci_search(f_new, 0, 4, 50, 0.0001))

print(f_new(2.472))
