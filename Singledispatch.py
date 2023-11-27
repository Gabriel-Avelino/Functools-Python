from functools import singledispatch

@singledispatch
def fun(arg):
    pass


@fun.register
def _ (arg: int):
    print('Fui chamada para um inteiro')


@fun.register
def _ (arg: str):
    print('Fui chamada para uma string')


fun('Hello World!')
