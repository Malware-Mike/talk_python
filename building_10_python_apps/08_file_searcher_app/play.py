# factorial
# 5 * 4 * 3 * 2 *1


def fact(n):
    if n <= 1:
        return 1

    return n * fact(n -1)

def f(n):

    if n <= 1:
        return 1
    count = n
    total = 1

    while count >= 1:
        total *= count
        count -= 1

    return total
