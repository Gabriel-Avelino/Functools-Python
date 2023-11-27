from functools import singledispatchmethod

class NeuralNetwork:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError('Não foi implementada')


    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg


x = NeuralNetwork()

print(x.neg(False))
