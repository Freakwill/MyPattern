# -*- coding: utf-8 -*-
"""
http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
 -written-in-python-the-sample-in-wikipedia
In most of other languages Strategy pattern is implemented via creating some
base strategy interface/abstract class and subclassing it with a number of
concrete strategies (as we can see at
http://en.wikipedia.org/wiki/Strategy_pattern), however Python supports
higher-order functions and allows us to have only one class and inject
functions into it's instances, as shown in this example.
"""

import types
import random


class BaseContext:
    # e.g. Algorithm calling strategies

    def __init__(self, func=None):
        if func is not None:
            self.select(func)

    def __call__(self, *args, **kwargs):
        self.execute(*args, **kwargs)

    def execute(self, *args, **kwargs):
        # to call self.execute(args) is to call strategy(obj, arguments)
        pass

    def select(self, func):
        # redefine a method
        # select a concrete strategy
        # func = fit (func)
        self.execute = types.MethodType(func, self)




class ContextExample(BaseContext):

    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.select(func)


    def execute(self, arg='nothing'):
        # original method
        print(arg)

    def make(self):
        self.select(execute_replacement1)

    def random(self):
        r = random.random()
        if r > 0.5:
            self.select(execute_replacement1)
        else:
            self.select(execute_replacement2)


def fit(f):
    def g(obj, *args, **kwargs):
        return f(*args, **kwargs)
    return g

# strategies
def execute_replacement1(obj, s=' from execute'):
    # object, arguments
    print(obj.name + s + '1')


@fit
def execute_replacement2(s=' from execute'):
    print('x' + s + '2')


class SubContext(ContextExample):
    def __init__(self, func=None):
        super(SubContext, self).__init__(func)
        self.name = 'Strategy Example x'



if __name__ == '__main__':

    contx = SubContext()
    contx()
    for _ in range(5):
        contx.random()
        contx()

