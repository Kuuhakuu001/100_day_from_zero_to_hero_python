def find_squared_root(a):
    """Find the squared root of number a"""
    EPSILON = 0.001
    x_n = a
    while True:
        x_n1 = 0.5 * (x_n + a / x_n)
        if abs(x_n1 - x_n) < EPSILON:
            return x_n1
        x_n = x_n1


print(find_squared_root(2))
print(find_squared_root(3))

