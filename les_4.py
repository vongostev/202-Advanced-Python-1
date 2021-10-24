import scipy.optimize as opt


def f(x):
    return x**2

print(opt.minimize(f, 10))
