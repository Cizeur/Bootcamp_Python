import numpy as np


class NumPyCreator():

    def from_list(self, lst: list, dtype=None):
        return np.asarray(lst, dtype=dtype)

    def from_tuple(self, tpl: tuple, dtype=None):
        return np.asarray(tpl, dtype=dtype)

    def from_iterable(self, itr, dtype=None):
        return np.asarray(itr, dtype=dtype)

    def from_shape(self, shape, value=0, dtype=None):
        return np.full(shape, value, dtype)

    def random(self, shape, dtype=None, low=0.0, high=1.0):
        r = np.zeros(shape, dtype)
        r[:] = np.random.uniform(low, high, shape)
        return r

    def identity(self, shape, dtype=None):
        return np.identity(shape, dtype)


if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    shape = (3, 5)
    print(npc.from_shape(shape, 5))
    print(npc.random(shape))
    print(npc.identity(4))
