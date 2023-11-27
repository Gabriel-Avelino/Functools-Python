from functools import partialmethod

class Numero:


    def mul(self, n1, n2):
        return n1 * n2

    dobro = partialmethod(mul, n2 = 2)

n = Numero()
print(n.mul(3, 5))
print(n.dobro(3))