# -*- coding: UTF-8 -*-

__author__ = 'AlbericC'


class WithPref():
    def __init__(self) -> None:
        """Class for object expressing a preference among other objects
        """
        self.pref = list()


def pair(firsts, seconds) -> "generator":
    """Pairs together sets of objects. Returns a list of tuples representing the stable pairs.

    Each object in the parameters has to exhibit a .pref attribute:
    an ordered list of all elements from the other parameter.

    :param firsts @Iterable: They get their best option by design
    :param seconds @Iterable: They don't get their best option by design
    """
    if len(firsts) != len(seconds):
        raise IndexError("lengths must match")
    if any(not hasattr(item,"pref") for item in set(firsts) | set(seconds)):
        raise TypeError("Elements of the sets given must exhibit a .pref attribute")
    scores = {(f, s): (f.pref.index(s) + s.pref.index(f), f.pref.index(s)) for f in firsts for s in seconds}
    while scores:  # loop until candidates list is empty
        (f, s), best = min(scores.items(), key=lambda tup: tup[-1])
        for (k, v) in tuple(scores.items()):
            if v is best:
                yield k
            if s in k or f in k:
                scores.pop(k)


if __name__ == "__main__":
    """
    demo: the marriage problem in a population of 4 women and 4 men.
    """
    class Human(WithPref):
        def __init__(self, name):
            """Create a representation for a human and name it

            :param name @str: the name to give to this human.
            """
            super().__init__()
            assert name
            self.name = name

        def __repr__(self):
            return " ".join((self.__class__, self.name))

    women = A, B, C, D = [Human(name) for name in "Ally Betty Catherine Dana".split()]
    men = a, b, c, d, = [Human(name) for name in "Aaron Bobby Charles Dylan".split()]

    A.pref = a, b, c, d
    B.pref = b, d, c, a
    C.pref = a, c, d, b
    D.pref = b, a, c, d

    a.pref = D, C, B, A
    b.pref = D, B, C, A
    c.pref = B, C, D, A
    d.pref = D, C, A, B
    print()
    for w, m in pair(women, men):
        print("{0.name:>10} goes with {1.name:<10}".format(w, m))
