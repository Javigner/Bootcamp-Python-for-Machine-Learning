import numpy as np
import sys

class Numpycreator:
    def from_list(lst):
        if (isinstance(lst, list) == False and isinstance(lst, range) == False):
            sys.exit("lst must be a list")
        return np.array(lst)
    def from_tuple(tpl):
        if (isinstance(tpl, tuple) == False):
            sys.exit("tpl must be a tuple")
        return np.array(tpl)
    def from_iterable(itr):
        if isinstance(itr, range) == False:
            sys.exit("itr must be iterable")
        return np.array(itr)
    def from_shape(shape, value=0):
        if (isinstance(shape, tuple) == False):
            sys.exit("shape must be a tuple")
        return np.full(shape, value)
    def random(shape):
        if (isinstance(shape, tuple) == False):
            sys.exit("shape must be a tuple")
        return np.random.random_sample(shape)
    def identity(n):
        if (isinstance(n, int) == False):
            sys.exit("n must be an int")
        return np.identity(n)