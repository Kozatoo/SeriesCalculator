def fibonacci(n):
    if n < 0:
        raise ValueError("The given number must be positive")
    if n == 0:
        return 0
    if n > 92:
        raise ValueError("The given number is too big!")
    x = 0
    y = 1
    for i in range(n - 1):
        x, y = y, x + y
    return y


def square_numbers(n):
    return n * n


def arithmetic_sum(n):
    if n < 0:
        raise ValueError("The given number must be positive")
    return n * (n + 1) // 2


def pentagonal_series(n):
    if n == 0 :
        return 0
    if n < 1:
        raise ValueError("The given number must be greater than 1")
    return (n * n * 3 - n) // 2


def caterer_sequence(n):
    if n == 0:
        return 1
    if n < 1:
        raise ValueError("The given number must be greater than 1")
    return caterer_sequence(n - 1)+n
