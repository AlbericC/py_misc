__author__ = "atrament"
__all__ = "talkative", "timed", "Memoize", "mro_list"

from time import time
from functools import wraps


def talkative(message=""):
    """decorator for custom trace of a function"""

    def talker(function):
        def wrapper(*args, **kwargs):
            print(message, function.__name__, args, kwargs)
            return function(*args, **kwargs)

        return wrapper

    return talker


def timed(f):
    """Decorator for (rough) performance measure"""

    @wraps(f)
    def wrapper(*args, **kwds):
        start = time()
        result = f(*args, **kwds)
        elapsed = time() - start
        if elapsed:
            print("\t\t\t{}{} took {b:03.2f} s to finish"
                  .format(f.__name__, args, kwds, b=elapsed))
        return result

    return wrapper


class Memoize:
    def __init__(self, function):
        """gives Memoize capability to a function"""
        self.function = function
        self.__name__ = function.__name__
        self.__doc__ = "::Memoize decorated::\n" + str(function.__doc__)
        self.memoized = dict()

    def __call__(self, *args):
        if args in self.memoized:
            return self.memoized.get(args)
        else:
            ans = self.memoized[args] = self.function(*args)
            return ans


def mro_list(some_class):
    """class decorator allowing to list all attributes and where
    they come from in the MRO through the '.mro_list' method"""

    def tell(inst):
        print("instance: " + ", ".join(a for a in vars(inst)
                                       if not a.startswith("__")))
        print("\n".join(["   class: " + ", ".join(a for a in vars(cls)
                                                  if not a.startswith("__"))
                         + " (" + cls.__name__ + ") "
                         for cls in type(inst).__mro__]))
        print("    meta: " + ", ".join(a for a in vars(type(type(inst)))
                                       if not a.startswith("__")) + " (" + type(type(inst)).__name__ + ")")

    some_class.mro_list = tell
    return some_class
