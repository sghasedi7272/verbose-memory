# Sara Ghasedi
# MATH 4610 Project #1

import math


def f(lambda_0):
    return (2.5 / (7 + lambda_0)) ** 2 + (1.5 / (4 + lambda_0)) ** 2 + (0.1 / (0.3 + lambda_0)) ** 2 - 0.05


def f_prime(lambda_0):
    return -12.5 / (7 + lambda_0) ** 3 - 4.5 / (4 + lambda_0) ** 3 - .02 / (.3 + lambda_0) ** 3


def g(lambda_0):
    return lambda_0 + 100 * f(lambda_0)


def newton(lambda_0, epsilon, maxits):
    lambdas = []
    i = 1
    while i < maxits:
        p = lambda_0 - f(lambda_0) / f_prime(lambda_0)
        lambdas.append(p)
        if abs(p - lambda_0) < epsilon:
            print("Solution approximated using Newton's method after", i, "iterations.")
            print(lambdas)
            return lambdas
        i = i + 1
        lambda_0 = p
    print("No solution found after max iterations.")


def fixed(lambda_0, epsilon, maxits):
    lambdas = []
    i = 1
    while i < maxits:
        p = g(lambda_0)
        lambdas.append(p)
        if abs(p - lambda_0) < epsilon:
            print("Solution approximated using fixed point method after", i, "iterations.")
            print(lambdas)
            return lambdas
        i = i + 1
        lambda_0 = p
    print("No solution found after max iterations.")


def table(lambdas):
    if lambdas is None:
        return lambdas
    ratios = []
    x = 0
    p = lambdas[-1]
    while lambdas[x + 2] != p:
        numerator = math.log(abs(lambdas[x + 2] - p) / abs(lambdas[x + 1] - p))
        denominator = math.log(abs(lambdas[x + 1] - p) / abs(lambdas[x] - p))
        ratios.append(numerator / denominator)
        x = x + 1
    return ratios


def main():
    lambda_0 = 10
    epsilon = 10e-12
    maxits = 25
    newton_m = newton(lambda_0, epsilon, maxits)
    fixed_m = fixed(lambda_0, epsilon, maxits)

    print()
    print("Ratios for Newton's method:", table(newton_m))
    print("Ratios for fixed point method:", table(fixed_m))


main()
