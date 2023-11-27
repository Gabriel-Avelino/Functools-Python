from functools import partial


def mul(n1, n2):
    return n1 * n2


dobro = partial(mul, n2 = 2)
triplo = partial(mul, n2 = 3)

print(mul(1, 2))
print(dobro(2))
print(triplo(3))